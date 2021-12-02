import file_processor
import data_processor


def process_input_file(file_name):
    input_data = file_processor.get_data_from_file("input_output/"+file_name)
    submarine_position = data_processor.process_movement(input_data)  # compute the position of the submarine
    output_x_position = "\n    Horizontal: " + str(submarine_position[0])
    output_y_position = "\n    Depth: " + str(submarine_position[1])
    output_xy = "\n\nMultiplied value: " + str(submarine_position[0]*submarine_position[1])
    output_text = "Submarine Position:" + output_x_position + output_y_position + output_xy
    file_processor.write_output_file("input_output/out_" + file_name, output_text)


process_input_file("test.txt")
process_input_file("input.txt")
