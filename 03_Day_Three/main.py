import file_processor
import data_processor


def process_input_file(file_name):
    input_data = file_processor.get_data_from_file("inout/"+file_name)
    gamma = data_processor.compute_gamma_rate(input_data)
    epsilon = data_processor.compute_epsilon_rate(gamma)
    output_text = data_processor.gen_output(gamma, epsilon)
    file_processor.write_output_file("inout/out_" + file_name, output_text)


process_input_file("test.txt")
process_input_file("input.txt")
