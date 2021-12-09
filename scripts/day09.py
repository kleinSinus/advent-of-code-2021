import lib.geometry as geo
import lib.arrays as a

def do_stuff(input_data, test_mode):
    output_text = "PART ONE\n========\n\n"
    rows = len(input_data)
    values_per_row = len(input_data[0])
    heatmap = geo.DDDiagram(values_per_row, rows)
    data_lines = []
    for line in input_data:
        data_lines.append(parse_input_line(line))
    for i in range(len(data_lines)):
        heatmap.set_row(i, data_lines[i])
    heatmap.show_heatmap()
    lows = get_low_points(heatmap)
    risk_levels = [low[2]+1 for low in lows]
    for low in lows:
        output_text += "Low Point found at (" + str(low[0]) + ", " + str(low[1]) + "), value = " + str(low[2]) + ". \n"
    output_text += "\nCalculated risk is therefore " + str(a.array_sum(risk_levels)) + ". \n"
    output_text += "\nPART TWO\n========\n\n"
    basins = geo.DDDiagram(values_per_row, rows)
    set_boundaries(heatmap, basins)
    for i in range(len(lows)):
        basins.mat[lows[i][1]][lows[i][0]] = i+1 # each basin gets an index starting at 1
    zeros_found = count_zeros(basins)
    while zeros_found > 0:
        spread_values(basins)
        zeros_found = count_zeros(basins)
    # print(basins)
    output_text += "There are " + str(len(lows)) + " basins.\n"
    basin_sizes = [0] * basins.get_min_max_val()[1]
    for x in range(basins.dim_x):
        for y in range(basins.dim_y):
            if basins.mat[y][x] > 0:
                value = basins.mat[y][x]
                basin_sizes[value-1] += 1
    # print(basin_sizes)
    three_largest = basin_sizes.copy()
    while len(three_largest) > 3:
        three_largest.remove(min(three_largest))
    # print(three_largest)
    output_text += "The three largest basins have sizes " + str(three_largest[0]) + ", "
    output_text += str(three_largest[1]) + " and "
    output_text += str(three_largest[2]) + "."
    output_text += "\nIf you multiply together the sizes of the three largest basins, you get "
    output_text += str(three_largest[0]*three_largest[1]*three_largest[2]) + "."
    return output_text

def parse_input_line(line):
    line_values = []
    for value in line:
        line_values.append(int(value))
    return line_values

def get_low_points(heatmap):
    low_points = []
    for x in range(heatmap.dim_x):
        for y in range(heatmap.dim_y):
            # corners
            if x == 0 and y == 0:
                if heatmap.mat[y][x+1] > heatmap.mat[y][x] and heatmap.mat[y+1][x] > heatmap.mat[y][x]:
                    low_points.append([x, y, heatmap.mat[y][x]])
            elif x == heatmap.dim_x-1 and y == 0:
                if heatmap.mat[y][x-1] > heatmap.mat[y][x] and heatmap.mat[y+1][x] > heatmap.mat[y][x]:
                    low_points.append([x, y, heatmap.mat[y][x]])
            elif x == heatmap.dim_x-1 and y == heatmap.dim_y-1:
                if heatmap.mat[y][x-1] > heatmap.mat[y][x] and heatmap.mat[y-1][x] > heatmap.mat[y][x]:
                    low_points.append([x, y, heatmap.mat[y][x]])
            elif x == 0 and y == heatmap.dim_y-1:
                if heatmap.mat[y][x+1] > heatmap.mat[y][x] and heatmap.mat[y-1][x] > heatmap.mat[y][x]:
                    low_points.append([x, y, heatmap.mat[y][x]])
            # edges
            elif x == 0:
                if heatmap.mat[y][x+1] > heatmap.mat[y][x] and heatmap.mat[y+1][x] > heatmap.mat[y][x] and heatmap.mat[y-1][x] > heatmap.mat[y][x]:
                    low_points.append([x, y, heatmap.mat[y][x]])
            elif x == heatmap.dim_x-1:
                if heatmap.mat[y][x-1] > heatmap.mat[y][x] and heatmap.mat[y+1][x] > heatmap.mat[y][x] and heatmap.mat[y-1][x] > heatmap.mat[y][x]:
                    low_points.append([x, y, heatmap.mat[y][x]])
            elif y == 0:
                if heatmap.mat[y][x+1] > heatmap.mat[y][x] and heatmap.mat[y][x-1] > heatmap.mat[y][x] and heatmap.mat[y+1][x] > heatmap.mat[y][x]:
                    low_points.append([x, y, heatmap.mat[y][x]])
            elif y == heatmap.dim_y-1:
                if heatmap.mat[y][x+1] > heatmap.mat[y][x] and heatmap.mat[y][x-1] > heatmap.mat[y][x] and heatmap.mat[y-1][x] > heatmap.mat[y][x]:
                    low_points.append([x, y, heatmap.mat[y][x]])
            else:
                if heatmap.mat[y][x-1] > heatmap.mat[y][x] and heatmap.mat[y][x+1] > heatmap.mat[y][x] and heatmap.mat[y-1][x] > heatmap.mat[y][x] and heatmap.mat[y+1][x] > heatmap.mat[y][x]:
                    low_points.append([x, y, heatmap.mat[y][x]])
    return low_points

