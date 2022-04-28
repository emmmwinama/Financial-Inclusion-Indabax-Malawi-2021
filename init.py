import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
np.random.seed(123)
warnings.filterwarnings('ignore')
%matplotlib inline

#importing data
train_data = pd.read_csv('Data/Train_v2.csv')
test_data = pd.read_csv('Data/Test_v2.csv')


# print shape
print('train data shape :', train_data.shape)
print('test data shape :', test_data.shape)

train data shape : (23524, 13)
test data shape : (10086, 12)

