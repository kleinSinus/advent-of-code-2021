# import lib.geometry

def do_stuff(input_data, test_mode):
    aim = False
    position = process_movement(input_data, aim)[0]
    depth = process_movement(input_data, aim)[1]
    output_text = "PART ONE\n========\n\n"
    output_text += "After following the instructions,"
    output_text += " you would have a horizontal position of " + str(position)
    output_text += "\nand a depth of " + str(depth)
    output_text += " (Multiplying these together produces " + str(position*depth) + ")"
    aim = True
    position = process_movement(input_data, aim)[0]
    depth = process_movement(input_data, aim)[1]
    output_text += "\n\nPART TWO\n========\n\n"
    output_text += "After following the better instructions,"
    output_text += " you would have a horizontal position of " + str(position)
    output_text += "\nand a depth of " + str(depth)
    output_text += " (Multiplying these together produces " + str(position*depth) + ")"
    return output_text

def process_movement(input_data, aim):
    if aim:
        return move_with_aim(input_data)
    else:
        return move(input_data)

def move(input_data):
    x = 0
    y = 0
    for command in input_data:
        direction = command.split(' ')[0]
        value = int(command.split(' ')[1])
        if direction == "forward":
            x += value
        elif direction == "up":
            y -= value
        elif direction == "down":
            y += value
        else:
            print("Direction " + direction + " was not expected")
    return [x, y]


def move_with_aim(input_data):
    x = 0
    y = 0
    aim = 0
    for command in input_data:
        direction = command.split(' ')[0]
        value = int(command.split(' ')[1])
        if direction == "forward":
            x += value
            y += aim*value
        elif direction == "up":
            aim -= value
        elif direction == "down":
            aim += value
        else:
            print("Direction " + direction + " was not expected")
    return [x, y]