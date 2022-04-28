import os
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DataSet:
    def __init__(self, data_dir="./data/") -> None:
        self.data_csv = pd.read_csv(data_dir + "english.csv")
        self.data_dir = data_dir

    def get_labels(self, labels: dict = {}, labels_r: dict = {}, idx: int = -1):
        for directory in os.listdir(self.data_dir):
            idx += 1
            labels[directory] = idx
            labels_r[idx] = directory
        np.save("./data/idx.npy",np.array(idx))
        

    def load_data(self):
        pass
