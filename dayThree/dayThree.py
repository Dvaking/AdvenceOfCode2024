import re


def extractAndMultiply(memory_string):
    pattern = re.compile(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))')

    total_sum = 0
    mul_enabled = True

    matches = pattern.findall(memory_string)

    for match in matches:
        if match.startswith("do()"):
            mul_enabled = True
        elif match.startswith("don't()"):
            mul_enabled = False
        elif match.startswith("mul") and mul_enabled:
            numbers = re.findall(r'\d+', match)
            if len(numbers) == 2:
                x, y = int(numbers[0]), int(numbers[1])
                total_sum += x * y

    return total_sum


def formatFileInList():
    file_path = './data2.txt'
    memory_string = ""
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    memory_string += line
        return memory_string
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'a pas été trouvé.")
        return ""


memory_string = formatFileInList()
if memory_string:
    print(extractAndMultiply(memory_string))
