import vk
from moya import retard
from saveallphotos import saveallphotomain
from saveallphotos import savediaphoto
tokenn="b9264d30e10e88ec6ff2301f049e4cffb35dbbd46be55c952f0506ee4cb6ecf1d8762bd430d3d4da1df24"
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
