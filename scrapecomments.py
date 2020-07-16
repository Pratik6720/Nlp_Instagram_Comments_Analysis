from instagram_private_api import Client, ClientCompatPatch
from prettytable import PrettyTable
import re
import pandas as pd
import excel_exporter as pr

y = PrettyTable()
i=0
y.field_names = ["Username","Text"]
import os
file = open('password.txt')
data =  file.readlines()
user_name = data[0].strip()
password = data[1]

api = Client(user_name, password)

usrprat = []
cmtprat = []

comments = api.media_n_comments('2340343289037185986_347696668',80)

def clean(text):

    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U0001F1F2-\U0001F1F4"  # Macau flag
                               u"\U0001F1E6-\U0001F1FF"  # flags
                               u"\U0001F600-\U0001F64F"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f910-\U0001f937"
                               u"\U0001f900-\U0001f9ff"
                               u"\U0001F1F2"
                               u"\U0001F1F4"
                               u"\U0001F620"
                               u"\u200d"
                               u"\u2640-\u2642"
                               "]+", flags=re.UNICODE)

    for x in text:
        x[1] = emoji_pattern.sub(r'', x[1])
        cmtprat.append(x[1])
    return text


scraped_data = []

for x in comments:
    # print(x)
    usr = api.user_info(x['user_id'])
    # print(usr)
    usrname = usr['user']['username']
    usrprat.append(usrname)
    comment = x['text']
    scraped_data.append([usrname,comment])
    print(i)
    i = i + 1


cleaned_data = clean(scraped_data)
for x in cleaned_data:
    y.add_row(x)



print(y)

pr.export(usrprat,cmtprat)

