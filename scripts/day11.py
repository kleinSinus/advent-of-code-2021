def do_stuff(input_data, test_mode):
    octopus_grid = [[int(c) for c in line] for line in input_data]
    output_text = "PART ONE\n========\n\n"
    total_flashes = 0
    # print(octopus_grid)
    steps = 100
    for n in range(steps):  # 100 steps
        total_flashes += one_step(octopus_grid)[0]
    output_text += "After " + str(steps) + " steps, there have been a total of " + str(total_flashes) + " flashes."
    output_text += "\n\nPART TWO\n========\n\n"
    octopus_grid = [[int(c) for c in line] for line in input_data]
    all_flashed = False
    steps = 0
    while not all_flashed:
        all_flashed = one_step(octopus_grid)[1]
        steps += 1
    output_text += "The first time all octopuses flash simultaneously is step " + str(steps) + "."
    return output_text

def one_step(octo_grid):
    rows = len(octo_grid)
    columns = len(octo_grid[0])
    for i in range(rows):
        for j in range(columns):
            octo_grid[i][j] += 1  # first increase energy level
    flashes = 0
    flashes_old = -1
    flashed = [[0] * len(row) for row in octo_grid]
    while flashes_old != flashes:
        flashes_old = flashes
        for i in range(rows):
            for j in range(columns):
                if octo_grid[i][j] > 9 and flashed[i][j] != 1:
                    flashes += 1
                    flashed[i][j] = 1
                    if i == 0:
                        if j == 0:
                            octo_grid[i+1][j] += 1
                            octo_grid[i+1][j+1] += 1
                            octo_grid[i][j+1] += 1
                        elif j == columns-1:
                            octo_grid[i+1][j-1] += 1
                            octo_grid[i+1][j] += 1
                            octo_grid[i][j-1] += 1
                        else:
                            octo_grid[i+1][j-1] += 1
                            octo_grid[i+1][j] += 1
                            octo_grid[i+1][j+1] += 1
                            octo_grid[i][j-1] += 1
                            octo_grid[i][j+1] += 1
                    elif i == rows-1:
                        if j == 0:
                            octo_grid[i-1][j] += 1
                            octo_grid[i-1][j+1] += 1
                            octo_grid[i][j+1] += 1
                        elif j == columns-1:
                            octo_grid[i-1][j-1] += 1
                            octo_grid[i-1][j] += 1
                            octo_grid[i][j-1] += 1
                        else:
                            octo_grid[i-1][j-1] += 1
                            octo_grid[i-1][j] += 1
                            octo_grid[i-1][j+1] += 1
                            octo_grid[i][j-1] += 1
                            octo_grid[i][j+1] += 1
                    elif j == 0:
                        octo_grid[i-1][j] += 1
                        octo_grid[i-1][j+1] += 1
                        octo_grid[i+1][j] += 1
                        octo_grid[i+1][j+1] += 1
                        octo_grid[i][j+1] += 1
                    elif j == columns-1:
                        octo_grid[i-1][j-1] += 1
                        octo_grid[i-1][j] += 1
                        octo_grid[i+1][j-1] += 1
                        octo_grid[i+1][j] += 1
                        octo_grid[i][j-1] += 1
                    else:
                        octo_grid[i-1][j-1] += 1
                        octo_grid[i-1][j] += 1
                        octo_grid[i-1][j+1] += 1
                        octo_grid[i+1][j-1] += 1
                        octo_grid[i+1][j] += 1
                        octo_grid[i+1][j+1] += 1
                        octo_grid[i][j-1] += 1
                        octo_grid[i][j+1] += 1
    everyone_flashed = True
    for i in range(len(octo_grid)):
        for j in range(len(octo_grid[i])):
            if octo_grid[i][j] > 9:
                octo_grid[i][j] = 0
            if flashed[i][j] == 0:
                everyone_flashed = False
    # print(octo_grid)
    return flashes, everyone_flashed
