import pygame, sys, random, math

pygame.init()

GAME_TITLE = "Recursive Backtracking Maze Generation"
line_thiccness = 1
WIDTH, HEIGHT = 900 + line_thiccness,900 + line_thiccness


#Creates the display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()
FPS = 144

# Choose a starting point in the field.
# Randomly choose a wall at that point and carve a passage through to the adjacent cell, but only if the adjacent cell has not been visited yet. This becomes the new current cell.
# If all adjacent cells have been visited, back up to the last cell that has uncarved walls and repeat.
# The algorithm ends when the process has backed all the way up to the starting point.


rows = 10
class Cell:

    def __init__(self,x_number, y_number):
        global cell_sequence
        self.width = WIDTH - line_thiccness
        self.height = HEIGHT - line_thiccness



        self.up_wall = True
        self.down_wall = True
        self.left_wall = True
        self.right_wall = True



        self.in_sequence = True
        self.x_number = x_number
        self.y_number = y_number



        self.x_pos = int(x_number * (self.width/rows))
        self.y_pos = int(y_number * (self.height/rows))
        self.blue = (50, 102, 137)
        self.bone_grey = (232, 218, 195)
        self.color = self.blue
        self.rect = pygame.Rect(self.x_pos, self.y_pos, int(self.width/rows), int(self.height/rows))

        #adds x_number and y _number to cell_sequence

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

        if self.up_wall:
            pygame.draw.line(screen, (0, 0, 0), self.rect.topleft, self.rect.topright, line_thiccness)
        if self.down_wall:
            pygame.draw.line(screen, (0, 0, 0), self.rect.bottomleft, self.rect.bottomright, line_thiccness)
        if self.left_wall:
            pygame.draw.line(screen, (0, 0, 0), self.rect.topleft, self.rect.bottomleft, line_thiccness)
        if self.right_wall:
            pygame.draw.line(screen, (0, 0, 0), self.rect.topright, self.rect.bottomright, line_thiccness)

    def wall_update(self):
       pass

    def color_in_sequence(self):
        self.color = self.bone_grey

    def color_out_sequence(self):
        self.color = self.blue

    def color_last_cell(self):
        self.color = (210,31,60)

    def color_finish_sequence(self):
        self.color = (239, 240, 248)

    def report_coords(self):
        coords_list = []
        coords_list.append(self.x_number)
        coords_list.append(self.y_number)
        return coords_list

    def report_adjacent(self):

        #Please do not look at this method, I didn't mean for the following code to ever happen. But I don't know how else to do it
        #I really should repent

        available_sides = ["up","down","left","right"]
        if False:
            for cell in cell_list[:-1]:
                if cell.x_number == self.x_number:
                    if cell.y_number == self.x_number:
                        cell_list.remove(cell)

        #checks against all other cells
        for cell in cell_list[:-1]:
            if (cell.x_number == self.x_number + 1) and (cell.y_number == self.y_number):
                if "right" in available_sides:
                    available_sides.remove("right")
            elif cell.x_number == (self.x_number - 1) and cell.y_number == self.y_number:
                if "left" in available_sides:
                    available_sides.remove("left")
            elif cell.y_number == (self.y_number + 1) and cell.x_number == self.x_number:
                if "down" in available_sides:
                    available_sides.remove("down")
            elif cell.y_number == (self.y_number - 1) and cell.x_number == self.x_number:
                if "up" in available_sides:
                    available_sides.remove("up")

        #checks against the boundries (if its on the edge)
        if self.x_number==rows-1:
            if "right" in available_sides:
                available_sides.remove("right")
        if self.x_number==0:
            if "left" in available_sides:
                available_sides.remove("left")
        if self.y_number==rows-1:
            if "down" in available_sides:
                available_sides.remove("down")
        if self.y_number==0:
            if "up" in available_sides:
                available_sides.remove("up")

        if len(available_sides) > 0:
            return available_sides
        return False

    def deconstruct_wall(self, wall):
        if wall == "up":
            self.down_wall = False
            print("down wall")
        elif wall == "down":
            self.up_wall = False
            print("up wall")
        elif wall == "left":
            self.right_wall = False
            print("right wall")
        elif wall == "right":
            self.left_wall = False
            print("left wall")
        print("\n")


    def __str__(self):
        return [self.x_number, self.y_number]


def deconstruct_wall(adjacent_list):
    #adjacent_list should be available_adjacent[0]
    wall_direction = None
    if adjacent_list == "up":
        pass


def add_cell():
    global cell_list, cell_sequence

    #Makes sure a possible move isn't past the edges
    #Makes a list containing two lists. First sub-list is wether it can go left or right and second sub-list is wether it can go up and down

    running = True
    if cell_sequence:
        #while running:
        last_cell = cell_sequence[-1]

        last_cell_pos = last_cell.report_coords()
        available_adjacent = last_cell.report_adjacent()

        new_x_num = last_cell.x_number
        new_y_num = last_cell.y_number

        #Checks to make sure there are available sides
        if available_adjacent:
            #randomizes all the possible adjacent sides
            random.shuffle(available_adjacent)

            #sets the new y or x num to the last cells x or y number +1 or -1
            if available_adjacent[0] == "up":
                new_y_num = last_cell.y_number - 1
            elif available_adjacent[0] == "down":
                new_y_num = last_cell.y_number + 1
            elif available_adjacent[0] == "left":
                new_x_num = last_cell.x_number - 1
            elif available_adjacent[0] == "right":
                new_x_num = last_cell.x_number + 1
            cell = Cell(new_x_num, new_y_num)
            cell_sequence.append(cell)
            cell_list.append(cell)

            #Deconstructs the walls
            cell.deconstruct_wall(available_adjacent[0])
            opposite_wall = None
            if available_adjacent[0] == "up":
                opposite_wall = "down"
            elif available_adjacent[0] == "down":
                opposite_wall = "up"
            elif available_adjacent[0] == "left":
                opposite_wall = "right"
            elif available_adjacent[0] == "right":
                opposite_wall = "left"
            cell_sequence[-2].deconstruct_wall(opposite_wall)

            running = False

        #if there are no available sides then it will delete the last cell from the cell sequence and start again
        else:
            cell_sequence.pop(-1)



first_cell = Cell(0,0)
cell_sequence = [first_cell]
cell_list = [first_cell]
add_cell()

cell_add_bool = False
game_running = True
while game_running:
    screen.fill((30,30,30))
    screen.fill((255,255,255))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            cell_add_bool = True

        if event.type == pygame.MOUSEBUTTONUP:
            cell_add_bool = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                first_cell = Cell(0, 0)
                cell_sequence = [first_cell]
                cell_list = [first_cell]


    for cell in cell_list:
        cell.draw()

    if cell_add_bool:
        add_cell()



    #colors in the cells
    for cell in cell_sequence:
        cell.color_in_sequence()
    for cell in cell_list:
        if cell not in cell_sequence:
            cell.color_out_sequence()
    if cell_sequence:
        cell_sequence[-1].color_last_cell()
    else:
        for cell in cell_list:
            cell.color_finish_sequence()
        cell_list[0].color_last_cell()

    #pygame.draw.rect(screen, (255, 255, 0), (500, 30, 80, 60))

    clock.tick(FPS)
    pygame.display.flip()

