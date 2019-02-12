from math import pi, cos, sin

size(360,500)
speed(30)

def draw():
    R = 50
    strokewidth(2)
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
    fill(0)
    a = FRAME % 120 
    if a < 5 or 115 <= a:
        text("Eclipse",-25,200)
    if 55 <= a <65:
        text("Staggard",-25,200)
             