import file_processor
import data_processor


def process_input_file(file_name):
    input_data = file_processor.get_data_from_file("inputs/"+file_name)
    output_text = data_processor.gen_output(input_data)
    file_processor.write_output_file("outputs/" + file_name, output_text)


process_input_file("test.txt")
process_input_file("input.txt")
