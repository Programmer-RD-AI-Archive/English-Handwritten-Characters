import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class DataSet:

    def __init__(self, data_dir="./data/") -> None:
        data_csv = pd.read_csv(data_dir + "english.csv")

    def get_labels(self, labels: dict = None):
        if labels is None:
            labels = {}
        pass

    def load_data(self):
        pass
