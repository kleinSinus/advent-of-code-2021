# import lib

def do_stuff(input_data, test_mode):
    if test_mode :
        output_text = "PART ONE\n========\n\n"
        error_count = 0
        error_score = 0
        completion_scores = []
        for line in input_data:
            stack_or_error = check_brackets(line)[0]
            error_source = check_brackets(line)[1]
            if error_source != "":
                error_count += 1
            completion_string = get_completion_string(stack_or_error)
            output_text += stack_or_error
            if error_source != "":
                output_text += "-> ERROR " + str(get_error_score(error_source)) + "\n"
            else:
                output_text += "-> COMPLETION with " + get_completion_string(stack_or_error) + ": " + str(get_completion_score(completion_string)) + "\n"
                completion_scores.append(get_completion_score(completion_string))
            error_score += get_error_score(error_source)
        output_text += "\nThere are " + str(error_count) + " erroneous lines in the current input file."
        output_text += "\nThe error score for the current file is " + str(error_score) + "."
        output_text += "\n\nPART TWO\n========\n\n"
        completion_scores = sorted(completion_scores)
        output_text += "The middle completion score for the remaining " + str(len(input_data)-error_count) + " lines is " + str(completion_scores[int((len(completion_scores)-1)/2)]) + "."
    else:
        output_text = "PART ONE\n========\n\n"
        error_score = 0
        error_count = 0
        completion_scores = []
        for line in input_data:
            stack_or_error = check_brackets(line)[0]
            error_source = check_brackets(line)[1]
            if error_source != "":
                error_count += 1
            else:
                completion_string = get_completion_string(stack_or_error)
                completion_scores.append(get_completion_score(completion_string))
            error_score += get_error_score(check_brackets(line)[1])
        output_text += "\nThere are " + str(error_count) + " erroneous lines in the current input file."
        output_text += "\nThe error score for the current file is " + str(error_score) + "."
        output_text += "\n\nPART TWO\n========\n\n"
        completion_scores = sorted(completion_scores)
        output_text += "The middle completion score for the remaining " + str(len(input_data)-error_count) + " lines is " + str(completion_scores[int((len(completion_scores))/2)]) + "."
    return output_text

def check_brackets(input_string):
    bracket_stack = ''
    for i in range(len(input_string)):
        if input_string[i] == '(' or input_string[i] == '[' or input_string[i] == '{' or input_string[i] == '<':
            bracket_stack += input_string[i]
        elif input_string[i] == ')':
            if bracket_stack[-1] != '(':
                return " - Expected " + get_closing_bracket(bracket_stack[-1]) + ", but found " + input_string[i] + " instead.", input_string[i]
            else:
                bracket_stack = bracket_stack[:-1]
        elif input_string[i] == ']':
            if bracket_stack[-1] != '[':
                return " - Expected " + get_closing_bracket(bracket_stack[-1]) + ", but found " + input_string[i] + " instead.", input_string[i]
            else:
                bracket_stack = bracket_stack[:-1]
        elif input_string[i] == '}':
            if bracket_stack[-1] != '{':
                return " - Expected " + get_closing_bracket(bracket_stack[-1]) + ", but found " + input_string[i] + " instead.", input_string[i]
            else:
                bracket_stack = bracket_stack[:-1]
        elif input_string[i] == '>':
            if bracket_stack[-1] != '<':
                return " - Expected " + get_closing_bracket(bracket_stack[-1]) + ", but found " + input_string[i] + " instead.", input_string[i]
            else:
                bracket_stack = bracket_stack[:-1]
    return bracket_stack, ""

def get_closing_bracket(bracket):
    if bracket == '(':
        return ')'
    elif bracket == '[':
        return ']'
    elif bracket == '{':
        return '}'
    elif bracket == '<':
        return '>'
    else:
        return "Input ERROR"

def get_error_score(bracket):
    if bracket == ')':
        return 3
    elif bracket == ']':
        return 57
    elif bracket == '}':
        return 1197
    elif bracket == '>':
        return 25137
    else:
        return 0

def get_completion_value(bracket):
    if bracket == ')':
        return 1
    elif bracket == ']':
        return 2
    elif bracket == '}':
        return 3
    elif bracket == '>':
        return 4
    else:
        return 0

def get_completion_score(stack):
    score = 0
    for i in range(len(stack)):
        score *= 5
        score += get_completion_value(stack[i])
    return score

def get_completion_string(stack):
    stack_reversed = stack[::-1]
    completion_string = ''
    for i in range(len(stack)):
        completion_string += (get_closing_bracket(stack_reversed[i]))
    return completion_string
