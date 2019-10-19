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
    def move_to(self, x, y):
        self.x = x
        self.y = y
    def set_to_animate(self, x, y, steps):
        dX = (x - self.x)//steps
        dY = (y - self.y)//steps
        for i in range(1, steps):
            self.route.append((self.x + i * dX, self.y + i * dY))

        
    def animate(self):
        if self.route:
            self.x, self.y = self.route.pop(0)
        self.draw()
        

ball = Ball(500, 400, 50)

        

while not done:
    clock.tick(20)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball.set_to_animate(*event.pos, 20)
            
        
    screen.fill(BLACK)
    ball.animate()
    pygame.display.flip()