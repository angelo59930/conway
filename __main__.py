#!/usr/bin/env python3
import pygame
import numpy as np
import time
''' 
juego de la vida de conway
  -Una célula muerta con exactamente 3 células vecinas vivas "nace" 
  -Una célula viva con 2 o 3 células vecinas vivas sigue viva, en otro caso muere 
'''

def main():
    display()


def display():
    # tamaño de pantalla
    width, height = 600, 600
    screen = pygame.display.set_mode((width, height))
    # coloreado de la pnatalla
    bg = 25, 25, 25
    screen.fill(bg)

    cX = 50
    cY = 50
    sizeX = int(width/cX)
    sizeY = int(height/cY)

    # matriz con el estado de las celdas 1=vivo, 0=muerto
    arrayState = np.zeros((cX, cY))


    pause = False


    while True:
        newArrayState = np.copy(arrayState)
        screen.fill(bg)

        time.sleep(0.1)

        # DETECCION DEL BOTON PARA CERRAR
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            mouseClick = pygame.mouse.get_pressed()

            if sum(mouseClick) > 0:
                posX, posY = pygame.mouse.get_pos()
                celX, celY = int(np.floor(posX/sizeX)), int(np.floor(posY/sizeY))
                newArrayState[celX, celY] = 1
     
            if event.type == pygame.KEYDOWN:
                pause = not pause

        
        for y in range(0, cX):
            for x in range(0, cY):
                if pause:
                    # calculo de numero de vecinos
                    numberNeighbor = arrayState[(x-1) % cX, (y-1) % cY] +\
                      arrayState[(x) % cX, (y-1) % cY] +\
                      arrayState[(x+1) % cX, (y-1) % cY] +\
                      arrayState[(x-1) % cX, (y) % cY] +\
                      arrayState[(x+1) % cX, (y) % cY] +\
                      arrayState[(x-1) % cX, (y+1) % cY] +\
                      arrayState[(x) % cX, (y+1) % cY] +\
                      arrayState[(x+1) % cX, (y+1) % cY]
                    #-Una célula muerta con exactamente 3 células vecinas vivas "nace"
                    if arrayState[x, y] == 0 and numberNeighbor == 3:
                        newArrayState[x, y] = 1

                    #-Una célula viva con 2 o 3 células vecinas vivas sigue viva, en otro caso muere
                    elif arrayState[x, y] == 1 and (numberNeighbor < 2 or numberNeighbor > 3):
                        newArrayState[x, y] = 0

                poly = [((x) * sizeX, y * sizeY),
                      ((x+1) * sizeX, y * sizeY),
                      ((x+1) * sizeX, (y+1) * sizeY),
                      ((x) * sizeX, (y+1) * sizeY)]

                if newArrayState[x, y] == 0:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
                else:
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

                arrayState = np.copy(newArrayState)

        # actualizacion del juego
        pygame.display.flip()


if __name__ == "__main__":
    main()
