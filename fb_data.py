import glob
import itertools
import json
import os
import re

import altair as alt
import pandas as pd
from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# result = []
# folders = os.listdir('inbox/')
# for i in range(len(folders)):
#     folder = folders[i]
#     with open(f'inbox/{folder}/message_1.json', 'r') as f:
#         result.append(json.load(f))
#
# result
# with open('messages.txt', "w") as out:
#      json.dump(result, out)

with open('messages.txt') as json_file:
    data = json.load(json_file)


def top_50_words(facebook_name):
    # Making a list of every message sent by me
    message = []
    for i in range(len(data)):
        for m in range(len(data[i]['messages'])):
            if data[i]['messages'][m]['sender_name'] == facebook_name:
                try:
                    message.append(data[i]['messages'][m]['content'])
                except:
                    pass

    # Removing messages facebook sent whenever I sent a link/attachment
    stopword = 'You sent an attachment.'
    for i, sub_list in enumerate(message):
            if stopword in sub_list:
                    del message[i]


    stopword = 'You sent a link.'
    for i, sub_list in enumerate(message):
            if stopword in sub_list:
                    del message[i]

    # Removing all links I sent (using regex)
    for i in range(len(message)):
        message[i] = re.sub(r'http\S+', '', message[i])

    # Making everything lowercase
    for i in range(len(message)):
        message[i] = message[i].lower()

    # Making a list of words from my list of messages using regex to include "don't" as a word and not seperating on apostrophes
    word_list = []
    for words in list(message):
        rgx = re.compile("([\w][\w']*\w)")
        word_list = word_list + rgx.findall(words)

    # Removing stopwords
    stop_words = stopwords.words('english')
    stop_words.append("i'm")
    words = [w for w in word_list if not w in stop_words]

    # Using counter to easily count the amount of times each word appears
    word_count = Counter(words)
    word_count.most_common()

    # my top 10 words over ALL years
    df = pd.DataFrame([word for word in word_count.most_common()[:50] ],columns= ['word','count'])
    return df



top_50_words('Jordan Milne')['word'].tolist()

def message_year(facebook_name, number_of_words, year):
    message = []
    for i in range(len(data)):
        for m in range(len(data[i]['messages'])):
            if data[i]['messages'][m]['sender_name'] == facebook_name and pd.to_datetime(data[i]['messages'][m]['timestamp_ms'],unit='ms').year == year:
                try:
                    message.append(data[i]['messages'][m]['content'])
                except:
                    pass

    # removing the text attached with attachments
    stopword = 'You sent an attachment.'
    for i, sub_list in enumerate(message):
            if stopword in sub_list:
                    del message[i]

    # removing the text attached with links
    stopword = 'You sent a link.'
    for i, sub_list in enumerate(message):
            if stopword in sub_list:
                    del message[i]

    # removing attachments
    for i in range(len(message)):
        message[i] = re.sub(r'http\S+', '', message[i])

    # making everything lowercase
    for i in range(len(message)):
        message[i] = message[i].lower()

    # using regex to seperate words (inluding words with apostrophes)
    word_list = []
    for words in list(message):
        rgx = re.compile("([\w][\w']*\w)")
        word_list = word_list + rgx.findall(words)

    # removing stop words (less interesting when my number 1 used word is 'the')
    stop_words = stopwords.words('english')
    stop_words.append("i'm")
    words = [w for w in word_list if not w in stop_words]

    word_count = Counter(words)

    # my top 10 words over ALL years
    top_words = top_50_words('Jordan Milne')['word'].tolist()[:number_of_words]
    # df = pd.DataFrame([word for word in word_count.most_common() if word[0] in top10],columns= ['word','count'])
    df = pd.DataFrame([word for word in word_count.most_common() if word[0] in top_words],columns= ['word','count'])
    df['year'] = year
    return df



a = message_year('Jordan Milne', 5, 2011)
a
for i in range(2010,2020+1):
    final = pd.concat([a, message_year(i)])
    a = final
df1 = final.reset_index(drop=True)
df2 = df1[2:32]
df3 = df2.to_dict()
df1.pivot(index='year',columns='word',values='count').plot(figsize=(15,10))
