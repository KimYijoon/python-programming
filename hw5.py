def read_single_digit(num) :
    if num == 0 :
        print('영', end=' ')
    elif num == 1 :
        print('일', end=' ')
    elif num == 2 :
        print('이', end=' ')
    elif num == 3 :
        print('삼', end=' ')
    elif num == 4 :
        print('사', end=' ')
    elif num == 5 :
        print('오', end=' ')
    elif num == 6 :
        print('육', end=' ')
    elif num == 7 :
        print('칠', end=' ')
    elif num == 8 :
        print('팔', end=' ')
    else :
        print('구', end=' ')

def read_number(N) :
    a = N // 100
    read_single_digit(a)
    b = (N % 100) // 10
    read_single_digit(b)
    c = N % 10
    read_single_digit(c)

n = int(input('세 자리 정수 입력: '))
read_number(n)
