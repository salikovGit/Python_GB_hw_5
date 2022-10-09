'''
1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'абвгдейка - это передача' = >" - это передача"
'''


def delete_something(origin_string, arg):
    return ' '.join([word for word in origin_string.split() if arg not in word])


print(delete_something('абвгдейка - это передача', 'абв'))
