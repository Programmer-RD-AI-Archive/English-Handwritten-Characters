import os

import matplotlib.pyplot as plt
import pandas as pd


class DataSet:

    def __init__(self, data_dir="./data/") -> None:
        self.data_csv = pd.read_csv(data_dir + "english.csv")
        self.data_dir = data_dir

    def get_labels(self,
                   labels: dict = {},
                   labels_r: dict = {},
                   idx: int = -1):
        pass

    def load_data(self):
        pass
