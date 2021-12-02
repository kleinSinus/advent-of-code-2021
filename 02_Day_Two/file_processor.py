# simple file processor that can load and store text files

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
def write_output_file(file_name, output_text):
    file = open(file_name, "w")
    for line in output_text:
        file.write(line+"\n")
    file.close()
