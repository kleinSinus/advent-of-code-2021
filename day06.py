# file_name = "test06.txt"
file_name = "day06.txt"

# reads the input for the day's riddle
file = open("inputs/"+ file_name, "r")
input_data = [line[:-1] for line in file]
file.close()

output_text = 'Initial state:'
output_text += input_data[0]


lanternfish = input_data[0].split(',')
lanternfish_ages = [int(fish) for fish in lanternfish]

day_count = 0

reproduction= [0]*9
for fish in lanternfish_ages:
    reproduction[fish] += 1
# print(reproduction)

while day_count < 256:
    newborn = reproduction[0]
    # left shift
    for i in range(len(reproduction)-1):
        reproduction[i] = reproduction[i+1]
    reproduction[8] = 0
    # print(reproduction)
    # update newborns and new parents
    reproduction[6] += newborn
    reproduction[8] += newborn
    # print(reproduction)

    number_of_fishes = 0
    for fishes in reproduction:
       number_of_fishes += fishes

    # print(reproduction, number_of_fishes)
    day_count += 1



# less efficient way that solved part 1 but takes exponentially long on part two
# while day_count < 256:
#     newborn = 0
#     for i in range(len(lanternfish_ages)):
#         if lanternfish_ages[i] > 0:
#             lanternfish_ages[i] -= 1
#         else:
#             lanternfish_ages[i] = 6
#             newborn += 1
#     for j in range(newborn):
#         lanternfish_ages.append(8)
#     # if day_count < 9:
#     #     output_text += "\nAfter  " + str(day_count+1) + " days: " + str(lanternfish_ages)
#     #     output_text += " -> " + str(len(lanternfish_ages)) + " fishes"
#     # else:
#     #     output_text += "\nAfter " + str(day_count+1) + " days: " + str(lanternfish_ages)
#     #     output_text += " -> " + str(len(lanternfish_ages)) + " fishes"
#     print("Simulating fish reproduction, day " + str(day_count) + "/256") 
#     day_count += 1

output_text += "\n\n After " + str(day_count) + " days there are " + str(number_of_fishes) + " fishes"

# writes the output for the day's riddle
file = open("outputs/" + file_name, "w")
file.write(output_text)
file.close()
