import file_processor
import data_processor


def process_input_file(file_name, window_size):
    input_data = file_processor.get_data_from_file(file_name)
    window_data = data_processor.get_sum_window_data(input_data, window_size)
    output_strings = data_processor.process_measurements(window_data)
    output_count = data_processor.count_increments(window_data)
    file_processor.write_output_file("out" + str(window_size) + "_" + file_name, output_strings, output_count)


process_input_file("test.txt", 1)
process_input_file("input.txt", 1)
