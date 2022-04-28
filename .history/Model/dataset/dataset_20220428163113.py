import os
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


class DataSet:
    def __init__(self, data_dir="./raw/", save_dir="./data/") -> None:
        self.data_csv = pd.read_csv(data_dir + "english.csv")
        self.data_dir = data_dir
        self.save_dir = save_dir

    def analytics(self,plot=False) -> tuple:
        value_counts = dict(self.data_csv["label"].value_counts())
        try:
        classification_class = list(value_counts.keys())
        number_of_values = list(value_counts.values())
        plt.figure(figsize=(25, 7))
        plt.bar(classification_class, number_of_values, color="green", width=0.4)
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

    def get_labels(self, labels: dict = {}, labels_r: dict = {}, idx: int = -1) -> tuple:
        print("Get Labels")
        for directory in tqdm(self.analytics()[0]):
            idx += 1
            labels[directory] = idx
            labels_r[idx] = directory
        np.save("./data/idx.npy", np.array(idx))
        np.save("./data/labels.npy", np.array(labels))
        np.save("./data/labels_r.npy", np.array(labels_r))
        return (labels, labels_r, idx)

    def load_data(self):
        labels, labels_r, idx = self.get_labels()
