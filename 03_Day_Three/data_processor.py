# compute a binary number by finding the most common bit in the corresponding position of all numbers
def compute_gamma_rate(input_data):
    gamma_vector = [0] * len(input_data[0])
    for number in input_data:
        for i in range(len(number)):
            if number[i] == '0':
                gamma_vector[i] -= 1
            elif number[i] == '1':
                gamma_vector[i] += 1
            else:
                print("Did not expect '" + number[i] + "' in a binary number.")
    gamma_value = ""
    for digit in gamma_vector:
        if digit > 0:
            gamma_value += '1'
        elif digit < 0:
            gamma_value += '0'
        else:
            gamma_value += '_'
    return gamma_value


# gets a binary number as string and returns the corresponding decimal value
def bin2dec(binary_number):
    dec_value = 0
    number_length = len(binary_number)
    for i in range(number_length):
        dec_value += 2 ** (-(i-number_length+1)) * int(binary_number[i])
    return dec_value


# generates output text
def gen_output(gamma_value, epsilon_value):
    output_text = "Gamma rate: " + gamma_value
    output_text += "\n    -> That's " + str(bin2dec(gamma_value)) + " in decimal."
    output_text += "\n Epsilon rate: " + epsilon_value
    output_text += "\n    -> That's " + str(bin2dec(epsilon_value)) + " in decimal."
    output_text += "\n\n The power consumption is therefore " + str(bin2dec(gamma_value)*bin2dec(epsilon_value)) + "."
    return output_text


# computes epsilon value by inverting the digits of the gamma value
def compute_epsilon_rate(gamma_value):
    epsilon_value = ''
    for digit in gamma_value:
        if digit == '0':
            epsilon_value += '1'
        elif digit == '1':
            epsilon_value += '0'
        else:
            print("Did not expect '" + digit + "' in a binary number.")
    return epsilon_value
