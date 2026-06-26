#1. Importing Libraries
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#2. Importing the Dataset
data = pd.read_csv("news.csv")
data.head()

#3. Preprocessing Dataset
data = data.drop(["Unnamed: 0"], axis=1)
data.head(5)

#4. Data Encoding
le = preprocessing.LabelEncoder()
le.fit(data['label'])
data['label'] = le.transform(data['label'])

#5. Variables Setup
