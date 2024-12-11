


def isSafe(number):
    differences = [abs(number[i] - number[i + 1])
                   for i in range(len(number) - 1)]
    if all(number[i] > number[i + 1] for i in range(len(number) - 1)) or all(number[i] < number[i + 1] for i in range(len(number) - 1)):
        return all(1 <= diff <= 3 for diff in differences)
    return False


def countSafeReport(reports):
    safe_count = sum(isSafe(number) for number in reports)
    return safe_count


def isSafeWithTolerance(numbers):
    if isSafe(numbers):
        return True

    for i in range(len(numbers)):
        modified_number = numbers[:i] + numbers[i + 1:]
        if isSafe(modified_number):
            return True

    return False


def countSafeReportWithTolerence(numbers):
    safe_count = sum(isSafeWithTolerance(number) for number in numbers)
    return safe_count


def formatFileInList():
    file_path = './data.txt'
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    numbers.append([int(num) for num in line.split()])
        return numbers
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'a pas été trouvé.")
        return []


num = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]

numbers = formatFileInList()
if numbers:
    print(countSafeReport(numbers))
    print(countSafeReportWithTolerence(numbers))
