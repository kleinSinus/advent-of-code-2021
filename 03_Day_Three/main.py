import file_processor
import data_processor


def process_input_file(file_name):
    input_data = file_processor.get_data_from_file("inout/"+file_name)
    # TODO: DO stuff!!!
    file_processor.write_output_file("inout/out_" + file_name, output_text)


process_input_file("test.txt")
process_input_file("input.txt")
