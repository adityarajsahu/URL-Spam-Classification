import pandas as pd
from sklearn.preprocessing import LabelEncoder
import nltk
nltk.download('punkt')

def preprocessor(df):
    df = df.drop_duplicates(keep='first')
    df['url_length'] = df['url'].apply(lambda x : len(x))
    df['ssl_certified'] = df['url'].apply(lambda x : 1 if 'https' in x else 0)

    df['digit_count'] = df['url'].apply(lambda x : len("".join(_ for _ in x if _.isdigit())))
    df['hash_count'] = df['url'].apply(lambda x : len("".join(_ for _ in x if _ == '#')))
    df['hyphen_count'] = df['url'].apply(lambda x : len("".join(_ for _ in x if _ == '-')))
    df['underscore_count'] = df['url'].apply(lambda x : len("".join(_ for _ in x if _ == '_')))
    df['question_mark_count'] = df['url'].apply(lambda x : len("".join(_ for _ in x if _ == '?')))

    df['contains_www'] = df['url'].apply(lambda x: 1 if 'www' in x else 0)
    df['contains_subscribe'] = df['url'].apply(lambda x : 1 if 'subscribe' in x else 0)
    df['contains_discount'] = df['url'].apply(lambda x : 1 if 'discount' in x else 0)
    df['contains_sale'] = df['url'].apply(lambda x : 1 if 'sale' in x else 0)

    df['url'] = df['url'].apply(lambda x : x.replace('/', ' '))
    df['url'] = df['url'].apply(lambda x: x.replace('.', ' '))
    df['url'] = df['url'].apply(lambda x: x.replace('?', ' '))
    df['url'] = df['url'].apply(lambda x: x.replace('#', ' '))
    df['word_count'] = df['url'].apply(lambda x : len(nltk.word_tokenize(x)))

    le = LabelEncoder()
    le.fit(df['is_spam'])
    df['is_spam'] = le.transform(df['is_spam'])
    return df
