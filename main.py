import pygame as pg
import time

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
materialList = ["sand", "stone"]
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
        elif material == "stone": material = "sand"

    screen.fill((30,30,30))
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

            # water
            if cell == 2:
                # below empty
                if row + 1 < rows and grid[row+1][col] == 0:
                    grid[row][col] = 0
                    grid[row+1][col] = 2
                    pg.draw.rect(screen, color_water, (col*8, row*8, CELL_SIZE, CELL_SIZE))
                # right-down    
                elif row + 1 < rows and col + 1 < cols and grid[row+1][col+1] == 0:
                    grid[row][col] = 0
                    grid[row+1][col+1] = 2
                    pg.draw.rect(screen, color_water, (col*8, row*8, CELL_SIZE, CELL_SIZE))
                # right
                elif row + 1 < rows and col + 1 < cols and grid[row][col+1] != 2:
                    grid[row][col] = 0
                    grid[row][col+1] = 2
                    pg.draw.rect(screen, color_water, (col*8, row*8, CELL_SIZE, CELL_SIZE))
                # left
                elif row + 1 < rows and col - 1 >= 0 and grid[row+1][col-1] == 0:
                    grid[row][col] = 0
                    grid[row+1][col-1] = 2
                    pg.draw.rect(screen, color_water, (col*8, row*8, CELL_SIZE, CELL_SIZE))
            
                else: pg.draw.rect(screen, color_water, (col*8, row*8, CELL_SIZE, CELL_SIZE))

            # stone
            if cell == 3: pg.draw.rect(screen, color_stone, (col*8, row*8, CELL_SIZE, CELL_SIZE))
            

                    
    pg.display.flip()
    time.sleep(0.025)
pg.quit()







