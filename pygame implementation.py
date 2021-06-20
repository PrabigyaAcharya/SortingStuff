from sort import Sort
import pygame
import random 

def draw(screen, numbers):
    screen.fill((255, 255, 255))
    width = 400//len(numbers)
    x = 250 - (width * len(numbers))//2
    count = 1
    for number in numbers:
        if count % 2 == 0:
            pygame.draw.rect(screen, (0,255,100), (x, 500-number-40, width, number))
            
        else:
            pygame.draw.rect(screen, (150,0 ,100), (x, 500-number-40, width, number))
        x += width
        count += 1

def callDraw(screen, numbers):
    states = Sort.insertionSort(numbers)
    for number in states:
        print(number)
        draw(screen, number)
        pygame.display.update()
        pygame.time.delay(1)

def generateList():
    finished = True
    num = random.sample(range(1, 100), 80)
    return num

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Sorting Visualiser")

numbers = generateList()
bg = (255, 255, 255)
run = True
screen.fill(bg)
draw(screen, numbers)


while run:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        callDraw(screen, numbers)
    pygame.display.update()

pygame.quit()