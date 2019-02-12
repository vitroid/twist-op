from math import pi, cos, sin
size(360,500)

speed(30)

def draw():
    R = 50
    strokewidth(2)
    push()
    translate(180,200)
    stroke(0)
    theta = FRAME*pi/180
    th120 = 120*pi/180
    line(0,0,3*R*cos(0), 3*R*sin(0))
    line(0,0,3*R*cos(0+th120), 3*R*sin(0+th120))
    line(0,0,3*R*cos(0+2*th120), 3*R*sin(0+2*th120))
    fill(255,255,255)
    oval(-R,-R,R*2,R*2)
    line(0,0,3*R*cos(theta), 3*R*sin(theta))
    line(0,0,3*R*cos(theta+th120), 3*R*sin(theta+th120))
    line(0,0,3*R*cos(theta+2*th120), 3*R*sin(theta+2*th120))
    pop()
        
    translate(0,400)
    nofill()
    a = FRAME % 360
    beginpath(0,0)
    for i in range(a):
        lineto(i,-sin(3*i*pi/180)*R)
    moveto(0,0)
    endpath()
    stroke()
    line(0,0,360,0)
        
    fill(0)
    text(u"sin 3θ",155,R*1.5)    

    for i in range(0,a,120):
        text("E",i,20)    
    for i in range(60,a,120):
        text("S",i,0)    
        