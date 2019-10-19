import pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 1000, 800
BLACK = 0, 0, 0

screen = pygame.display.set_mode(SIZE)
done = False

clock = pygame.time.Clock()

class Ball():
    def __init__(self, x, y, radius, color = (255,0,0)):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.route = []
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    def move(self):
        self.x += 1
        self.draw()

    def set_to_animate(self, x, y, time, FPS):
        steps = int(time*FPS)
        if self.route:
            X, Y = self.route[-1]
        else:
            X, Y = self.x, self.y
        dX = (x - X)//steps
        dY = (y - Y)//steps
        for i in range(1, steps):
            self.route.append((X + i * dX, Y + i * dY))
  
    def animate(self):
        if self.route:
            self.x, self.y = self.route.pop(0)
        self.draw()
        
ball = Ball(500, 400, 50)
FPS = 20
while not done:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball.set_to_animate(*event.pos, 0.2, 20)
            
        
    screen.fill(BLACK)
    ball.animate()
    pygame.display.flip()