import lib.arrays
import lib.type_converter

def do_stuff(input_data, test_mode):
    data = [int(entry) for entry in input_data]
    data_win3 = lib.arrays.window_sums(data, 3)
    if test_mode :
        output_text = "PART ONE\n========\n\n"
        output_text += get_increment_table(data)
        output_text += "\nPART TWO\n========\n\n"
        output_text += get_increment_table(data_win3)
    else:
        output_text = "PART ONE\n========\n\n"
        output_text += "In this example, there are "
        output_text += str(lib.arrays.count_increments(data))
        output_text += " measurements that are larger than the previous measurement."
        output_text += "\n\n\nPART TWO\n========\n\n"
        output_text += "In this example, there are "
        output_text += str(lib.arrays.count_increments(data_win3))
        output_text += " sums that are larger than the previous sum."
    return output_text

def get_increment_table(data):
    table = ""
    increments = lib.arrays.pairwise_compare(data)
    for i in range(len(data)):
        if i == 0:
            table += lib.type_converter.int2label(i) + ": " + str(data[0]) + " (N/A - no previous measurement)\n"
        elif increments[i] == 0:
            table += lib.type_converter.int2label(i) + ": " + str(data[i]) + " (no change)\n"
        elif increments[i] == 1:
            table += lib.type_converter.int2label(i) + ": " + str(data[i]) + " (increased)\n"
        elif increments[i] == -1:
            table += lib.type_converter.int2label(i) + ": " + str(data[i]) + " (decreased)\n"
    return table