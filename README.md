# URL-Spam-Classification

The aim of this project was to create a web application that can predict whether a particular URL is a spam URL or non-spam URL. Now a days, hackers use such spam URLs to carry out phishing attacks on the internet to steal sensitive user information. In order to avoid such attacks, I created a machine learning model that classify a URL as spam or non-spam.

# About the Dataset

The dataset consists of only two columns:
- url : This is the content column that contains the various URLs.
- is_spam : This is the label column that contains either of the two boolean values, True or False.

# Data Cleaning and Preprocessing

First, I checked if there is any empty row. There were no empty rows in the dataset. Next, I checked if there are any duplicate rows and removed all duplicate rows and kept only the first row of the duplicate ones. 

While Data Preprocessing, I created the following columns:
- url_length : number of characters in the url
- ssl_certified : if the URL contains 'https' in it
- digit_count : number of digits in the URL
- hash_count : number of hash in the URL
- hyphen_count : number of hyphen in the URL
- underscore_count : number of underscore in the URL
- question_mark_count : number of question mark in the URL
- contains_www : if the URL contains 'www' in it
- contains_discount : if the URL contains 'discount' word in it
- contains_sale : if the URL contains 'sale' word in it
- word_count : number of words in the URL

I read a few articles about phishing attacks and preformed some data analysis and found that generally spam URLs are longer than non-spam. The spam URLs are generally not SSL certified. Generally, the spam URLs contain more number of special characters in comparison to non-spam URLs.

# Why I used Decision Tree ?

I wanted a classification model that can classify the data with very high accuracy and at the same time is faster. While classification algorithms like Logistic Regression, Support Vector Machine, etc. are faster but the accuracy is often not upto the mark, in the other hand, algorithms like Random Forest, Artificial Neural Network provide higher accuracy but are slower than other algorithms.

# Why I didn't perform NLP ?

Every non-spam URL has a unique domain name. Since the dataset was highly imbalanced and had more number of non-spam URL, so the vectorized matrix would have been of very large size which would have made training the classification model, a really difficult task. 

# Accuracy of the model

Accuracy over validation dataset : 96.6%

# Web Deployment

I created a web application using streamlit where the classification runs in the backend and classifies the input URLs as spam or non-spam. I deployed the web application on streamlit cloud.

Link - https://share.streamlit.io/adityarajsahu/url-spam-classification/main/app.py

# Further Development

I have planned to deploy this classification model as a chrome extension, so that the user can access it faster.