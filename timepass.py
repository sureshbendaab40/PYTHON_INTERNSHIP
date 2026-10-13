# from turtle import *
# from colorsys import *

# tracer(50)
# bgcolor("black")
# pensize(2)

# h = 0

# for i in range(350):
#     h += 0.0021
#     c = hsv_to_rgb(h, 1, 1)
#     color(c)

#     goto(0, 0)
#     circle(180 - i / 4, 90)
#     circle(40)
#     circle(180 - i / 4, -60)
#     right(50)

# done()










# from turtle import *
# from colorsys import *

# tracer(50)
# bgcolor("black")
# pensize(2)

# h = 0

# for i in range(350):
#     h += 0.0028

#     # Attractive neon colors
#     c = hsv_to_rgb(h, 0.9, 1)
#     color(c)

#     goto(0, 0)
#     circle(180 - i / 4, 90)
#     circle(40)
#     circle(180 - i / 4, -60)
#     right(50)

# done()















# # import turtle

# # t = turtle.Turtle()
# # t.speed(0)
# # t.width(2)

# # turtle.bgcolor("black")

# # colors = ["red", "magenta", "blue", "cyan", "purple", "pink"]

# # for i in range(72):
# #     t.color(colors[i % len(colors)])
    
# #     for j in range(2):
# #         t.circle(100, 60)
# #         t.left(120)
    
# #     t.left(5)

# # turtle.done()









# import turtle

# t = turtle.Turtle()
# t.speed(0)
# t.width(3)

# turtle.bgcolor("black")

# colors = ["cyan", "blue", "purple", "magenta", "pink"]

# for i in range(300):
#     t.color(colors[i % len(colors)])
#     t.forward(i * 1.5)
#     t.right(91)

# turtle.done()


# import turtle

# t = turtle.Turtle()
# t.speed(0)
# t.width(2)

# turtle.bgcolor("black")

# colors = ["cyan", "deepskyblue", "blue",
#           "purple", "magenta", "hotpink"]

# for i in range(120):
#     t.color(colors[i % len(colors)])
    
#     for j in range(5):
#         t.forward(200)
#         t.right(144)
    
#     t.right(3)

# turtle.done()


# import turtle
# import time
# import random

# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("Madam Ji Sorry ❤️")
# screen.setup(900, 600)

# # Main turtle
# t = turtle.Turtle()
# t.hideturtle()
# t.penup()

# # Colors
# colors = [
#     "red",
#     "hotpink",
#     "magenta",
#     "purple",
#     "cyan",
#     "deepskyblue"
# ]

# # Moving stars
# stars = []

# for i in range(35):
#     star = turtle.Turtle()
#     star.shape("circle")
#     star.shapesize(0.15)
#     star.color(random.choice(colors))
#     star.penup()
#     star.goto(
#         random.randint(-430, 430),
#         random.randint(-280, 280)
#     )
#     stars.append(star)

# # Animate stars
# def move_stars():
#     for star in stars:
#         star.goto(
#             star.xcor() + random.randint(-3, 3),
#             star.ycor() + random.randint(-2, 2)
#         )

#         if star.xcor() > 450:
#             star.setx(-450)

#         if star.xcor() < -450:
#             star.setx(450)

# # Text
# text = "MADAM JI SORRY"

# # Starting position
# x = -300
# y = -40

# # Write letters one by one
# for i, letter in enumerate(text):

#     # Move stars while text appears
#     for j in range(8):
#         move_stars()
#         screen.update()
#         time.sleep(0.03)

#     t.goto(x, y)

#     # Different color for every letter
#     t.color(colors[i % len(colors)])

#     t.write(
#         letter,
#         align="left",
#         font=("Arial", 42, "bold")
#     )

#     x += 45

# # Heart underneath
# t.goto(0, -130)
# t.color("red")
# t.write("♥", align="center", font=("Arial", 55, "bold"))

# # Final message
# t.goto(0, -200)
# t.color("white")
# t.write(
#     "Please forgive me 😅",
#     align="center",
#     font=("Arial", 20, "normal")
# )

# screen.update()
# turtle.done()



# import pygame
# import random
# import math

# pygame.init()

# # Screen
# WIDTH = 1000
# HEIGHT = 650

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("MADAM JI SORRY ❤️")

# clock = pygame.time.Clock()

# # Fonts
# big_font = pygame.font.Font(None, 90)
# small_font = pygame.font.Font(None, 35)

# # Colors
# COLORS = [
#     (255, 50, 50),
#     (255, 100, 200),
#     (100, 200, 255),
#     (100, 255, 150),
#     (255, 220, 50),
#     (200, 100, 255)
# ]


# # -------------------------
# # Firework Particle
# # -------------------------

# class Particle:

#     def __init__(self, x, y, color):

#         self.x = x
#         self.y = y

#         angle = random.uniform(0, math.pi * 2)
#         speed = random.uniform(2, 7)

#         self.vx = math.cos(angle) * speed
#         self.vy = math.sin(angle) * speed

#         self.color = color
#         self.life = random.randint(40, 80)

#     def update(self):

#         self.x += self.vx
#         self.y += self.vy

#         # Gravity
#         self.vy += 0.08

#         self.life -= 1

#     def draw(self):

#         if self.life > 0:

#             radius = max(1, self.life // 15)

#             pygame.draw.circle(
#                 screen,
#                 self.color,
#                 (int(self.x), int(self.y)),
#                 radius
#             )


# # -------------------------
# # Firework
# # -------------------------

# class Firework:

