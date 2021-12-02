import file_processor
import data_processor


def process_input_file(file_name):
    input_data = file_processor.get_data_from_file(file_name)
    output_strings = data_processor.process_measurements(input_data)
    output_count = data_processor.count_increments(input_data)
    file_processor.write_output_file("out_"+file_name, output_strings, output_count)


process_input_file("test.txt")
process_input_file("input.txt")
