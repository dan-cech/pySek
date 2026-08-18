import pygame as pg
import time
import random

pg.init()
width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("PySek")

CELL_SIZE = 8
cols = width // CELL_SIZE
rows = height // CELL_SIZE

# material colors
color_sand = (235, 198, 52)
color_water = (30, 30, 240)
color_stone = (80, 80, 80)

# initializng the grid
grid = [[0 for _ in range(cols)] for _ in range(rows)]
moved = [[False for _ in range(cols)] for _ in range(rows)]

materialList = ["sand", "stone", "water"]
material = "sand"

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    mouseX, mouseY = pg.mouse.get_pos()
    isPressed = pg.mouse.get_pressed()[0]
    isPressed2 = pg.mouse.get_pressed()[2]

    if isPressed2:
        if material == "sand": material = "stone"
        elif material == "stone": material = "water"
        elif material == "water": material = "sand"

    screen.fill((30,30,30))
    moved = [[False for _ in range(cols)] for _ in range(rows)]
    if isPressed:
        mouseX //= CELL_SIZE
        mouseY //= CELL_SIZE

        # checks if mouse is not out of bounds
        if mouseX >= 0 and mouseY >= 0 and mouseX < cols and mouseY < rows:
            if material == "sand" : grid[mouseY][mouseX] = 1
            elif material == "water" : grid[mouseY][mouseX] = 2
            elif material == "stone" : grid[mouseY][mouseX] = 3

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

            # water - claude potahal dekuju :)
            if cell == 2:
                if moved[row][col] == False:
                    

                    # below empty
                    if row + 1 < rows and grid[row+1][col] == 0:
                        grid[row][col] = 0
                        grid[row+1][col] = 2
                        moved[row+1][col] = True
                        pg.draw.rect(screen, color_water, (col*8, row*8, CELL_SIZE, CELL_SIZE))
                    # right-down    
                    elif row + 1 < rows and col + 1 < cols and grid[row+1][col+1] == 0:
                        grid[row][col] = 0
                        grid[row+1][col+1] = 2
                        moved[row+1][col+1] = True
                        pg.draw.rect(screen, color_water, (col*8, row*8, CELL_SIZE, CELL_SIZE))
                    # horizontal spread (random order so it doesn't always favor one side)
                    elif row + 1 < rows and (
                        (col + 1 < cols and grid[row][col+1] == 0) or
                        (col - 1 >= 0 and grid[row][col-1] == 0)
                    ):
                        dirs = [1, -1]
                        random.shuffle(dirs)
                        for d in dirs:
                            nc = col + d
                            if 0 <= nc < cols and grid[row][nc] == 0:
                                grid[row][col] = 0
                                grid[row][nc] = 2
                                moved[row][nc] = True
                                break
                        pg.draw.rect(screen, color_water, (col*8, row*8, CELL_SIZE, CELL_SIZE))
                    # idle
                    else: pg.draw.rect(screen, color_water, (col*8, row*8, CELL_SIZE, CELL_SIZE))

                else:
                    moved[row][col] = False
                    pg.draw.rect(screen, color_water, (col*8, row*8, CELL_SIZE, CELL_SIZE))


            # stone (wow)
            if cell == 3: pg.draw.rect(screen, color_stone, (col*8, row*8, CELL_SIZE, CELL_SIZE))
            

                    
    pg.display.flip()
    time.sleep(0.025)
pg.quit()







