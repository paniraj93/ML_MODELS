# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:33:38 2024

@author: bitm
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib.pyplot as plt
import seaborn as sns

iris=load_iris()
x,y=iris.data,iris.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

rf_clf=RandomForestClassifier(n_estimators=100,random_state=42)
rf_clf.fit(x_train,y_train)

y_pred=rf_clf.predict(x_test)
accuracy=accuracy_score( y_test,y_pred)
print(f"Accuracy: {accuracy :.2f}%")

print("Classification Report")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

conf_matrix=confusion_matrix(y_test ,y_pred)
print("Confusion Matrix: ")
print(conf_matrix)
plt.figure(figsize=(8,6))
sns.heatmap(conf_matrix,annot=True,fmt='d',cmap='Blues',xticklabels=iris.target_names,yticklabels=iris.target_names)
plt.ylabel('Actual')
plt.xlabel('predicted')
plt.title('Confusion Matrix')
plt.show()
