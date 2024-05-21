import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(0)
raagn=('red','orange','blue','green','yellow','light green','violet','indigo','light blue','dark green', 'pink','light pink1','dark red',''
'light blue1','brown','dark orange2')

def d(a,b):
t.up()
t.goto(a,b)
t.pendown()
d(-200,-150)

x=0

for i in range(500):
t.color(raagn[i%16])
t.pencolor()
t.circle(x)
t.fd(1)
x=x+0.5
