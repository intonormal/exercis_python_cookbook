# 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？


x,y=(4,5)
print(x,y)

name, shares, price, date = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
print(name, shares, price, date)

name, shares, price, (year, mon, day) = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
print(year,mon,day)

a, b, c, d, e = 'hello'
print(a, b, c, d, e)

_, shares, price, _ = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
print(shares, price)
