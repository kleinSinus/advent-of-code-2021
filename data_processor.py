import math
from PIL import Image


# a simple 2D line
class DDLine:
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    length = 0

    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.length = math.sqrt((end_x-start_x)**2 + (end_y-start_y)**2)

    def __str__(self):
        return f"{self.start_x},{self.start_y} -> {self.end_x},{self.end_y}"


# a simple 2D plotter class
class DDDiagram:
    dim_x = 0
    dim_y = 0
    max_val = 0
    mat = []
    image = None

    def __init__(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.mat = [[0 for i in range(dim_y)] for j in range(dim_x)]
        self.image = Image.new("RGB", size=(dim_x, dim_y))
        for x in range(dim_x):
            for y in range(dim_y):
                self.image.putpixel((x, y), (255, 255, 255))

    def __str__(self):
        description = ''
        description += "Max value: " + str(self.max_val)
        description += "\nOverlap count: " + str(self.overlap_count())
        description += "\nMax value count: " + str(self.max_value_count()) + "\n\n"
        for row in self.mat:
            for cell in row:
                if cell == 0:
                    description += '.'
                else:
                    description += str(cell)
            description += '\n'
        return description

    def add_point(self, x, y):
        if self.mat[y][x] == self.max_val:
            self.max_val += 1
        self.mat[y][x] += 1
        # print("Set point (" + str(x) + ", " + str(y) + ") to " + str(self.mat[y][x]))

    def draw_axis_parallel_lines(self, lines):
        for line in lines:
            # print(line)
            if line.start_x == line.end_x or line.start_y == line.end_y:
                self.draw_line(line)

    def draw_diagonal_lines(self, lines):
        for line in lines:
            print(line)
            dx = int(math.fabs(line.end_x-line.start_x))
            dy = int(math.fabs(line.end_y-line.start_y))
            if dx == dy:
                self.draw_line(line)

    def draw_line(self, line):
        if line.start_x > line.end_x:
            start = (line.end_x, line.end_y)
            end = (line.start_x, line.start_y)
        else:
            start = (line.start_x, line.start_y)
            end = (line.end_x, line.end_y)
        x_min = min(line.end_x, line.start_x)
        y_min = min(line.end_y, line.start_y)
        x_max = max(line.end_x, line.start_x)
        y_max = max(line.end_y, line.start_y)
        dx = x_max - x_min
        dy = y_max - y_min
        y_dir = end[1]-start[1]
        if dx == 0:
            for i in range(dy+1):
                self.add_point(x_min, y_min+i)
        else:
            if y_dir < 0:
                y_step = -dy/dx
            else:
                y_step = dy/dx
            for x_step in range(dx+1):
                self.add_point(start[0]+x_step, start[1]+x_step*int(y_step))

    def max_value_count(self):
        count = 0
        for i in range(self.dim_x):
            for j in range(self.dim_y):
                if self.mat[i][j] == self.max_val:
                    count += 1
        return count

    def overlap_count(self):
        count = 0
        for i in range(self.dim_x):
            for j in range(self.dim_y):
                if self.mat[i][j] > 1:
                    count += 1
        return count

    def draw_image(self):
        for x in range(self.dim_x):
            for y in range(self.dim_y):
                grey_tone = min(max(int(255 * (1 - self.mat[y][x]/self.max_val)), 0), 255)
                grey = (grey_tone, grey_tone, grey_tone)
                red = (255, 0, 0)
                if self.mat[y][x] == self.max_val:
                    self.image.putpixel((x, y), red)
                else:
                    self.image.putpixel((x, y), grey)

    def show_image(self):
        self.image.show()


# generates a 2D-line-representation from an input line formatted like "x,y -> x,y"
def input_line2ddline(input_line):
    start = input_line.split(' -> ')[0]
    end = input_line.split(' -> ')[1]
    start_x = int(start.split(',')[0])
    start_y = int(start.split(',')[1])
    end_x = int(end.split(',')[0])
    end_y = int(end.split(',')[1])
    ddline = DDLine(start_x, start_y, end_x, end_y)
    return ddline


# converts the input file into a list of lines
def input2lines(input_file):
    line_list = []
    for line in input_file:
        line_list.append(input_line2ddline(line))
    return line_list


# gets the maximal 2D dimensions of a list of lines
def get_dim(line_list):
    max_x = 0
    max_y = 0
    for line in line_list:
        if line.start_x > max_x:
            max_x = line.start_x
        elif line.start_y > max_y:
            max_y = line.start_y
        elif line.end_x > max_x:
            max_x = line.end_x
        elif line.end_y > max_y:
            max_y = line.end_y
    return max_x+1, max_y+1  # plus 1 for padding


# generates output text
def gen_output(input_data):
    input_lines = input2lines(input_data)
    # print("Processing input:\n")
    dim = get_dim(input_lines)
    # print("\nGenerating Diagram: \n")
    output_text = "OUTPUT\n======\n\n"
    diagram = DDDiagram(dim[0], dim[1])
    diagram.draw_axis_parallel_lines(input_lines)
    diagram.draw_diagonal_lines(input_lines)
    output_text += str(diagram)
    diagram.draw_image()
    diagram.show_image()
    return output_text
