print(ord('は'))
print(ord('巻'))
print(ord('卷'))
print(chr(21368))
print('\u4e2d\u6587')
print(ord('中'))

print('中文的'.encode('utf-8'))
print(b'\xe4\xb8\xad'.decode('utf-8'))

print(len('中文'))
print(len('中文'.encode('utf-8')))

print('%3d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

a = 1
b = 1
print(f"{a}+{b}+a")


# ex
s1 = 72
s2 = 85
r = (s2/s1 - 1)*100
print('小明成绩提高%.1f%%' % r)
