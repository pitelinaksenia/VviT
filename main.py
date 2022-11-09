'''3
sides=[3,2,4,7,5,12,11,13,15,16,14,14]

sides=sorted(sides,reverse=True)

smax=0
for i in range(len(sides)):
    for j in range(i+1,len(sides)):
        for k in range(j+1,len(sides)):
            a=sides[i]
            b=sides[j]
            c=sides[k]
            if a+b>c and a+c>b and b+c>a:
                p=(a+b+c)/2
                s=(p*(p-a)*(p-b)*(p-c))**(1/2)
                if s>smax:
                    smax=s
print("Максимальная площадь треугольника",smax)
'''

import sys
print("Введите коэффициент а:")
a=int(input())
print("Введите коэффициент b:")
b=int(input())
print("Введите коэффициент с:")
c=int(input())

if a==0:
    print("Не является квадратным уравнением")
    sys.exit()
d=b**2-(4*a*c)

if d<0:
    print('Нет корней')
elif d==0:
    x0=-(b)/(2*a)
    print ('1 корень: ',x0)
elif d>0:
    x1=(-b+(d**(1/2)))/(2*a)
    x2 = (-b - (d ** (1 / 2))) / (2 * a)
    print("2 корня: x1=",x1, "x2=", x2)
