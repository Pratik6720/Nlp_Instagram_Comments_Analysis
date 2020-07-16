from instagram_private_api import Client, ClientCompatPatch
import os
file = open('password.txt')
data =  file.readlines()
user_name = data[0].strip()
password = data[1]

api = Client(user_name, password)

# for x in comments['comments']:
#     print(x['text'])

comments = api.media_n_comments('2344478637069676132_347696668',10)

for x in comments:
    usr = api.user_info(x['user_id'])
    print(usr)
    usrname = usr['user']['username']

    print('{0} : {1}'.format(usrname,x['text']))

    # print(api.username_info('prataik_6720'))
