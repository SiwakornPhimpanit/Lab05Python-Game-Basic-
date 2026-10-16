#rect.py
import pygame

# ก ำหนดค่ำต่ำง ๆ 
SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 600 
GRAVITY = 0.1 
BOUNCE_DAMPING = 0.9 
DAMPING_COEFFICIENT = 0.999 

class Rectangle:
    def __init__(self, x, y, vx, vy, size, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.size = size
        self.color = color

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY
        self.vx *= DAMPING_COEFFICIENT
        self.vy *= DAMPING_COEFFICIENT

        # กำรชนกับขอบจอ 
        if self.x - self.size <= 0 or self.x + self.size >= SCREEN_WIDTH:
            self.vx = -self.vx * BOUNCE_DAMPING
        if self.y + self.size >= SCREEN_HEIGHT:
            self.vy = -self.vy * BOUNCE_DAMPING
            self.y = SCREEN_HEIGHT - self.size

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (int(self.x), int(self.y), 
                         self.size, self.size))
