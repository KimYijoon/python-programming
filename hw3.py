def get_fixed_price(p) :
    global d
    res = int(int(p) * 100 / (100 - int(d)))
    return res
  
d = input('할인율은? ')  
A = int(input('A 상품의 할인된 가격은? '))
B = int(input('B 상품의 할인된 가격은? '))
ap = get_fixed_price(A)
print('A 상품의 정가는', ap, '원')
bp = get_fixed_price(B)
print('B 상품의 정가는', bp, '원')
