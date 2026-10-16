#ball_sim_v2.py
import pygame 
import matplotlib.pyplot as plt 
from ball import Ball  # นำเข้าคลำส Ball จากไฟล์ ball.py
 
# ก ำหนดค่ำต่ำง ๆ 
SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 600 
BALL_RADIUS = 15 
GRAVITY = 0.1 
BOUNCE_DAMPING = 0.9 
DAMPING_COEFFICIENT = 0.999 
FPS = 60 
FRAME_LIMIT = 600 
 
# สี 
BLACK = (0, 0, 0) 
RED = (255, 0, 0) 
 
# เริ ่มต้น Pygame 
pygame.init() 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("ลูกบอลเด้ง") 
clock = pygame.time.Clock() 

#ball = Ball(400, 100, 3, 0, RED)
#ball2 = Ball(100, 100, -3, 0, RED)

N = 100  # จำนวนลูกบอล
balls = []  # รายกำรเก็บลูกบอล
for i in range(N):
    #x, y, vx, vy, color
    ball = Ball(100 + i*20, 100, 3 * (-1)**i, 0, RED)  # สร้างลูกบอลแต่ละลูก
    balls.append(ball)
positions = []  # เก็บต ำแหน่งเพื่อพล็อตกรำฟ 

# Simulation loop 
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
    #draw_ball(ball) 
    positions.append((ball.x, ball.y))  # บันทึกต ำแหน่ง 
    
    pygame.display.flip() 
    clock.tick(FPS) 
    time_steps += 1 
    if time_steps > FRAME_LIMIT:  # จ ำกัดจ ำนวนเฟรม 
        running = False 
 
pygame.quit() 
 