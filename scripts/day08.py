import lib.arrays as a

def do_stuff(input_data, test_mode):
    output_text = "PART ONE\n========\n\n"
    segment_inputs = ['']*len(input_data)
    for i in range(len(input_data)):
        segment_inputs[i] = parse_input_line(input_data[i])
    outputs = []
    for j in range(len(segment_inputs)):
        segment_strings = segment_inputs[j][0]
        digit_strings = segment_inputs[j][1]
        key = segment_solver(segment_strings)
        digit_map = []
        for segment_string in segment_strings:
            digit_map.append(segment_string_mapper(segment_string, key))
        # print(digit_map) # for testing
        digits = []
        for digit_string in digit_strings:
            digits.append(segment_string_mapper(digit_string, key))
        outputs.append(digits)
    digit_occurence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for output in outputs:
        for i in range(4):
            digit_occurence[output[i]] += 1
    unique_count = digit_occurence[1] + digit_occurence[4] + digit_occurence[7] + digit_occurence[8]
    output_text += "In the example, there are " + str(unique_count)
    output_text += " instances of digits that use a unique number of segments."
    output_text += "\n\nPART TWO\n========\n\n"
    output_values = []
    for output in outputs:
        value = output[0]*1000 + output[1]*100 + output[2]*10 + output[3]
        output_values.append(value)
    output_text += "Adding all of the output values in this example produces "
    output_text += str(a.array_sum(output_values)) + "."
    return output_text

def parse_input_line(line):
    digit_string = line.split('| ')[0]
    number_string = line.split('| ')[1]
    digits = digit_string.split()
    numbers = number_string.split()
    return digits, numbers

# takes the string for a segment and a key and maps those
# onto a 7 segment signal, returns identified digit or error
def segment_string_mapper(segment_string, key):
    display = [0, 0, 0, 0, 0, 0, 0]
    for letter in segment_string:
        for i in range(7):
            if letter == key[i]:
                display[i] = 1
    output = seg2num(display)
    if output == 10:
        print(display)
        print(key)
        print(segment_string)
    return output

def segment_solver(segment_list):
    a = identify_A(segment_list)
    b = identify_B(segment_list)
    c = identify_C(segment_list)
    d = identify_D(segment_list)
    e = identify_E(segment_list)
    f = identify_F(segment_list)
    g = identify_G(segment_list)
    return [a, b, c, d, e, f, g]

# expects a digit from 0 to 9, returns a list of 1s for on and 0s for off segments 
def num2seg(num):
    if num == 0:
        return [1,1,1,0,1,1,1]
    elif num == 1:
        return [0,0,1,0,0,1,0]
    elif num == 2:
        return [1,0,1,1,1,0,1]
    elif num == 3:
        return [1,0,1,1,0,1,1]
    elif num == 4:
        return [0,1,1,1,0,1,0]
    elif num == 5:
        return [1,1,0,1,0,1,1]
    elif num == 6:
        return [1,1,0,1,1,1,1]
    elif num == 7:
        return [1,0,1,0,0,1,0]
    elif num == 8:
        return [1,1,1,1,1,1,1]
    elif num == 9:
        return [1,1,1,1,0,1,1]
    else:
        return [0,0,0,0,0,0,0]

# expects a 7-segment input, returns the displayed digit or 10 as error code
def seg2num(display):
    if display == num2seg(0):
        return 0
    elif display == num2seg(1):
        return 1
    elif display == num2seg(2):
        return 2
    elif display == num2seg(3):
        return 3
    elif display == num2seg(4):
        return 4
    elif display == num2seg(5):
        return 5
    elif display == num2seg(6):
        return 6
    elif display == num2seg(7):
        return 7
    elif display == num2seg(8):
        return 8
    elif display == num2seg(9):
        return 9
    else:
        return 10
    

# counts activated segments in a segment number
def count_segments(seg_num):
    return a.array_sum(seg_num)

# checks whether segment number A contains segment number B
def contains_segment(seg_A, seg_B):
    result = True
    for i in range(7):
        if seg_A[i] == 0 and seg_B[i] == 1:
            result = False
    return result

# counts the occurence of a letter in a list of words
def count_letter_occurence(word_list, letter):
    count = 0
    for i in range(len(word_list)):
        for j in range(len(word_list[i])):
            if word_list[i][j] == letter:
                count += 1
    return count

# identifies the A-segment 
# the A-segment is contained in 7, but not in 1
def identify_A(segment_list):
    seven = ''
    one = ''
    output = ''
    for i in range(len(segment_list)):
        if len(segment_list[i]) == 3:
            seven = segment_list[i]
        elif len(segment_list[i]) == 2:
            one = segment_list[i]
    for i in range(3):
        found = False
        for j in range(2):
            if seven[i] == one[j]:
                found = True
        if not found:
            output = seven[i]
    return output

# identifies the B-segment 
# the B-segment is contained in 6 different digits
# no other segment is contained in that exact number of digits
def identify_B(segment_list):
    output = ''
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if count_letter_occurence(segment_list, letter) == 6:
            output = letter        
    return output

# identifies the C-segment 
# the C-segment is contained in 8 different digits
# This is not unique, but the other segment is A, 
# which we can identify elsewise
def identify_C(segment_list):
    candidates = []
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if count_letter_occurence(segment_list, letter) == 8:
            candidates += letter
    output = ''
    for candidate in candidates:
        if identify_A(segment_list) != candidate:
            output = candidate       
    return output

# identifies the D-segment 
# the D-segment is contained in 7 different digits
# This is not unique, but the other segment is G, 
# which we can identify elsewise
def identify_D(segment_list):
    candidates = []
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if count_letter_occurence(segment_list, letter) == 7:
            candidates += letter
    output = ''

    for candidate in candidates:
        if identify_G(segment_list) != candidate:
            output = candidate
    return output

# identifies the E-segment 
# the E-segment is contained in 4 different digits
# no other segment is contained in that exact number of digits
def identify_E(segment_list):
    output = ''
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if count_letter_occurence(segment_list, letter) == 4:
            output = letter        
    return output

# identifies the F-segment 
# the F-segment is contained in 9 different digits
# no other segment is contained in that exact number of digits
def identify_F(segment_list):
    output = ''
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if count_letter_occurence(segment_list, letter) == 9:
            output = letter        
    return output

# identifies the G-segment 
# the G-segment is contained in 7 different digits
# This is not unique, but out of the two candidates 
# it's the one not occuring in digits with less than 5 segments
# if we omit digits with less segments it is part of all 7
# while D, the other candidate, is only part of 6
def identify_G(segment_list):
    check_list = []
    for entry in segment_list:
        if len(entry) > 4:
            check_list.append(entry)
    # print(check_list)
    candidates = []
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if count_letter_occurence(check_list, letter) == 7:
            candidates.append(letter)
    output = ''
    for candidate in candidates:
        if identify_A(segment_list) != candidate:
            output = candidate
    return output
