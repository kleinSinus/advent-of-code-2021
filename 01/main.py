# get string that verbalizes the measurement difference between current depth and previous depth
def measurement_difference_string(input_data, i):
    if i == 0:
        return "(N/A - no previous measurement)"
    elif input_data[i] > input_data[i-1]:
        return "(increased)"
    elif input_data[i] == input_data[i-1]:
        return "(no change)"
    else:
        return "(decreased)"


# process input data array with depth measurements, return table with measurements and their status
def process_measurements(input_data):
    array_size = len(input_data)
    status_messages = [""] * array_size
    for i in range(array_size):
        new_message = str(input_data[i]) + ", " + measurement_difference_string(input_data, i)
        print(new_message)
        status_messages[i] = new_message
    return status_messages


# count increments within input data
def count_increments(input_data):
    array_size = len(input_data)
    counter = 0
    for i in range(array_size-1):
        if input_data[i+1] > input_data[i]:
            counter += 1
    print("\nIn this input data there are " + str(counter) + " measurements larger than the previous measurement.")
    return counter


def process_input_file():
    # get data
    file = open("input.txt", "r")
    input_data = []
    for line in file:
        content = int(line[:-1])
        input_data.append(content)
    print(input_data)
    process_measurements(input_data)
    count_increments(input_data)


def process_test_input():
    input_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    process_measurements(input_data)
    count_increments(input_data)


# process_test_input()
process_input_file()

