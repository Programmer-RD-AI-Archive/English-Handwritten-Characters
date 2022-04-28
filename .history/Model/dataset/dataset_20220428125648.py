import matplotlib.pyplot as plt
import pandas as pd


class DataSet:

    def __init__(self, data_dir="./data/") -> None:
        data_csv = pd.read_csv(data_dir + "english.csv")

    def get_labels(self):
        pass

    def load_data(self):
        pass
