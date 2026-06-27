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
embedding_dim = 50
max_length = 54
padding_type = 'post'
trunc_type = 'post'
oov_tok = "<OOV>"
training_size = 3000
test_portion = 0.1

#6. Tokenization 
title = []
text = []
labels = []
for x in range(training_size):
    title.append(data['title'][x])
    text.append(data['text'][x])
    labels.append(data['label'][x])

tokenizer1 = Tokenizer()
tokenizer1.fit_on_texts(title)
word_index1 = tokenizer1.word_index
vocab_size1 = len(word_index1)
sequences1 = tokenizer1.texts_to_sequences(title)
padded1 = pad_sequences(sequences1, padding=padding_type, truncating=trunc_type)

#7. Splitting Data for Training and Testing
split = int(test_portion * training_size)
training_sequences1 = padded1[split:training_size]
test_sequences1 = padded1[0:split]
test_labels = labels[0:split]
training_labels = labels[split:training_size]
#8. Reshaping Data for LSTM
training_sequences1 = np.array(training_sequences1)
test_sequences1 = np.array(test_sequences1)

#9. Generating Word Embedding
