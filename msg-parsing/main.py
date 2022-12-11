import extract_msg

# with open('./strangeDate.msg') as file:
#   msg = extract_msg.Message(file)
#   # print(msg)
msg = extract_msg.openMsg('./strangeDate.msg')
print(msg.body)
print(msg.headerDict)
