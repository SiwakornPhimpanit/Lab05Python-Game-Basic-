import pygame 
import math
 
# เริ ่มต้น Pygame 
pygame.init() 
# ก ำหนดขนำดหน้ำจอ 
WIDTH, HEIGHT = 800, 600 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
# ตั ้งชื่อหน้ำต่ำง 
pygame.display.set_caption("เริ ่มต้นใช้งำน Pygame") 
# สีพื ้นหลัง 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
BLUE = (0, 0, 255) 
GREEN = (0, 255, 0) 
# ก ำหนดต ำแหน่งและขนำด 
circle_x, circle_y = WIDTH//2, HEIGHT//2  # ต ำแหน่งของวงกลม 
circle_radius = HEIGHT//2  # รัศมีของวงกลม

a = 2*math.sqrt(circle_radius**2/2)  # คำนวณความสูงของสามเหลี่ยมด้านเท่า

rect_x, rect_y = circle_x - a//2, circle_y - a//2  # ต ำแหน่งของสี่เหลี่ยม 
rect_width, rect_height = a, a  # ขนำดของสี่เหลี่ยม 

line_start1 = (rect_x, rect_y)  # จุดเริ ่มต้นของเส้น 
line_end1 = (rect_x+a, rect_y+a)  # จุดสิ ้นสุดของเส้น 
line_start2 = (rect_x, rect_y+a)  # จุดเริ ่มต้นของเส้น 
line_end2 = (rect_x+a, rect_y)  # จุดสิ ้นสุดของเส้น 
line_width = 20  # ควำมหนำของเส้น 


# วำดหน้ำจอพื ้นฐำน 
running = True 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
    # เติมสีพื ้นหลัง 
    screen.fill(BLACK) 

    pygame.draw.circle(screen, GREEN, (circle_x, circle_y), circle_radius) 
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height)) 
    pygame.draw.line(screen, RED, line_start1, line_end1, line_width) 
    pygame.draw.line(screen, RED, line_start2, line_end2, line_width) 
    # อัปเดตหน้ำจอ 
    pygame.display.flip() 
 
pygame.quit()