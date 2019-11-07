import math


WIDTH = 800
HEIGHT = 800
origin = (WIDTH / 2, HEIGHT / 2)

alien = Actor('rocket2')
alien.pos = 100, 56
alien.velocity = [0, 0]



bullets = []

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    alien.draw()
    for bullet in bullets:
        bullet.draw()
    screen.draw.circle(origin, 30, 'black')

def update():
    for bullet in bullets:
        update_thing(bullet)
    update_thing(alien)

def update_thing(thing):
    # gravity(thing)

    thing.left += thing.velocity[0]
    thing.top += thing.velocity[1]

    if thing.left > WIDTH:
        thing.left = 0
    if thing.top > HEIGHT:
        thing.top  = 0
    if thing.left < 0:
        thing.left = WIDTH
    if thing.top < 0:
        thing.top = HEIGHT

def gravity(thing):
    G = 0.01
    # d = 10000 / dist(thing.pos, origin) ** 2

    dx = thing.pos[0] - origin[0]
    dy = thing.pos[1] - origin[1]

    theta = math.atan(dy/dx)

    thing.velocity[0] -= math.sin(theta) * G
    thing.velocity[1] -= math.cos(theta) * G


def dist(a, b):
    dsq = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    return math.sqrt(dsq)

def on_key_down(key, mod, unicode):
    if key == keys.LEFT:
        alien.angle += 20
    elif key == keys.RIGHT:
        alien.angle -= 20
    elif key == keys.SPACE:
        alien.velocity[0] -= math.sin(math.radians(alien.angle))
        alien.velocity[1] -= math.cos(math.radians(alien.angle))
    elif key == keys.F:
        bullet = Actor('zap')
        bullet.pos = alien.pos
        bullet.velocity = alien.velocity.copy()
        bullet.velocity[0] -= math.sin(math.radians(alien.angle)) * 3
        bullet.velocity[1] -= math.cos(math.radians(alien.angle)) * 3
        bullets.append(bullet)



