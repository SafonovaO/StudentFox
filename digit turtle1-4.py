import turtle
from math import sin

t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen", "yellow")
t.shapesize(2)
t.speed(10)


def digit_one(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
   
    t.penup()
    t.forward(length/2)
    t.pendown()
    t.left(90)
    t.forward(length)
    t.left(90+45)
    t.forward(length*sin(45*3.141592/180))
    t.penup()
    t.left(45)
    t.forward(length/2)
    t.left(90)

def digit_two(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
 
    t.penup()
    t.forward(length/2)
    t.pendown()
    t.backward(length/2)
    t.left(45)
    t.forward(length*sin(45*3.141592/180))
    t.left(45)
    t.forward(length/2)
    t.left(90)
    t.forward(length/2)
    t.left(90)
    t.penup()
    t.forward(length)    
    t.left(90)
 
def digit_three(length):
    """ Рисует цифру с высотой length
            слева от направления черепашки
            контракт (договорённость):
                черепаха возвращается в исходную точку
                и имеет исходную ориентацию
                перо оказывается поднятым по окончании функции
        """
    t.pendown()
    t.left(45)
    t.forward(length*sin(45*3.141592/180))
    t.left(45+90)
    t.forward(length/2)
    t.right(90+45)
    t.forward(length*sin(45*3.141592/180)) 
    t.left(90+45)
    t.forward(length/2)
    t.left(90)
    t.penup()
    t.forward(length)    
    t.left(90)  
        
def digit_four(length):
    """ Рисует цифру с высотой length
            слева от направления черепашки
            контракт (договорённость):
                черепаха возвращается в исходную точку
                и имеет исходную ориентацию
                перо оказывается поднятым по окончании функции
        """
    t.penup()
    t.forward(length/2)
    t.pendown()
    t.left(90) 
    t.forward(length)
    t.backward(length/2)
    t.left(90)
    t.forward(length/2)
    t.right(90)
    t.forward(length/2) 
    t.penup()
    t.backward(length)    
    t.right(90)  
                
def sravn():# выбор цифры для рисования
        t.penup()
        
        t.forward(length)
        if d==0:
                digit_zero(length)
        elif d==1:
                digit_one(length)
        elif d==2:
                digit_two(length)
        elif d==3:
                digit_three(length)
        elif d==4:
                digit_four(length)
        elif d==5:
                digit_five(length)
                
    
length=50

#подсчет разрядов в числе
da=0
n = int(input())
da=len(str(n))
d=n
#выделение цифры и ее рисование
for i in range(da-1,-1,-1):
    d //= 10**i 
    sravn()        
    n=n % 10**i
    d=n
    
    
#t.left(30)
#t.right(30)
#t.forward(200)
#t.backward(200)
#t.penup()
#t.pendown()
#t.begin_fill()
#t.end_fill()