import extract_msg

msg = extract_msg.openMsg('./strangeDate.msg')
print(msg.body)
print(msg.headerDict)
