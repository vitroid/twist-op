from math import pi, cos, sin

size(360,500)
speed(30)

def draw():
    colormode(HSB)
    strokewidth(2)
    R = 50
    push()
    translate(180,200)
    a = FRAME % 360
    for i in range(a):
        theta = i*pi/180
        phase = i % 120
        if phase < 60:
            hue = 0
        else:
            hue = 2./3.
        sat = abs(sin(phase*3*pi/180))
        stroke(hue,sat,100)
        line(2*R*cos(theta), 2*R*sin(theta), 3*R*cos(theta), 3*R*sin(theta))
    fill(0,0,1)
    fontsize(36)
    for i in range(30,360,120):
        text("L",R*2.5*cos(i*pi/180)-10,R*2.5*sin(i*pi/180)+15)
    for i in range(90,360,120):
        text("R",R*2.5*cos(i*pi/180)-10,R*2.5*sin(i*pi/180)+15)
        
    stroke(0)
    theta = FRAME*pi/180
    th120 = 120*pi/180
    line(0,0,3*R*cos(0), 3*R*sin(0))
    line(0,0,3*R*cos(0+th120), 3*R*sin(0+th120))
    line(0,0,3*R*cos(0+2*th120), 3*R*sin(0+2*th120))
    fill(255,0,255)
    oval(-R,-R,R*2,R*2)
    line(0,0,3*R*cos(theta), 3*R*sin(theta))
    line(0,0,3*R*cos(theta+th120), 3*R*sin(theta+th120))
    line(0,0,3*R*cos(theta+2*th120), 3*R*sin(theta+2*th120))

    stroke(0)
    pop()
    translate(0,400)
    fontsize(24)
    for i in range(a):
        theta = i*pi/180
        phase = i % 120
        if phase < 60:
            hue = 0
        else:
            hue = 2./3.
        sat = abs(sin(phase*3*pi/180))
        stroke(hue,sat,100)
        line(i,0,i,-R*sin(theta*3))
    fill(0,0,1)
    for i in range(30,360,120):
        text("L",i-6.6,-10)
    for i in range(90,360,120):
        text("R",i-6.6,34)
    nofill()
    stroke(0)
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
    
