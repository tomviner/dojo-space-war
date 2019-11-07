alien = Actor('rocket2')
alien.pos = 100, 56
alien.velocity = 2, 3

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
        alien.right = 0
    if alien.top > HEIGHT:
        alien.bottom = 0