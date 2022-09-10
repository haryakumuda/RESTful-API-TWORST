from contextlib import nullcontext
from ctypes.wintypes import WORD
from optparse import Values
import pandas as pd
import numpy as np
import re
import csv
import json
import mysql.connector
import sqlite3

db = sqlite3.connect('challenge.db')
db.text_factory = bytes
mycursor = db.cursor()
q_kamusalay = "select * from kamusalay"
t_kamusalay = pd.read_sql_query(q_kamusalay, db)

def lowercase(text):
    return text.lower()

def remove_unnecessary_char(text):
    text = re.sub('\n',' ', text)
    text = re.sub('rt',' ', text)
    text = re.sub('user',' ', text)
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))',' ',text)
    text = re.sub('  +',' ', text)
    return text
def remove_nonaplhanumeric(text):
    text = re.sub('[^0-9a-zA-Z]+', ' ', text)  #tolong dicek kalau tanda tanya dan tanda seru kan penting
    return text

alay_dict_map = dict(zip(t_kamusalay['alay'], t_kamusalay['cleaned'])) #zip menyatukan value dengan index yang sama
#alay_dict_items = alay_dict_map.items()
def normalize_alay(text):
    for word in alay_dict_map:
        return ' '.join([alay_dict_map[word] if word in alay_dict_map else word for word in text.split(' ')]) #Pelajari lagi masih bingung


'''    if word in alay_dict_map:
        alay_dict_map[word]
    else:
        word for word in text.split(' '):'''


def preprocess(text):
    text = lowercase(text) # 1
    text = remove_unnecessary_char(text) # 2
    text = remove_nonaplhanumeric(text) # 3
    text = normalize_alay(text) # 4
    return text







def process_csv(input_csv):

    try:
        t_input = pd.read_csv(input_csv, encoding='iso-8859-1')
    except:
        print("Trying another Encoding")

    try:
        t_input = pd.read_csv(input_csv, encoding='utf-8')
    except:
        print("CSV File is unreadable")

    try:

        first_column = t_input.iloc[:100, 0] #Nanti kalau launching 100 nya dihilangkan
        print(first_column)

        for tweet in first_column:
            tweet_clean = preprocess(tweet)
            query_tabel = "insert into tweet (tweet_mentah,tweet_clean) values (?, ?)"
            val = (tweet, tweet_clean)
            mycursor.execute(query_tabel, val)
            db.commit()
            print(tweet)
    except:
        print("CSV File is unreadable")



def process_text(input_text):
    try: 
        output_text = preprocess(input_text)

        print(input_text)
        print(output_text)

        query_text = "insert into tweet (tweet_mentah,tweet_clean) values (?, ?)"
        val = (input_text, output_text)
        mycursor.execute(query_text, val)
        db.commit()
    except:
        print("Text is unreadable")


#input_csv = "data.csv" #Nanti Input client disini, sementara pake data.csv dulu
#input_text = "CONTOH Alay Bangsat Kasar User HTTPS://www.Facebook.com Adek hahaha 3x bangsat,,,..,.,.!!!@@@ aww" #Nanti Input text masuk sini, ini sementara
#process_csv(input_csv)
#process_text(input_text)






#yang bawah ga dipake lagi

'''
print(t_datatweet.head(10))
t_datatweet['Tweet'] = t_datatweet['Tweet'].apply(preprocess) #untuk apply fungsi preprocess / cleaning data pakai .apply
print(t_datatweet.head(10))
#t_datatweet['Tweet'] = kolom
'''

'''

db = mysql.connector.connect(
            host = 'localhost',
            user = 'haryauyee',
            password = 'password',
            database = 'binargold'
            )

mycursor = db.cursor(buffered=True)

q_kamusalay = "select * from kamusalay"
q_abusive = "select * from abusive"
q_datatweet = "select * from datatweet"
t_kamusalay = pd.read_sql(q_kamusalay, db)
t_abusive = pd.read_sql(q_abusive, db)
t_datatweet = pd.read_sql(q_datatweet, db)


input_user = input("Masukan Tweet Anda: ")

output_user = preprocess(input_user)

Tweet_user = [output_user]
print(Tweet_user)
HS_user = None
Abusive_user = None
HS_Individual_user = None
HS_Group_user = None
HS_Religion_user = None
HS_Physical_user = None
HS_Gender_user = None
HS_Other_user = None
HS_Weak_user = None
HS_Moderate_user = None
HS_Strong_user = None

#query = ("insert into"
#        "datatweet (Tweet, HS, Abusive, HS_Individual, HS_Group, HS_Relegion, HS_Physical, HS_Gender, HS_Other, HS_Weak, HS_Moderate, HS_Strong)"
#        "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)"
#        )
#values = (Tweet_user, HS_user, Abusive_user, HS_Individual_user, HS_Group_user, HS_Religion_user, HS_Physical_user, HS_Gender_user, HS_Other_user, HS_Weak_user, HS_Moderate_user, HS_Strong_user)

query = ("insert into"
        " datatweet (Tweet)"
        " values (%s)")
values = (Tweet_user)
mycursor.execute(query, values)
db.commit()

print(t_datatweet.tail(5))
'''