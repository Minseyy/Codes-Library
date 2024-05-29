def split_problems(problems):
    split_prob = []
    for problem in problems:
        parts = problem.split()
        split_prob.append(parts)
    return split_prob


def validate_problems(split_prob):
    for i in range(len(split_prob)):

        if not split_prob[i][0].isdigit() or not split_prob[i][2].isdigit():
            return "Error: Numbers must only contain digits."

        if len(split_prob[i][0]) > 4 or len(split_prob[i][2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if split_prob[i][1] not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
    return None


def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        print("Error: Too many problems.")

    split_prob = split_problems(problems)
    not_Valid = validate_problems(split_prob)
    if not_Valid:
        return not_Valid

    first_line = ""
    sec_line = ""
    dashes = ""
    answers = ""

    for each in split_prob:
        num1 = each[0]
        operator = each[1]
        num2 = each[2]

        max_len = max(len(num1), len(num2)) + 2

        first_line += num1.rjust(max_len) + '    '
        sec_line += operator + num2.rjust(max_len - 1) + '    '
        dashes += '-' * max_len + '    '

        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))

            answers += result.rjust(max_len) + '    '

    arranged_line = f"{first_line.rstrip()}\n{sec_line.rstrip()}\n{dashes.rstrip()}"

    if show_answers:
        arranged_line += f"\n{answers.rstrip()}"

    return arranged_line


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')
