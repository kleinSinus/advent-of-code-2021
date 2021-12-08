import math as m
import lib.arrays as a 
import lib.type_converter as tc

def do_stuff(input_data, test_mode):
    if test_mode :
        output_text = "PART ONE\n========\n\n"
        crab_positions = tc.csv2intlist(input_data[0])
        compare_pos2 = dist_crabs_pos(crab_positions, 2)
        compare_costs = combined_steps_to_pos(crab_positions)
        for i in range(len(crab_positions)):
            output_text += "  - Move from " + str(crab_positions[i]) + " to 2: " + str(compare_pos2[i]) + "\n"
        output_text += "\nThis costs a total of " + str(a.array_sum(compare_pos2)) + " fuel. "
        output_text += "This is the cheapest possible outcome;"
        output_text += "\nmore expensive outcomes include aligning at position 1 (" + str(compare_costs[1]) + " fuel),"
        output_text += "\nposition 3 (" + str(compare_costs[3]) + " fuel),"
        output_text += " or position 10 (" + str(compare_costs[10]) + " fuel)."
        output_text += "\n\nPART TWO\n========\n\n"
        output_text += "Fuel cost = Distance was wrong, best horizontal position in this"
        output_text += " is actually 5:\n\n"
        compare_pos5 = dist_crabs_pos(crab_positions, 5)
        for i in range(len(compare_pos5)):
            compare_pos5[i] = gauss_sum(compare_pos5[i])
        compare_dists = combined_steps_to_pos(crab_positions)
        print(compare_dists)
        compare_costs = fuel_cost(crab_positions)
        print(compare_costs)
        for i in range(len(crab_positions)):
            output_text += "  - Move from " + str(crab_positions[i]) + " to 2: " + str(compare_pos5[i]) + "\n"
        output_text += "\nThis costs a total of " + str(a.array_sum(compare_pos5)) + " fuel. "
        output_text += "This is the cheapest possible outcome;"
        output_text += "\nthe old alignment position (2) costs " + str(compare_costs[2]) + " fuel instead."
    else:
        output_text = "PART ONE\n========\n\n"
        crab_positions = tc.csv2intlist(input_data[0])
        compare_costs = combined_steps_to_pos(crab_positions)
        min_cost = min(compare_costs)
        for i in range(len(compare_costs)):
            if compare_costs[i] == min_cost:
                output_text += "Minimum cost of " + str(min_cost)
                output_text += " fuel at position " + str(i) + "."
        output_text += "\n\nPART TWO\n========\n\n"
        compare_costs = fuel_cost(crab_positions)
        min_cost = min(compare_costs)
        for i in range(len(compare_costs)):
            if compare_costs[i] == min_cost:
                output_text += "Minimum cost of " + str(min_cost)
                output_text += " fuel at position " + str(i) + "."
    return output_text

# takes list of horizontal crab positions, 
# returns list of their respective distance to an aimed at horizontal position
def dist_crabs_pos(crabs, pos):
    result = [0] * len(crabs)
    for i in range(len(crabs)):
        result[i] = int(m.fabs(crabs[i] - pos))
    return result

# gets the initially assumed cost for all horizontal positions within the range of the crabs positions
def combined_steps_to_pos(crabs):
    max_aim = max(crabs)
    fuel_costs = [0] * max_aim
    for pos in range(max_aim):
        fuel_costs[pos] = a.array_sum(dist_crabs_pos(crabs, pos))
    return fuel_costs

# gets the cost for all horizontal positions within the range of the crabs positions
def fuel_cost(crabs):
    max_aim = max(crabs)
    fuel_costs = [0] * max_aim
    for pos in range(max_aim):
        distances = dist_crabs_pos(crabs, pos)
        for i in range(len(distances)):
            distances[i] = gauss_sum(distances[i])
        fuel_costs[pos] = a.array_sum(distances)
    return fuel_costs

# returns sum of 1+...+i
def gauss_sum(i):
    return int((i+1)*i/2)