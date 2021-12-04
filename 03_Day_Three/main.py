import file_processor
import data_processor


def process_input_file(file_name):
    input_data = file_processor.get_data_from_file("inout/"+file_name)
    gamma = data_processor.compute_gamma_rate(input_data)
    epsilon = data_processor.compute_epsilon_rate(gamma)
    oxy_gen = data_processor.compute_oxygen_generator_rating(input_data)
    co2_scrub = data_processor.compute_co2_scrubber_rating(input_data)
    output_text = data_processor.gen_output(gamma, epsilon, oxy_gen, co2_scrub)
    file_processor.write_output_file("inout/out_" + file_name, output_text)


process_input_file("test.txt")
process_input_file("input.txt")
