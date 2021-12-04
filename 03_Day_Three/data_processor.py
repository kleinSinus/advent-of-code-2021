# get the first bits, 2nd bits, 3rd bits and so on from the input_data into groups represented by one bitstring each
def group_bits(input_data):
    if not input_data:
        return input_data
    else:
        input_copy = input_data.copy()
        entry_length = len(input_copy[0])
        grouped_bits = ['']*entry_length
        for i in range(entry_length):
            for j in range(len(input_copy)):
                grouped_bits[i] += input_copy[j][0]
                input_copy[j] = input_copy[j][1:]
    return grouped_bits


# takes bitstring, returns most frequent bit, if both 0s and 1s are equally frequent returns 1
def most_common_digit(bitstring):
    zeros_n_ones = [0,0]
    for digit in bitstring:
        if digit == '0':
            zeros_n_ones[0] += 1
        elif digit == '1':
            zeros_n_ones[1] += 1
        else:
            print("Unexpected digit encountered")
    if zeros_n_ones[0] > zeros_n_ones[1]:
        return '0'
    else:
        return '1'


# takes bitstring, returns most frequent bit, if both 0s and 1s are equally frequent returns 0
def least_common_digit(bitstring):
    zeros_n_ones = [0,0]
    for digit in bitstring:
        if digit == '0':
            zeros_n_ones[0] += 1
        elif digit == '1':
            zeros_n_ones[1] += 1
        else:
            print("Unexpected digit encountered")
    if zeros_n_ones[0] > zeros_n_ones[1]:
        return '1'
    else:
        return '0'


# takes a list of binary numbers and returns it without entries, that have a 1 as i-th digit
def del_zero(bit_num_list, i):
    new_bit_num_list = []
    for entry in bit_num_list:
        if entry[i] == '1':
            new_bit_num_list.append(entry)
    return new_bit_num_list


# takes a list of binary numbers and returns it without entries, that have a 0 as i-th digit
def del_one(bit_num_list, i):
    new_bit_num_list = []
    for entry in bit_num_list:
        if entry[i] == '0':
            new_bit_num_list.append(entry)
    return new_bit_num_list


# compute a binary number by finding the most common bit in the corresponding position of all numbers
def compute_gamma_rate(input_data):
    input_copy = input_data.copy()
    grouped_bits = group_bits(input_copy)
    gamma = ''
    for bitstring in grouped_bits:
        gamma += most_common_digit(bitstring)
    return gamma


# computes epsilon value by inverting the digits of the gamma value
def compute_epsilon_rate(gamma):
    epsilon = ''
    for digit in gamma:
        if digit == '0':
            epsilon += '1'
        elif digit == '1':
            epsilon += '0'
        else:
            print("Did not expect '" + digit + "' in a binary number.")
    return epsilon


# gets a binary number as string and returns the corresponding decimal value
def bin2dec(binary_number):
    dec_value = 0
    number_length = len(binary_number)
    for i in range(number_length):
        dec_value += 2 ** (-(i-number_length+1)) * int(binary_number[i])
    return dec_value


def compute_oxygen_generator_rating(input_data):
    numbers_considered = input_data.copy()
    oxy_gen = ''
    bits_tested = 0
    stopped = False
    while not stopped:
        next_digit = most_common_digit(group_bits(numbers_considered)[bits_tested])
        if next_digit == '0':
            numbers_considered = del_one(numbers_considered, bits_tested)
        elif next_digit == '1':
            numbers_considered = del_zero(numbers_considered, bits_tested)
        else:
            print("Unexpected digit in a bitstring!")
        oxy_gen += next_digit
        bits_tested += 1
        if len(numbers_considered) == 1:
            stopped = True
            oxy_gen = numbers_considered[0]
    return oxy_gen


def compute_co2_scrubber_rating(input_data):
    numbers_considered = input_data.copy()
    co2 = ''
    bits_tested = 0
    stopped = False
    while not stopped:
        next_digit = least_common_digit(group_bits(numbers_considered)[bits_tested])
        if next_digit == '0':
            numbers_considered = del_one(numbers_considered, bits_tested)
        elif next_digit == '1':
            numbers_considered = del_zero(numbers_considered, bits_tested)
        else:
            print("Unexpected digit in a bitstring!")
        co2 += next_digit
        bits_tested += 1
        if len(numbers_considered) == 1:
            stopped = True
            co2 = numbers_considered[0]
    return co2


# generates output text
def gen_output(gamma_value, epsilon_value, oxy_gen, co2_scrub):
    output_text = "Gamma rate:   " + gamma_value
    output_text += "\n    -> That's " + str(bin2dec(gamma_value)) + " in decimal."
    output_text += "\nEpsilon rate: " + epsilon_value
    output_text += "\n    -> That's " + str(bin2dec(epsilon_value)) + " in decimal."
    output_text += "\n\nThe power consumption is therefore " + str(bin2dec(gamma_value)*bin2dec(epsilon_value)) + "."
    output_text += "\n\nOxygen Generator: " + oxy_gen
    output_text += "\n    -> That's " + str(bin2dec(oxy_gen)) + " in decimal."
    output_text += "\nCO2 Scrubber:     " + co2_scrub
    output_text += "\n    -> That's " + str(bin2dec(co2_scrub)) + " in decimal."
    output_text += "\n\nThe life support rating is therefore " + str(bin2dec(oxy_gen)*bin2dec(co2_scrub)) + "."
    return output_text
