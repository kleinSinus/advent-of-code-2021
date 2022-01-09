# import lib

def do_stuff(input_data, test_mode):
    dots, folds = order_input_data(input_data)
    max_x = 0
    max_y = 0
    for dot in dots:
        if dot[0] > max_x:
            max_x = dot[0]
        if dot[1] > max_y:
            max_y = dot[1]
    # print(max_x, max_y)
    matrix = [[0 for i in range(max_x+1)] for j in range(max_y+1)]
    for dot in dots:
        matrix[dot[1]][dot[0]] += 1
    if test_mode :
        output_text = "PART ONE\n========\n\n"
        output_text += matrix_to_string(matrix)
        output_text += "\n\n"
        matrix = fold_matrix(matrix,folds[0][0], folds[0][1])
        output_text += matrix_to_string(matrix)
        sum = 0
        for row in matrix:
            for cell in row:
                if cell != 0:
                    sum += 1
        output_text += "\nAfter the first fold in the example above, " + str(sum) + " dots are visible"
        output_text += "\n\n\nPART TWO\n========\n"
        
        del folds[0]
        for fold in folds:
            output_text += "\n"
            matrix = fold_matrix(matrix,fold[0], fold[1])
            output_text += matrix_to_string(matrix)
    else:
        output_text = "PART ONE\n========\n"
        output_text += matrix_to_string(matrix)
        output_text += "\n\n"
        matrix = fold_matrix(matrix,folds[0][0], folds[0][1])
        output_text += matrix_to_string(matrix)
        sum = 0
        for row in matrix:
            for cell in row:
                if cell != 0:
                    sum += 1
        output_text += "\nAfter the first fold in the example above, " + str(sum) + " dots are visible"
        output_text += "\n\n\nPART TWO\n========\n\n"
        del folds[0]
        for fold in folds:
            output_text += "\n"
            matrix = fold_matrix(matrix,fold[0], fold[1])
            output_text += matrix_to_string(matrix)

    return output_text

def order_input_data(input_data):
    dots = []
    folds = []
    dot_mode = True
    i = 0
    while dot_mode:
        dots.append([int(coordinate) for coordinate in input_data[i].split(',')])
        i += 1
        if input_data[i] == "":
            dot_mode = False
    i += 1
    while i < len(input_data):
        relevant_input = input_data[i][11:]
        folds.append([relevant_input.split('=')[0], int(relevant_input.split('=')[1])])
        i += 1
    return dots, folds

def matrix_to_string(matrix):
    output = ""
    for row in matrix:
        for i in range(len(row)):
            if row[i] == 0:
                output += '.'
            else:
                output += '#'
        output += "\n"
    return output

def fold_matrix(matrix, fold_axis, index):
    print("Folding on axis " + fold_axis)
    if fold_axis == 'y':
        for i in range(index):
            add_matrix_rows(matrix, i, 2 * index - i)
        matrix = matrix[:index] 
    elif fold_axis == 'x':
        for i in range(index):
            add_matrix_columns(matrix, i, 2 * index - i)
        for row in range(len(matrix)):
            matrix[row] = matrix[row][:index]
    return matrix
    

def add_matrix_rows(matrix, i, j):
    print("\nAdding rows " + str(i) + " and " + str(j))
    print("Row " + str(i) + ":")
    print(matrix[i])
    print("Row " + str(j) + ":")
    print(matrix[j])
    matrix[i] = [matrix[i][x]+matrix[j][x] for x in range(len(matrix[i]))]
    print("Sum:")
    print(matrix[i])

def add_matrix_columns(matrix, i, j):
    for row in matrix:
        row[i] += row[j]