# import lib

def do_stuff(input_data, test_mode):
    if test_mode :
        output_text = "PART ONE\n========\n\n"
        template = input_data[0]
        del input_data[0]
        del input_data[0]
        # print(input_data)
        rules = [line.split(" -> ") for line in input_data]
        # print(rules)
        output_text += "Template:     " + template + "\n"
        result = template
        for i in range(4):
            output_text += "After step " + str(i+1) + ": "
            result = pair_insertion(result, rules)
            output_text += result + "\n"
        for i in range(6):
            output_text += "Result length after step " + str(i+5) + ": "
            result = pair_insertion(result, rules)
            output_text += str(len(result)) + "\n"
        output_text += "\nAfter step 10:\n"
        counts = element_counting(result)
        for count in counts:
            output_text += "- " + count[0] + " occurs " + str(count[1]) + " times\n"
        output_text += "\nTaking the quantity of the most common element "
        output_text += "(" + most_common(counts)[0] + ", " +  str(most_common(counts)[1]) + ")"
        output_text += "\nand subtracting the quantity of the least common element "
        output_text += "(" + least_common(counts)[0] + ", " +  str(least_common(counts)[1]) + ")"
        output_text += "\nproduces " + str(most_common(counts)[1]) + " - " + str(least_common(counts)[1])
        output_text += " = " + str(most_common(counts)[1] - least_common(counts)[1]) + "."
        output_text += "\n\nPART TWO\n========\n\n"
        for i in range(30):
            print(i+10)
            result = pair_insertion(result, rules)
        output_text += "Result length after step 40: "
        output_text += str(len(result)) + "\n"
        counts = element_counting(result)
        for count in counts:
            output_text += "- " + count[0] + " occurs " + str(count[1]) + " times\n"
        output_text += "\nTaking the quantity of the most common element "
        output_text += "(" + most_common(counts)[0] + ", " +  str(most_common(counts)[1]) + ")"
        output_text += "\nand subtracting the quantity of the least common element "
        output_text += "(" + least_common(counts)[0] + ", " +  str(least_common(counts)[1]) + ")"
        output_text += "\nproduces " + str(most_common(counts)[1]) + " - " + str(least_common(counts)[1])
        output_text += " = " + str(most_common(counts)[1] - least_common(counts)[1]) + "."
    else:
        output_text = "PART ONE\n========\n\n"
        template = input_data[0]
        del input_data[0]
        del input_data[0]
        rules = [line.split(" -> ") for line in input_data]
        output_text += "Template: " + template + "\n"
        result = template
        for i in range(10):
            output_text += "Result length after step " + str(i+1) + ": "
            result = pair_insertion(result, rules)
            output_text += str(len(result)) + "\n"
        output_text += "\nAfter step 10:\n"
        counts = element_counting(result)
        for count in counts:
            output_text += "- " + count[0] + " occurs " + str(count[1]) + " times\n"
        output_text += "\nTaking the quantity of the most common element "
        output_text += "(" + most_common(counts)[0] + ", " +  str(most_common(counts)[1]) + ")"
        output_text += "\nand subtracting the quantity of the least common element "
        output_text += "(" + least_common(counts)[0] + ", " +  str(least_common(counts)[1]) + ")"
        output_text += "\nproduces " + str(most_common(counts)[1]) + " - " + str(least_common(counts)[1])
        output_text += " = " + str(most_common(counts)[1] - least_common(counts)[1]) + "."
        output_text += "\n\n\nPART TWO\n========\n\n"
        # TODO: Generate summarized output for part 2
    return output_text

def pair_insertion(polymer, rules):
    print(len(polymer))
    polymer_new = ''
    for i in range(len(polymer)-1):
        current_pair = polymer[i] + polymer[i+1]
        found = False
        for rule in rules:
            if rule[0] == current_pair:
                found = True
                if found:
                    polymer_new += polymer[i] + rule[1]
        if not found:
            polymer_new += polymer[i]
    polymer_new += polymer[-1]
    return polymer_new

def element_counting(polymer):
    polymer_copy = polymer
    elements = []
    for element in polymer_copy:
        tracked = False
        for i in range(len(elements)):
            if elements[i][0] == element:
                tracked = True
                elements[i][1] += 1
        if not tracked:
            elements.append([element, 1])
    print(elements)
    return elements

def most_common(counts):
    max_element = counts[0][0]
    max_count = counts[0][1]
    for element in counts:
        if element[1] > max_count:
            max_element = element[0]
            max_count = element[1]
    return max_element, max_count

def least_common(counts):
    min_element = counts[0][0]
    min_count = counts[0][1]
    for element in counts:
        if element[1] < min_count:
            min_element = element[0]
            min_count = element[1]
    return min_element, min_count