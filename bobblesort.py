import random
import pygame
import math
import time

width = 500
height = 100
n = 20
colors = []

# Cria alguns números inteiros aleatórios.
numbers = [i for i in range(n)]
random.shuffle(numbers)

# Cria alguns tons de cores que serão
# associados aos números aleatórios.
for c in range(n):
	r = math.floor(c * 255 / n)
	colors.append((r, 0, 0))

pygame.init()
pygame.display.set_caption('Bobble Sort')
screen = pygame.display.set_mode([500, 50])
looping = True

# Desenha os retângulos com cores, ainda
# não ordenados.
screen.fill((255, 255, 255))
i = 0
for x in range(0, 500, 500 // n):
	# colors[numbers[i]] <- Cada número aleatório corresponde a uma cor.
	pygame.draw.rect(screen, colors[numbers[i]], pygame.Rect(x, 0, 500 // n, height))
	i += 1
	pygame.display.flip()

while looping:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			looping = False	
	# Bobble sort.
	for i in range(1, n):
		for j in range(n - i):
			if numbers[j] > numbers[j + 1]:
				aux = numbers[j]
				numbers[j] = numbers[j + 1]
				numbers[j + 1] = aux
			# Redesenha os retângulos.
			i = 0
			for x in range(0, 500, 500 // n):
				pygame.draw.rect(screen, colors[numbers[i]], pygame.Rect(x, 0, 500 // n, height))
				i += 1
				pygame.display.flip()
			time.sleep(0.2)
	looping = False
pygame.display.quit()
pygame.quit()
exit()



