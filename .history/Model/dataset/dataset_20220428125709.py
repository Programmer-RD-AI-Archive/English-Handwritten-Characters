import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DataSet:
    def __init__(self, data_dir="./data/") -> None:
        data_csv = pd.read_csv(data_dir + "english.csv")

    def get_labels(self,labels:dict={},labels_r:dict={},idx:int=):
        pass

    def load_data(self):
        pass
