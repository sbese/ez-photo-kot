import vk
from moya import retard
from saveallphotos import saveallphotomain
from saveallphotos import savediaphoto
tokenn=retard()
session = vk.Session(access_token=tokenn)
api = vk.API(session,v='5.57', lang='ru')
while 1==1:
    print('выберете действие')
    print('1.загрузка всех фотографий из диалогов')
    task = input()
    if task=='1':
        saveallphotomain(api)
    if task=='2':
        savediaphoto(api)
