import math
a = int(input("Nhap he so a ---> "))
b = int(input("Nhap he so b ---> "))
c = int(input("Nhap he so c ---> "))
delta = b^2 - 4*a*c
if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    x = -b/2*a
    print("Phuong trinh co nghiem kep",x)
else:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print("Phuong trinh co 2 nghiem phan biet")
    print(x1)
    print(x2)