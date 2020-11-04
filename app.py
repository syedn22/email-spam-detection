import pickle 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

df = pd.read_csv("emails.csv")
df.head(20)

df.isnull().sum()
df.describe()
df.corr()

X = df.iloc[:,1:3001]
Y = df.iloc[:,-1].values

train_x,test_x,train_y,test_y = train_test_split(X,Y,test_size = 0.25)

mnb = MultinomialNB(alpha=1.9)         
mnb.fit(train_x,train_y)
y_pred1 = mnb.predict(test_x)
print("Accuracy Score for Naive Bayes : ", accuracy_score(y_pred1,test_y))

# rfc = RandomForestClassifier(n_estimators=100,criterion='gini')
# rfc.fit(train_x,train_y)
# y_pred3 = rfc.predict(test_x)
# print("Accuracy Score : ", accuracy_score(y_pred3,test_y))
  
email_spam_model = 'email_spam_model.sav'
pickle.dump(mnb, open(email_spam_model, 'wb'))

loaded_model = pickle.load(open(email_spam_model, 'rb'))
result = loaded_model.predict(test_x) 
print(result)
