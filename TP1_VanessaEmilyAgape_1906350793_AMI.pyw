import turtle
import random

#Menentukan sisi persegi awal
sisi=turtle.numinput(
    "Rotating Colorful Square and Disks",
    "Please enter the side length of the first square (20-60): ",
    40, minval=20, maxval=60)
#Membuat cursor turtle tidak terlihat
turtle.hideturtle()
#Memindahkan cursor turtle ke koordinat (-200,100)
turtle.penup()
turtle.goto(-200,100)
#Membuat cursor menghadap ke kiri
turtle.setheading(180)
#Mempercepat proses gambar turtle
turtle.speed(0)
#Variable untuk mengubah sudut antar persegi
x=5
turtle.colormode(255)


#Membuat 72 Persegi
#Menggambar 72 persegi yang sudah diwarnai
for i in range(72):
    #Mengenerate angka random untuk pewarnaan random setiap persegi
    for color in range(72):
        r=random.randint(0, 255)
        g=random.randint(0, 255)
        b=random.randint(0, 255)
    turtle.fillcolor(r, g, b)
    turtle.pencolor('black')
    turtle.pendown()
    turtle.begin_fill()
    #Menggambar satu persegi dengan sisi dari variable sisi
    for i in range(3):
        turtle.forward(sisi)
        turtle.right(90)
    turtle.forward(sisi)
    turtle.end_fill()
    #Mengubah letak cursor agar jarak antar persegi 5 derajad
    turtle.setheading(180-x)
    #Mengupdate variable x agar terus bertambah 5 derajad
    x+=5
    #Mengupdate variable sisi agar terus bertambah 2 unit
    sisi+=2

#Menentukan radius lingkaran agar setengah dari persegi terakhir
sisi2=sisi/2
#Membuat cursor menghadap ke kanan
turtle.setheading(0)
#Memindahkan cursor ke koordinat (200, 100)
turtle.penup()
turtle.goto(200,100)
#Variable untuk mengubah sudut antar lingkaran
y=10


#Membuat 36 lingkaran
#Menggambar 36 lingkaran yang sudah diwarnai
for a in range(36):
    for colorr in range(36):
        #Mengenerate angka random untuk pewarnaan random setiap lingkaran
        r=random.randint(0, 255)
        g=random.randint(0, 255)
        b=random.randint(0, 255)
    turtle.fillcolor(r, g, b)
    turtle.pencolor("black")
    turtle.pendown()
    turtle.begin_fill()
    #Menggambar satu lingkaran dengan radius dari variable sisi2
    turtle.circle(sisi2)
    turtle.end_fill()
    #Mengubah letak cursor agar jarak antar lingkaran 10 derajad
    turtle.setheading(0+y)
    #Mengupdate variable y agar terus bertambah 10 derajad
    y+=10
    #Mengupdate variable sisi2 agar terus berkurang 2 unit
    sisi2-=2


#Membuat tulisan
turtle.penup()
turtle.pencolor("blue")
#Memindahkan cursor ke koordinat (0, -200)
turtle.goto(0, -200)
turtle.pendown()
#Membuat cursor menghadap ke kanan
turtle.setheading(0)
#Membuat tulisan yang ada dibawah
turtle.write(
    "There are 72 Squares and 36 Disks",
    False, align="center", font=("Arial", 20, "normal"))
#Turtle akan tertutup hanya ketika diklik
turtle.exitonclick()
