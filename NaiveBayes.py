import pandas as pd
import numpy as np

tennis = pd.read_csv("tennis.csv")
tennis_train = tennis[:10]
tennis_test = tennis[10:]

features = ['outlook','temp','humidity','windy']
feature_values = ['sunny','cool','high',True]
class_labels = ['yes','no']
p_list = []
label = 'play'
n = len(tennis)
f = len(features)
for class_label in class_labels:
  temp = tennis.groupby([label]).count()
  p_of_class = (temp.loc[(class_label)][0])/n
  print(p_of_class)
  for i in range(f):
    feature = features[i]
    feature_value = feature_values[i]
    temp = tennis.groupby([feature,label]).count()
    numer = (temp.loc[(feature_value,class_label)][0])
    denom = (tennis.groupby([label]).count().loc[(class_label)][0])
    prob = numer/denom
    print(feature_value,class_label, numer,denom)
    p_of_class *= prob
  p_list.append(p_of_class) 
print(p_list)
print(class_labels[p_list.index(max(p_list))])
