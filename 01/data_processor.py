# takes an array and an index i and compares values at this and the previous positions
def pairwise_comparison_string(input_data, i):
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
        label = get_label_from_int(i+1)
        new_message = label + ": " + str(input_data[i]) + ", " + pairwise_comparison_string(input_data, i)
        status_messages[i] = new_message
    return status_messages


def int_to_base26(i):
    number = i
    base26_number_backwards = []
    while number > 0:
        base26_number_backwards.append(number%26)
        number = number//26
    base26_number_length = len(base26_number_backwards)
    base26_number = [0]*base26_number_length
    for i in range(base26_number_length):
        base26_number[i] = base26_number_backwards[base26_number_length-i-1]
    return base26_number


def get_label_from_int(i):
    label = ''
    base26_number = int_to_base26(i)
    print(base26_number)
    for i in range(len(base26_number)):
        label += (chr(ord('@')+base26_number[i]))
    return label


# process input data, into windows with sums
def get_sum_window_data(input_data, window_size):
    array_size = len(input_data-window_size+1)
    window_data = [0]*array_size
    for i in range(array_size):
        window_data = input_data[i] + input_data[i+1] + input_data[i+2]
    return window_data


# count increments within input data
def count_increments(input_data):
    array_size = len(input_data)
    counter = 0
    for i in range(array_size-1):
        if input_data[i+1] > input_data[i]:
            counter += 1
    return counter
