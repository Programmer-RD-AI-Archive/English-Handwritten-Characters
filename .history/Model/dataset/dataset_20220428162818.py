import os
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


class DataSet:
    def __init__(self, data_dir="./raw/") -> None:
        self.data_csv = pd.read_csv(data_dir + "english.csv")
        self.data_dir = data_dir

    def analytics(self):
        value_counts = dict(self.data_csv["label"].value_counts())
        data = dict(data['label'].value_counts())
classification_class = list(data.keys()) 
number_of_values = list(data.values()) 
   

fig = plt.figure(figsize = (25, 7)) 
  
# creating the bar plot 
plt.bar(classification_class, number_of_values, color ='green',  
        width = 0.4) 
  
plt.xlabel("Classifcation Class") 
plt.ylabel("Number of Values") 
plt.title("Classes In Relation to Values") 
plt.savefig('./data/test.png') 
plt.close()
        return value_counts.keys()

    def get_labels(self, labels: dict = {}, labels_r: dict = {}, idx: int = -1) -> tuple:
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
