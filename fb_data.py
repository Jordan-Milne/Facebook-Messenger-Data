import json
import glob
import os
import pandas as pd
import itertools
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

## Loading all the JSON files from seperate folders into one file
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

# Opening the JSON file of all my messages
with open('messages.txt') as json_file:
    data = json.load(json_file)

# Making a list of every message sent by me
message = []
for i in range(len(data)):
    for m in range(len(data[i]['messages'])):
        if data[i]['messages'][m]['sender_name'] == 'Jordan Milne':
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
nltk.download('stopwords')
stop_words = stopwords.words('english')
stop_words.append("i'm")
words = [w for w in word_list if not w in stop_words]

# Using counter to easily count the amount of times each word appears
word_count = Counter(words)
word_count.most_common()
