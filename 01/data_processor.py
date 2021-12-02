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
        new_message = str(input_data[i]) + ", " + pairwise_comparison_string(input_data, i)
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
    return counter
