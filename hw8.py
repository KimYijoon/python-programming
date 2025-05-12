def buy(lst) :
    while True :
      print('[구입]')
      item = input('상품명? ')
      if item == '' :
        return False
      else :
        n = int(input('수량은? '))
        lst[item] = n
        print(f'장바구니에 {item} {n}개가 담겼습니다.')
        print()

def show(lst) :
    print(f'\n>>> 장바구니 보기: {lst}')

def find(lst) :
    print('\n[검색]')
    g = input('장바구니에서 확인하고자 하는 상품은? ')
    if g in lst :
        print(f'{g}은(는) {lst[g]}개 담겨 있습니다.')
    else :
        print(f'장바구니에 {g}은(는) 없습니다.')

shopping_bag = {}
while True :
    if buy(shopping_bag) == False :
        break
show(shopping_bag)
find(shopping_bag)
