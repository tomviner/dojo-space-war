import math

alien = Actor('rocket2')
alien.pos = 100, 56
alien.velocity = [0, 0]

bullets = []

WIDTH = 800
HEIGHT = 800

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    alien.draw()
    for bullet in bullets:
        bullet.draw()

def update():
    for bullet in bullets:
        update_thing(bullet)
    update_thing(alien)

def update_thing(thing):
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



