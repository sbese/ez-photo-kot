import vk,json,time,os
from progressbar import ProgressBar
from moya import retard
from saveallphotos import savephotomain
tokenn="cdc848e9d420a8117b3a2547f357050560e1533200c81f5722cb3fa10d5dcacfcb1448ccf2a84fbbb5f00"
session = vk.Session(access_token=tokenn)
api = vk.API(session,v='5.57', lang='ru')
def messagessave(getapi):
    global api,pid
    api =getapi
    dia=api.messages.getDialogs(count=200,preview_length=0)
    ji=0
    while ji< len(dia["items"]):
        print(str(ji+1)+"/"+str(len(dia["items"])))
        dia["items"][ji]["message"].setdefault("chat_id")
        if dia["items"][ji]["message"]["chat_id"]==None and str(dia["items"][ji]["message"]["user_id"])[0]!="-":
            time.sleep(0.3)
            pid=dia["items"][ji]["message"]["user_id"]
            tiname=api.users.get(user_ids=pid)
            time.sleep(0.5)
            print(str(pid)+tiname[0]["first_name"]+" "+tiname[0]["last_name"])
            nextuser(pid)
        ji=ji+1
def nextuser(pid):
    global f
    name_user=api.users.get(user_ids=pid)
    global namedd
    namedd= name_user[0]["first_name"]+" "+name_user[0]["last_name"]+"сообщения"
    name_owner=api.users.get()
    global named
    named = name_owner[0]["first_name"]+" "+name_owner[0]["last_name"]
    try:
        os.makedirs(str(named+"/"+namedd))
    except OSError:
        pass
    f = open(str(named)+"/"+str(namedd)+"/"+str(pid)+'.html', 'w')
    allmessages('0',0)
    f.close()
    time.sleep(0.4)
def allmessages(startfrom,block):
    global i,a,link
    print("блок "+str(block+1))
    i = 0
    a=api.messages.getHistory(peer_id=pid,media_type="photo",photo_sizes=1,count=200,start_from=startfrom)
    time.sleep(0.3)
    pbar  = ProgressBar(maxval=200).start()
    while i<len(a["items"]):
        fwrite(i)
        i=i+1
        pbar.update(i)
    pbar.finish()
    a.setdefault("next_from")
    if a["next_from"]!=None:
        allmessages(a["next_from"],block+1)


def fwrite(index):
    global f
    f.write("<div>\n")
    f.write("<div>\n")
    f.write(str(a["items"][index]["photo"]["id"]) + '\n')
    f.write(str(a["items"][index]["photo"]["owner_id"]) + '\n')
    f.write("</div>\n")
    f.write("<img src=" + link + '>\n')
    f.write("</div>\n")
