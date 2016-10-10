import vk,requests, shutil,os,time
from progressbar import ProgressBar
from moya import retard
def chartonum(simvol):
        if simvol=="":
            return    
        elif simvol=="s":
                return 1
        elif simvol=="m":
                return 2
        elif simvol=="x":
                return 3
        elif simvol=="y":
                return 4
        elif simvol=="z":
                return 5
        elif simvol=="w":
                return 6
        else:
                return 0
def bestphoto(index):
        maxdef=0
        j=0

        while j<len(a["items"][index]["photo"]["sizes"]):
                vz=chartonum(a["items"][index]["photo"]["sizes"][j]["type"])
                if vz > maxdef:
                        maxdef=vz
                        bphoto=a["items"][index]["photo"]["sizes"][j]["src"]
                j=j+1
        return bphoto
def fwrite(index):
        global f
        f.write("<div>\n")
        f.write("<div>\n")
        f.write(str(a["items"][index]["photo"]["id"])+'\n')
        f.write(str(a["items"][index]["photo"]["owner_id"])+'\n')
        f.write("</div>\n")
        f.write("<img src="+link+'>\n')
        f.write("</div>\n")
def savefile(src,block):
        global nphoto,nexcept
        nphoto=nphoto+1
        try:
                pic = requests.get(link,stream = True)
                with open(str(named)+"/"+str(namedd)+"/"+str(block)+str(i)+".png","wb") as filei:
                        shutil.copyfileobj(pic.raw,filei)
        except BaseException:
            nexcept=nexcept+1
            print("("+nexcept+")")
            pass
def allphotos(startfrom,block):
    global i,a,link
    print("блок "+str(block+1))
    i = 0
    a=api.messages.getHistoryAttachments(peer_id=pid,media_type="photo",photo_sizes=1,count=200,start_from=startfrom)
    time.sleep(0.3)
    pbar  = ProgressBar(maxval=200).start()
    while i<len(a["items"]):
        link=bestphoto(i)
        fwrite(i)
        if z=="Y" or z=="y":
            savefile(i,block)
        i=i+1
        pbar.update(i)
    pbar.finish()
    a.setdefault("next_from")
    if a["next_from"]!=None:
        allphotos(a["next_from"],block+1)
def nextuser(pid):
    global f
    name_user=api.users.get(user_ids=pid)
    global namedd
    namedd= name_user[0]["first_name"]+" "+name_user[0]["last_name"]+"/фото"
    name_owner=api.users.get()
    global named
    named = name_owner[0]["first_name"]+" "+name_owner[0]["last_name"]
    try:
        os.makedirs(str(named+"/"+namedd))
    except OSError:
        pass
    f = open(str(named)+"/"+str(namedd)+"/"+str(pid)+'.html', 'w')
    allphotos('0',0)
    f.close()
    time.sleep(0.4)
def saveallphotomain(getapi):
    global  nphoto,nexcept
    nphoto=0
    nexcept=0
    global api,pid
    api =getapi
    global z
    print('загрузить файлы на диск? Y/N')
    z=input()
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
    print(nphoto,nexcept)
def savediaphoto(getapi):
    global  nphoto,nexcept
    iddia=input()
    nextuser(iddia)
