# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования
# в последовательность кодов (не используя методы encode и decode) и определить тип,
# содержимое и длину соответствующих переменных.

a = b'class'
b = b'function'
c = b'method'

print(a)  # b'class'
print(type(a))  # <class 'bytes'>
print(len(a))  # 5
print(b)  # b'function'
print(type(b))  # <class 'bytes'>
print(len(b))  # 8
print(c)  # b'method'
print(type(c))  # <class 'bytes'>
print(len(c))  # 6

