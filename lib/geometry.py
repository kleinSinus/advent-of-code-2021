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
    mat = []
    image = None

    def __init__(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.mat = [[0 for i in range(dim_x)] for j in range(dim_y)]
        self.image = Image.new("RGB", size=(dim_x, dim_y))
        for x in range(dim_x):
            for y in range(dim_y):
                self.image.putpixel((x, y), (255, 255, 255))

    def __str__(self):
        description = ''
        for row in self.mat:
            for cell in row:
                if cell == -1:
                    description += 'X'
                else:
                    description += str(cell)
            description += '\n'
        return description

    def get_min_max_val(self):
        min = self.mat[0][0]
        max = self.mat[0][0]
        for i in range(self.dim_y):
            for j in range(self.dim_x):
                if self.mat[i][j] > max:
                    max = self.mat[i][j]
                if self.mat[i][j] < min:
                    min = self.mat[i][j]
        return min, max

    def set_value(self, x, y, value):
        self.mat[y][x] = value
    
    def set_row(self, row_index, row_values):
        if len(row_values) > self.dim_x:
            print("Inserted row is too long")
        elif row_index > self.dim_y:
            print("Row to be inserted out of diagram scope")
        else:
            for i in range(len(row_values)):
                self.set_value(i, row_index, row_values[i])
        
    def draw_heatmap(self):
        min_val = self.get_min_max_val()[0]
        max_val = self.get_min_max_val()[1]
        value_range = max_val - min_val
        for x in range(self.dim_x):
            for y in range(self.dim_y):
                heat_value = min(max(int((self.mat[y][x]-min_val)/value_range * 200), 0), 255)
                base = 55
                heat_color = (base+heat_value, base, 255-heat_value)
                self.image.putpixel((x, y), heat_color)

    def show_heatmap(self):
        self.draw_heatmap()
        self.image.show()