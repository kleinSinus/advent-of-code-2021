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
    increment_counter = 0
    status_messages = [0] * array_size
    for i in range(array_size):
        new_message = measurement_difference_string(input_data, i)
        status_messages[i] = new_message
    return status_messages


# start measurement processing for test data
test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
process_measurements(test_data)