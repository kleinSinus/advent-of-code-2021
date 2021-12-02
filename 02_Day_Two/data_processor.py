def process_movement(input_data):
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
