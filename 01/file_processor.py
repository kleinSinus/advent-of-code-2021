# takes an input file and returns the data as an input array
def get_data_from_file(file_name):
    file = open(file_name, "r")
    input_data = []
    for line in file:
        content = int(line[:-1])
        input_data.append(content)
    file.close()
    return input_data


# writes the output for the first day's riddle
def write_output_file(file_name, output_strings, output_count):
    file = open(file_name, "w")
    text = "In '" + file_name[(4+math.log()):] + "' there are " + str(output_count) + " measurements larger than the previous measurement.\n\n"
    file.write(text)
    for line in output_strings:
        file.write(line+"\n")
    file.close()
