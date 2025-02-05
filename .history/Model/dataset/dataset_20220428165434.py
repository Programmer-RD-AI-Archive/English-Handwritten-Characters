import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tqdm import tqdm


class DataSet:

    def __init__(self, data_dir="./raw/", save_dir="./data/") -> None:
        self.data_csv = pd.read_csv(data_dir + "english.csv")
        self.data_dir = data_dir
        self.save_dir = save_dir

    def analytics(self, plot=False) -> tuple:
        value_counts = dict(self.data_csv["label"].value_counts())
        if plot:
            classification_class = list(value_counts.keys())
            number_of_values = list(value_counts.values())
            plt.figure(figsize=(25, 7))
            plt.bar(classification_class,
                    number_of_values,
                    color="green",
                    width=0.4)
            plt.xlabel("Classifcation Class")
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

    def get_labels(self,
                   labels: dict = {},
                   labels_r: dict = {},
                   idx: int = -1) -> tuple:
        print("Get Labels")
        for class_name in tqdm(self.analytics()[0]):
            idx += 1
            labels[class_name] = idx
            labels_r[idx] = class_name
        np.save("./data/idx.npy", np.array(idx))
        np.save("./data/labels.npy", np.array(labels))
        np.save("./data/labels_r.npy", np.array(labels_r))
        return (labels, labels_r, idx)

    def load_image(self, image_file_path, img_size: tuple = (56, 56)):
        img = cv2.imread(self.data_dir + image_file_path)
        img = cv2.resize(img, (img_size))
        img = img / 255.0  # TODO Normalization
        return img

    @staticmethod
    def create_np_eye_list_with_label(idx, class_name, labels):
        current_idx = labels[class_name] + 1
        max_idx = idx + 1
        np_eye = np.eye(current_idx, max_idx)
        np_eye = np_eye[-1]
        return np_eye

    def load_data(self):
        data = []
        labels, labels_r, idx = self.get_labels()
        for iter_idx in range(len(self.data_csv)):
            image_dir, classes_name = list(self.data_csv.iloc[iter_idx])
            img = self.load_image(image_dir)
            label_np_eye = self.create_np_eye_list_with_label(
                idx, classes_name, labels)