#     def __init__(self):

#         self.x = random.randint(100, WIDTH - 100)
#         self.y = HEIGHT

#         self.target_y = random.randint(100, 350)

#         self.speed = random.uniform(7, 10)

#         self.color = random.choice(COLORS)

#         self.exploded = False

#         self.particles = []

#     def update(self):

#         if not self.exploded:

#             self.y -= self.speed

#             if self.y <= self.target_y:

#                 self.explode()

#         else:

#             for particle in self.particles:
#                 particle.update()

#             self.particles = [
#                 p for p in self.particles
#                 if p.life > 0
#             ]

#     def explode(self):

#         self.exploded = True

#         for i in range(120):

#             self.particles.append(
#                 Particle(
#                     self.x,
#                     self.y,
#                     self.color
#                 )
#             )

#     def draw(self):

#         if not self.exploded:

#             pygame.draw.circle(
#                 screen,
#                 self.color,
#                 (int(self.x), int(self.y)),
#                 4
#             )

#         else:

#             for particle in self.particles:
#                 particle.draw()


# # -------------------------
# # Variables
# # -------------------------

# fireworks = []

# running = True

# timer = 0


# # -------------------------
# # Main Loop
# # -------------------------

# while running:

#     clock.tick(60)

#     # Events
#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:
#             running = False

#         # Mouse click creates firework
#         if event.type == pygame.MOUSEBUTTONDOWN:

#             x, y = pygame.mouse.get_pos()

#             fw = Firework()

#             fw.x = x
#             fw.target_y = y

#             fireworks.append(fw)

#     # Background
#     screen.fill((5, 5, 20))

#     # Automatically create fireworks
#     timer += 1

#     if timer > 45:

#         fireworks.append(Firework())

#         timer = 0

#     # Update and draw fireworks
#     for fw in fireworks:

#         fw.update()
#         fw.draw()

#     # Remove finished fireworks
#     fireworks = [
#         fw for fw in fireworks
#         if not fw.exploded or len(fw.particles) > 0
#     ]

#     # -------------------------
#     # Text
#     # -------------------------

#     text1 = big_font.render(
#         "MADAM JI",
#         True,
#         (255, 100, 200)
#     )

#     text2 = big_font.render(
#         "SORRY ❤️",
#         True,
#         (255, 80, 80)
#     )

#     screen.blit(
#         text1,
#         (
#             WIDTH // 2 - text1.get_width() // 2,
#             HEIGHT - 180
#         )
#     )

#     screen.blit(
#         text2,
#         (
#             WIDTH // 2 - text2.get_width() // 2,
#             HEIGHT - 100
#         )
#     )

#     # Small instruction
#     instruction = small_font.render(
#         "Click anywhere for fireworks!",
#         True,
#         (220, 220, 220)
#     )

#     screen.blit(
#         instruction,
#         (
#             WIDTH // 2 - instruction.get_width() // 2,
#             20
#         )
#     )

#     pygame.display.flip()


# pygame.quit()
# import pygame
# import random

# pygame.init()

# # Screen
# WIDTH = 1000
# HEIGHT = 650

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Matrix Rain")

# clock = pygame.time.Clock()

# # Font
# font = pygame.font.Font(None, 22)
# big_font = pygame.font.Font(None, 80)

# # Matrix characters
# characters = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&@"

# # Columns
# font_size = 22
# columns = WIDTH // font_size

# drops = []

# for i in range(columns):
#     drops.append(random.randint(-HEIGHT, 0))


# # Main loop
# running = True

# while running:

#     clock.tick(60)

#     # Events
#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:
#             running = False

#     # Slight transparent black overlay
#     overlay = pygame.Surface((WIDTH, HEIGHT))
#     overlay.set_alpha(35)
#     overlay.fill((0, 0, 0))

#     screen.blit(overlay, (0, 0))

#     # Matrix rain
#     for i in range(columns):

#         x = i * font_size
#         y = drops[i]

#         # Random character
#         char = random.choice(characters)

#         # Bright green head
#         color = (120, 255, 120)

#         text = font.render(char, True, color)

#         screen.blit(text, (x, y))

#         # Move down
#         drops[i] += font_size

#         # Restart column randomly
#         if drops[i] > HEIGHT and random.random() > 0.975:
#             drops[i] = random.randint(-300, 0)

#     # -------------------------
#     # Center Message
#     # -------------------------

#     message = big_font.render(
#         "MADAM JI SORRY",
#         True,
#         (0, 255, 80)
#     )

#     # Black box behind text
#     box = pygame.Rect(
#         WIDTH // 2 - message.get_width() // 2 - 25,
#         HEIGHT // 2 - 55,
#         message.get_width() + 50,
#         message.get_height() + 30
#     )

#     pygame.draw.rect(
#         screen,
#         (0, 0, 0),
#         box
#     )

#     pygame.draw.rect(
#         screen,
#         (0, 255, 80),
#         box,
#         2
#     )

#     screen.blit(
#         message,
#         (
#             WIDTH // 2 - message.get_width() // 2,
#             HEIGHT // 2 - 40
#         )
#     )

#     # Instruction
#     instruction = font.render(
#         "SYSTEM MESSAGE : PLEASE FORGIVE ME...",
#         True,
#         (0, 200, 70)
#     )

#     screen.blit(
#         instruction,
#         (
#             WIDTH // 2 - instruction.get_width() // 2,
#             HEIGHT // 2 + 50
#         )
#     )

#     pygame.display.flip()


# pygame.quit()