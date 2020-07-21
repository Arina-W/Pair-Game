import pygame
import game_config as gc
from animal import Animal
from pygame import display, event, image
from time import sleep

def find_index(x,y):
    row = y // gc.imgsize
    col = x // gc.imgsize
    index = row * gc.numtiles + col
    return index

pygame.init()

display.set_caption('First Game')
screen = display.set_mode((512,512))
matched = image.load('other_assets/matched.png')
# screen.blit(matched, (0,0))
# display.flip()
running = True
tiles = [Animal(i) for i in range(0,gc.tilestotal)]
currentimg = []

while running:
    current_events = event.get()
    for e in current_events:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x, mouse_y)
            if index not in currentimg:
                currentimg.append(index)
            if len(currentimg)>2:
                currentimg = currentimg[1:]

    screen.fill((255,255,255))

    totalskipped = 0

    for i, tile in enumerate(tiles):
        image_i = tile.image if i in currentimg else tile.box
        if not tile.skip:
            screen.blit(image_i, (tile.col * gc.imgsize +gc.margin, tile.row*gc.imgsize+gc.margin))
        else:
            totalskipped += 1

    display.flip()

    if len(currentimg) == 2:
        i1, i2 = currentimg
        if tiles[i1].name == tiles[i2].name:
            tiles[i1].skip = True
            tiles[i2].skip = True
            sleep(0.4)
            screen.blit(matched, (0,0))
            display.flip()
            sleep(0.4)
            currentimg = []

    if totalskipped == len(tiles):
        running = False
        
        
print("THE END!")
