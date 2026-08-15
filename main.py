import pygame as pg
import time

pg.init()
width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Pisek")

CELL_SIZE = 8
cols = width // CELL_SIZE
rows = height // CELL_SIZE

color_sand = (235, 198, 52)

grid = [[0 for _ in range(cols)] for _ in range(rows)]

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    mouseX, mouseY = pg.mouse.get_pos()
    isPressed = pg.mouse.get_pressed()[0]


    screen.fill((30,30,30))
    if isPressed:
        mouseX //= CELL_SIZE
        mouseY //= CELL_SIZE

        if mouseX >= 0 and mouseY >= 0 and mouseX < cols and mouseY < rows:
            grid[mouseY][mouseX] = 1

    for row in range(rows-1, -1, -1):
        for col in range(len(grid[row])):
            cell = grid[row][col]

            # sand
            if cell == 1:
                # below empty
                if row + 1 < rows and grid[row+1][col] == 0:
                    grid[row][col] = 0
                    grid[row+1][col] = 1
                    pg.draw.rect(screen, color_sand, (col*8, row*8, CELL_SIZE, CELL_SIZE))
                # right    
                elif row + 1 < rows and col + 1 < cols and grid[row+1][col+1] == 0:
                    grid[row][col] = 0
                    grid[row+1][col+1] = 1
                    pg.draw.rect(screen, color_sand, (col*8, row*8, CELL_SIZE, CELL_SIZE))
                # left
                elif row + 1 < rows and col - 1 >= 0 and grid[row+1][col-1] == 0:
                    grid[row][col] = 0
                    grid[row+1][col-1] = 1
                    pg.draw.rect(screen, color_sand, (col*8, row*8, CELL_SIZE, CELL_SIZE))

                else: pg.draw.rect(screen, color_sand, (col*8, row*8, CELL_SIZE, CELL_SIZE))
                    
    pg.display.flip()
    time.sleep(0.025)
pg.quit()