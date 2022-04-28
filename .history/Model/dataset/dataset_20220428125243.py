import pandas as pd
import matplotlib.pyplot as plt

class DataSet:
    def __init__(self,data_dir="./data/") -> None:
        data_csv = pd.read_csv('./data')