def set_boundaries(heatmap, basinmap):
    for x in range(heatmap.dim_x):
        for y in range(heatmap.dim_y):
            if heatmap.mat[y][x] == 9:
                basinmap.mat[y][x] = -1

def spread_values(basinmap):
    for x in range(basinmap.dim_x):
        for y in range(basinmap.dim_y):
            if basinmap.mat[y][x] != -1:
                if x == 0:
                    if y == 0:
                        basinmap.mat[y][x] = max(basinmap.mat[y][x], basinmap.mat[y][x+1], basinmap.mat[y+1][x])
                    elif y == basinmap.dim_y-1:
                        basinmap.mat[y][x] = max(basinmap.mat[y][x], basinmap.mat[y][x+1], basinmap.mat[y-1][x])
                    else:
                        basinmap.mat[y][x] = max(basinmap.mat[y][x], basinmap.mat[y][x+1], basinmap.mat[y-1][x], basinmap.mat[y+1][x])
                elif y == 0:
                    if x == basinmap.dim_x-1:
                        basinmap.mat[y][x] = max(basinmap.mat[y][x], basinmap.mat[y][x-1], basinmap.mat[y+1][x])
                    else:
                        basinmap.mat[y][x] = max(basinmap.mat[y][x], basinmap.mat[y][x+1], basinmap.mat[y][x-1], basinmap.mat[y+1][x])
                elif x == basinmap.dim_x-1:
                    if y == basinmap.dim_y-1:
                        basinmap.mat[y][x] = max(basinmap.mat[y][x], basinmap.mat[y][x-1], basinmap.mat[y-1][x])
                    else:
                        basinmap.mat[y][x] = max(basinmap.mat[y][x], basinmap.mat[y][x-1], basinmap.mat[y+1][x], basinmap.mat[y-1][x])
                elif y == basinmap.dim_y-1:
                    basinmap.mat[y][x] = max(basinmap.mat[y][x], basinmap.mat[y][x-1], basinmap.mat[y][x+1], basinmap.mat[y-1][x])
                else:
                    basinmap.mat[y][x] = max(basinmap.mat[y][x], basinmap.mat[y][x+1], basinmap.mat[y][x-1], basinmap.mat[y+1][x], basinmap.mat[y-1][x])

def equal_diagrams(diag_A, diag_B):
    difference_found = False
    if diag_A.dim_x != diag_B.dim_x or diag_A.dim_y != diag_B.dim_y:
        difference_found = True
    else:
         for x in range(diag_A.dim_x):
             for y in range(diag_A.dim_y):
                 if diag_A.mat[y][x] != diag_B.mat[y][x]:
                     difference_found = True
    if difference_found:
        return False
    else:
        return True

def count_zeros(heatmap):
    zeros_found = 0
    for x in range(heatmap.dim_x):
        for y in range(heatmap.dim_y):
            if heatmap.mat[y][x] == 0:
                zeros_found += 1
    return zeros_found
