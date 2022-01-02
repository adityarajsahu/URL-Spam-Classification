import pandas as pd
from preprocessing import preprocessor
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

df = pd.read_csv("DATASET/url_spam_classification.csv")
df = preprocessor(df)

#df.to_csv("new_dataset.csv")

features = [feature for feature in df.columns if feature not in ["url", "is_spam"]]
X_train, X_val, Y_train, Y_val = train_test_split(df[features], df['is_spam'], test_size=0.2, shuffle=True)

dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(X_train, Y_train)

filename = 'SAVED MODEL/model_02-01-2022.sav'
pickle.dump(dt_classifier, open(filename, 'wb'))

