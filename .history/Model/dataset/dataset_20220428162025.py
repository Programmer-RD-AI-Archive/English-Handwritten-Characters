import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tqdm import tqdm


class DataSet:

    def __init__(self, data_dir="./data/") -> None:
        self.data_csv = pd.read_csv(data_dir + "english.csv")
        self.data_dir = data_dir

    def analytics(self):
        value_counts = dict(self.data_csv["label"].value_counts())
        return value_counts.keys()

    def get_labels(self,
                   labels: dict = None,
                   labels_r: dict = None,
                   idx: int = -1) -> tuple:
        if labels is None:
            labels = {}
        if labels_r is None:
            labels_r = {}
        print("Get Labels")
        for directory in tqdm(os.listdir(self.data_dir)):
            idx += 1
            labels[directory] = idx
            labels_r[idx] = directory
        np.save("./data/idx.npy", np.array(idx))
        np.save("./data/labels.npy", np.array(labels))
        np.save("./data/labels_r.npy", np.array(labels_r))
        return (labels, labels_r, idx)

    def load_data(self):
        labels, labels_r, idx = self.get_labels()
