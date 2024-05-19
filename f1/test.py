print('test1a')
"""
EX8: Se da variabila num = 12
a. Verifica daca num citit este pozitiv.
b. verifica daca num este mai mare decat 5.
verifica daca num este mai mic decat 25.
c. verifica daca num este intre 0 si 20.
"""
num = 12
print(num>0)
print(num>5)
print(num<25)
print(num>0 and num<25)
if num > 0:
 print('Numarul este pozitiv')
else:
 print('Numarul este negativ')
if num > 5:
 print('numarul este mai mare decat 5')
else:
 print('nuamrul este mai mic decat 5')
if num < 25:
 print('numarul este mai mic decat 25')
else:
 print('numarul este mai mare decat 25')
if num > 0 and num < 20:
 print('numarul este intre 0 si 20')
else:
 print('numarul nu se afla in intervalul dat')