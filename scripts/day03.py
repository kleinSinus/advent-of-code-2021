import lib.type_converter as tc

def do_stuff(input_data, test_mode):
    gamma = compute_gamma_epsilon(input_data)[0]
    epsilon = compute_gamma_epsilon(input_data)[1]
    gamma_num = tc.base2int(tc.bits2bin(gamma), 2)
    epsilon_num = tc.base2int(tc.bits2bin(epsilon), 2)
    
    output_text = "PART ONE\n========\n\n"
    output_text += "Gamma rate: " + gamma + " -> " + str(gamma_num) + "\n"
    output_text += "Epsilon rate: " + epsilon + " -> " + str(epsilon_num) + "\n"
    output_text += "=> Power consumption: " + str(gamma_num*epsilon_num)

    oxygen = compute_oxy_co2(input_data)[0]
    co2 = compute_oxy_co2(input_data)[1]
    oxy_num = tc.base2int(tc.bits2bin(oxygen), 2)
    co2_num = tc.base2int(tc.bits2bin(co2), 2)

    output_text += "\n\nPART TWO\n========\n\n"
    output_text += "Oxygen rate: " + oxygen + " -> " + str(oxy_num) + "\n"
    output_text += "CO2 rate: " + co2 + " -> " + str(co2_num) + "\n"
    output_text += "=> Life Support Rating: " + str(oxy_num*co2_num)
    return output_text

def compute_oxy_co2(input_data):
    oxy_number_pool = input_data.copy()
    co2_number_pool = input_data.copy()
    oxy_prefix = ''
    co2_prefix = ''
    bits_tested = 0
    stopped = False
    while not stopped:
        oxy_prefix += common_bit(group_bits(oxy_number_pool)[bits_tested], True)
        oxy_number_pool = prefix_match(oxy_number_pool, oxy_prefix)
        bits_tested += 1
        if len(oxy_number_pool) == 1:
            stopped = True
            oxy_prefix = oxy_number_pool[0]
    bits_tested = 0
    stopped = False
    while not stopped:
        co2_prefix += common_bit(group_bits(co2_number_pool)[bits_tested], False)
        co2_number_pool = prefix_match(co2_number_pool, co2_prefix)
        bits_tested += 1
        if len(co2_number_pool) == 1:
            stopped = True
            co2_prefix = co2_number_pool[0]
    return oxy_prefix, co2_prefix

# compute a binary number by finding the most common bit
# in the corresponding position of all numbers
def compute_gamma_epsilon(input_data):
    input_copy = input_data.copy()
    grouped_bits = group_bits(input_copy)
    gamma = ''
    epsilon = ''
    for bitstring in grouped_bits:
        gamma += common_bit(bitstring, True)
        epsilon += common_bit(bitstring, False)
    return gamma, epsilon

# get the first bits, 2nd bits, 3rd and so on from the input_data into groups
# represented by one bitstring each
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

# takes an array and returns only the entries that match a certain prefix
def prefix_match(array, prefix):
    result = []
    for entry in array:
        if entry[:len(prefix)] == prefix:
            result.append(entry)
    return result

# finds the most or least common bit in a bitstring
# if 0 and 1 are equally common it's decided by the mode
def common_bit(bitstring, mode_most):
    bit_counter = [0,0]
    for digit in bitstring:
        if digit == '0':
            bit_counter[0] += 1
        elif digit == '1':
            bit_counter[1] += 1
        else:
            print("Unexpected bit encountered")
    if mode_most:
        if bit_counter[0] > bit_counter[1]:
            return '0'
        else:
            return '1'
    else:
        if bit_counter[0] > bit_counter[1]:
            return '1'
        else:
            return '0'