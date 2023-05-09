from vpython import *

bola = sphere(pos=vector(-5, 1, 0), radius=0.5, color=color.blue, velocity=vector(10, 0, 0))
bola2 = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.white, velocity=vector(10, 0, 0))
muro = box(pos=vector(5, 0, 0), color=color.red, size=vector(0.5, 10, 10))
dt = 0.01
t = 0
while t < 3:
    rate(100)
    bola.pos.x = bola.pos.x + (bola.velocity.x * dt)
    if bola.pos.x >= muro.pos.x:
        bola.velocity.x = -bola.velocity.x
    t = t + dt
print("A BOLA SE DESLOCOU ", bola.pos.x - (-5), " METROS")
print("A BOLA SE DESLOCOU ", t, " SEGUNDOS")
