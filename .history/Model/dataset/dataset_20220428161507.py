import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class DataSet:

    def __init__(self, data_dir="./data/") -> None:
        self.data_csv = pd.read_csv(data_dir + "english.csv")
        self.data_dir = data_dir

    def get_labels(self,
                   labels: dict = None,
                   labels_r: dict = None,
                   idx: int = -1):
        if labels is None:
            labels = {}
        if labels_r is None:
            labels_r = {}
        for directory in os.listdir(self.data_dir):
            idx += 1
            labels[directory] = idx
            labels_r[idx] = directory
        np.save()

    def load_data(self):
        pass
