import math

alien = Actor('rocket2')
alien.pos = 100, 56
alien.velocity = [-2, -3]

WIDTH = 800
HEIGHT = 800

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    alien.draw()

def update():
    alien.left += alien.velocity[0]
    alien.top += alien.velocity[1]
    if alien.left > WIDTH:
        alien.left = 0
    if alien.top > HEIGHT:
        alien.top  = 0
    if alien.left < 0:
        alien.left = WIDTH
    if alien.top < 0:
        alien.top = HEIGHT

def on_key_down(key, mod, unicode):
    if key == keys.LEFT:
        alien.angle += 20
    elif key == keys.RIGHT:
        alien.angle -= 20
    elif key == keys.SPACE:
        alien.velocity[1] += math.sin(alien.angle) * 3
        alien.velocity[0] += math.cos(alien.angle) * 3

