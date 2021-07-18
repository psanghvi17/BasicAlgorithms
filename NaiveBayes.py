import pandas as pd
import numpy as np
tennis = pd.read_csv("tennis.csv")
tennis_train = tennis[:10]
tennis_test = tennis[10:]
features = ['outlook','temp','humidity','windy']
class_labels = ['yes','no']
p_list = []
label = 'play'
n = len(tennis)
f = len(features)
final_labels = []
for feature_values in tennis_test.values.tolist():
	final_label = ""
	final_prob = 0
	for class_label in class_labels:
		p_of_class = len(tennis[tennis[label] == class_label])/n
		for i in range(f):
			feature = features[i]
			feature_value = feature_values[i]
			numer = len(tennis.loc[(tennis[feature] == feature_value) & (tennis[label] == class_label)])
			denom = len(tennis[tennis[label] == class_label])
			prob = numer/denom
			#print(feature_value,class_label, numer,denom)
			p_of_class *= prob
		print("before if",p_of_class,final_prob,class_label)
		if final_prob < p_of_class:
			final_prob = p_of_class
			final_label = class_label
			print("in if",p_of_class,final_prob,class_label)
	print("after loop",final_label,final_prob)
	final_labels.append(final_label)
print(final_labels)
test_labels = tennis_test.play.tolist()
result = [True if test_labels[i] == final_labels[i] else False for i in range(len(test_labels))]
print(result)
