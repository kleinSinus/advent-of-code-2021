import file_processor
import data_processor

date = 7
test_mode = True
valid_date = True

if date < 10:
    if test_mode:
        file_name = "test0" + str(date) + ".txt"
    else:
        file_name = "day0" + str(date) + ".txt"
elif date < 26:
    if test_mode:
        file_name = "test" + str(date) + ".txt"
    else:
        file_name = "day" + str(date) + ".txt"
else:
    valid_date = False

if valid_date:
    input_data = file_processor.get_data_from_file("inputs/" + file_name)
    output_text = data_processor.gen_output(input_data, date, test_mode)
    file_processor.write_output_file("outputs/" + file_name, output_text)
else:
    print("Not a valid input date")