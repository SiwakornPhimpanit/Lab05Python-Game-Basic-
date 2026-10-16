import pygame 
from ball import Ball  # นำเข้าคลำส Ball จากไฟล์ ball.py
from rect import Rectangle  # นำเข้าคลำส Rectangle จากไฟล์ rect.py
from dog import Dog  # นำเข้าคลำส Dog จากไฟล์ dog.py
import random

SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
FPS = 60
pygame.init() 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("ลูกบอลเด้ง") 
clock = pygame.time.Clock() 

balls = [] #สร้างลิสต์เก็บลูกบอล
rects = [] #สร้างลิสต์เก็บสี่เหลี่ยม
N = 10
for i in range(N):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, 200)
    vx = random.uniform(-5, 5)
    vy = random.uniform(-5, 5)
    color = (random.randint(0, 255), 
         random.randint(0, 255), 
         random.randint(0, 255))  # สีสุ่ม
    radius = random.randint(10, 30)  # รัศมีสุ่ม
    ball = Ball(x, y, vx, vy, radius, color)  # สร้างลูกบอล
    balls.append(ball) #เก็บลูกบอลในลิสต์

    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, 200)
    vx = random.uniform(-5, 5)
    vy = random.uniform(-5, 5)
    size = random.randint(20, 50)  # ขนาดสุ่ม
    rect = Rectangle(x, y, vx, vy, size, color)  # สร้างสี่เหลี่ยม
    rects.append(rect)  # เก็บสี่เหลี่ยมในลิสต์

all_sprites = pygame.sprite.Group()
dog = Dog(400, 500, 5, "Lab05/images/dog.png")  # สร้างวัตถุ Dog
all_sprites.add(dog)

running = True 
time_steps = 0 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
    screen.fill(BLACK) 

    for ball in balls:
        ball.move()  
        ball.draw(screen) 

    for rect in rects:
        rect.move()  
        rect.draw(screen)

    # อัปเดตการทำงานของหมาย (เรียก def update อัตโนมัติ)
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip() 
    clock.tick(FPS)
pygame.quit() 