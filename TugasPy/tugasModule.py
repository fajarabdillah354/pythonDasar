import pygame#module yang dipakai dalam program

# Inisialisasi pygame
pygame.init()

# Buat sebuah window dengan ukuran 640x480 px
screen = pygame.display.set_mode((640, 480))

# Set judul window
pygame.display.set_caption("FajarAbdillahAhmad")

# Buat sebuah objek bola dengan posisi awal (100, 100)
ball = pygame.Rect(100, 100, 20, 20)

# Buat sebuah kecepatan bola dengan arah ke kanan (2 px/frame)
speed = [2, 0]

# Game loop
running = True
while running:
  # Periksa event yang terjadi
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Update posisi bola
  ball.x += speed[0]
  ball.y += speed[1]

  # Periksa apakah bola menyentuh batas window
  if ball.left < 0 or ball.right > 640:
    speed[0] = -speed[0]
  if ball.top < 0 or ball.bottom > 480:
    speed[1] = -speed[1]

  # Bersihkan layar
  screen.fill((0, 0, 0))

  # Gambar bola di layar
  pygame.draw.rect(screen, (255, 255, 255), ball)

  # Tampilkan layar
  pygame.display.flip()

# Bersihkan pygame
pygame.quit()
