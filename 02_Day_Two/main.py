import file_processor
import data_processor


def process_input_file(file_name):
    input_data = file_processor.get_data_from_file(file_name)
    # TODO: Solve problem
    output_text = ['']
    file_processor.write_output_file("out_" + file_name, output_text)


process_input_file("input_output/test.txt")
process_input_file("input_output/input.txt")
