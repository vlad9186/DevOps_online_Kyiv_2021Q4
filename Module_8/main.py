#!/usr/bin/env python3
def main():
    valid_param = validate_param()
    a = valid_param[0]
    b = valid_param[1]
    c = valid_param[2]
    square_print(a, b, c, roots)
    solv_square(a, b, c)
    
def validate_param():
    print('Решаем уравнение a•x²+b•x+c=0')
    for i in 1, 2, 3:
        try:
            a = int(input('Введите значение a: '))
            b = int(input('Введите значение b: '))
            c = int(input('Введите значение c: '))
        except ValueError:
            print("Вводите только цифровые значения!")
            continue
        else:
            return a, b, c

def discriminant(a, b, c):
    d = b ** 2 - 4 * a * c
    print('Дискриминант = ' + str(d))
    return d

def roots(d, a, b, c):
    if d < 0:
        print('Корней нет')
    elif d == 0:
        x = -b / (2 * a)
        print('x = ' + str(x))
        return x
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print('x₁ = ' + str(x1))
        print('x₂ = ' + str(x2))
        return x1, x2

def solv_square(a, b, c) -> roots:
    d = discriminant(a, b, c)
    root = roots(d,a,b,c)
    return root

def square_print(a, b, c, roots):
    print('Решаем уравнение '+str(a)+ 'x²+'+str(b)+ 'x+' +str(c)+ '=0')
    return roots

main()
