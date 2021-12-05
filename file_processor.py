# simple file processor that can load and store text files

# takes an input file and returns the data as an input array of strings
def get_data_from_file(file_name):
    file = open(file_name, "r")
    input_data = [line[:-1] for line in file]
    file.close()
    return input_data


# writes the output for the first day's riddle
def write_output_file(file_name, output_text):
    file = open(file_name, "w")
    file.write(output_text)
    file.close()
