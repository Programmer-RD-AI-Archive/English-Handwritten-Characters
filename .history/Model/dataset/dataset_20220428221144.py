import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from PIL import Image
from Model.preproccessing import PreProccessing


class DataSet:

    def __init__(
        self,
        data_dir: str = "./raw/",
        save_dir: str = "./data/",
        preproccessing:PreProccessing = PreProccessing(),
    ) -> None:
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.data_csv = pd.read_csv(data_dir + "english.csv")
        self.data_dir = data_dir
        self.save_dir = save_dir
        self.transformation = preproccessing.forward()

    def analytics(self,
                  plot: bool = False,
                  figsize_of_analytics: tuple = ()) -> tuple:
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        value_counts = dict(self.data_csv["label"].value_counts())
        if plot:
            classification_class = list(value_counts.keys())
            number_of_values = list(value_counts.values())
            plt.figure(figsize=figsize_of_analytics)
            plt.bar(classification_class,
                    number_of_values,
                    color="green",
                    width=0.4)
            plt.xlabel("Classification Class")
            plt.ylabel("Number of Values")
            plt.title("Classes In Relation to Values")
            plt.savefig(f"{self.save_dir}Classes In Relation to Values.png")
            plt.close()
            return (
                value_counts.keys(),
                f"{self.save_dir}Classes In Relation to Values.png",
                value_counts,
            )
        return (
            value_counts.keys(),
            None,
            value_counts,
        )
    
    # Loading Data Pytorch
    
    def get_labels(self,
                   labels: dict = None,
                   labels_r: dict = None,
                   idx: int = 0) -> tuple:
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if labels is None:
            labels = {}
        if labels_r is None:
            labels_r = {}
        print("Get Labels")
        for class_name in tqdm(self.analytics()[0]):
            idx += 1
            labels[class_name] = idx
            labels_r[idx] = class_name
        np.save("./data/idx.npy", np.array(idx))
        np.save("./data/labels.npy", np.array(labels))
        np.save("./data/labels_r.npy", np.array(labels_r))
        return (labels, labels_r, idx)

    def load_image(self, image_file_path: str,
                   img_size: tuple = (56, 56)) -> list:
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        img = cv2.imread(self.data_dir + image_file_path)
        img = cv2.resize(img, (img_size))
        img = self.transformation(Image.fromarray(img))
        img = img / 255.0  # TODO Normalization
        return img

    @staticmethod
    def create_np_eye_list_with_label(idx: int, class_name: any,
                                      labels: dict) -> np.array:
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        current_idx = labels[class_name]
        max_idx = idx
        np_eye = np.eye(current_idx, max_idx)
        np_eye = np_eye[-1]
        return np_eye

    def data_to_X_train_y_train_X_test_y_test(self,
                                              data: list,
                                              test_size: float = 0.25,
                                              shuffle: bool = True) -> tuple:
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        print("Converting Data -> X,y + train,test")
        X = []
        y = []
        for X_iter, y_iter in tqdm(data):
            X.append(X_iter)
            y.append(y_iter)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, shuffle=shuffle)
        X_train = torch.from_numpy(np.array(X_train))
        y_train = torch.from_numpy(np.array(y_train))
        X_test = torch.from_numpy(np.array(X_test))
        y_test = torch.from_numpy(np.array(y_test))
        torch.save(X_train, self.save_dir + "X_train.pt")
        torch.save(X_train, self.save_dir + "X_train.pth")
        torch.save(X_test, self.save_dir + "X_test.pt")
        torch.save(X_test, self.save_dir + "X_test.pth")
        torch.save(y_train, self.save_dir + "y_train.pt")
        torch.save(y_train, self.save_dir + "y_train.pth")
        torch.save(y_test, self.save_dir + "y_test.pt")
        torch.save(y_test, self.save_dir + "y_test.pth")
        return (X_train, X_test, y_train, y_test)

    def load_data(self) -> tuple:
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        data = []
        labels, labels_r, idx = self.get_labels()
        print("Loading Images and Creating Data")
        for iter_idx in tqdm(range(len(self.data_csv))):
            image_dir, classes_name = list(self.data_csv.iloc[iter_idx])
            img = self.load_image(image_dir)
            label_np_eye = self.create_np_eye_list_with_label(
                idx, classes_name, labels)
            data.append([img, label_np_eye])
        np.random.shuffle(data)
        X_train, X_test, y_train, y_test = self.data_to_X_train_y_train_X_test_y_test(
            data)
        return (X_train, X_test, y_train, y_test, data, labels, labels_r, idx)
