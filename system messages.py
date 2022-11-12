import aminofix
client = aminofix.Client()
client.login(email=' ', password=' ')

print("\nLOGGING IN...")
n=input("\nCHAT LINK:")

fok=client.get_from_code(n)
id=client.get_from_code(n).objectId
cid=fok.path[1:fok.path.index("/")]
print(cid)
client.join_community(cid)
subclient=aminofix.SubClient(comId=cid,profile=client.profile)
print("\nJOINING AMINO....")
subclient.join_chat(chatId=id)
while True:
     mssg=input ("BOT MESSAGE:-")
     subclient.send_message(chatId=id,message=mssg,messageType=109)
     print("\nMESSAGE SENT!")