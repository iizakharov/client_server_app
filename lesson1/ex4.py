# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
# представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).


a = 'разработка'
b = 'администрирование'
c = 'protocol'
d = 'standard'

a_enc = a.encode('utf-8')
print(a_enc)
a_dec = a_enc.decode('utf-8')
print(a_dec)
print()

b_enc = b.encode('utf-8')
print(b_enc)
b_dec = b_enc.decode('utf-8')
print(b_dec)
print()

c_enc = c.encode('utf-8')
print(c_enc)
c_dec = c_enc.decode('utf-8')
print(c_dec)
print()

d_enc = d.encode('utf-8')
print(d_enc)
d_dec = d_enc.decode('utf-8')
print(d_dec)
print()