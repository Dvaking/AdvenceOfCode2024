from collections import defaultdict, deque


def parseRules(rules):
    order_rules = defaultdict(set)
    for rule in rules:
        x, y = map(int, rule.split('|'))
        order_rules[y].add(x)
    return order_rules


def isCorrectOrder(pages, order_rules):
    for i in range(len(pages)):
        for j in range(i + 1, len(pages)):
            if pages[j] in order_rules[pages[i]]:
                return False
    return True


def middlePageNumber(pages):
    n = len(pages)
    return pages[n // 2] if n % 2 != 0 else pages[n // 2 - 1]


def sumMiddlePageNumbers(rules, updates):
    order_rules = parseRules(rules)
    total_sum = 0

    for update in updates:
        pages = list(map(int, update.split(',')))
        if isCorrectOrder(pages, order_rules):
            total_sum += middlePageNumber(pages)

    return total_sum


def parseFile(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    rules_section, updates_section = content.strip().split('\n\n')
    rules = rules_section.split('\n')
    updates = updates_section.split('\n')

    return rules, updates


def parseRulesTwo(rules):
    order_rules = defaultdict(set)
    for rule in rules:
        x, y = map(int, rule.split('|'))
        order_rules[y].add(x)
    return order_rules


def isCorrectOrderTwo(pages, order_rules):
    for i in range(len(pages)):
        for j in range(i + 1, len(pages)):
            if pages[j] in order_rules[pages[i]]:
                return False
    return True


def topologicalSort(pages, order_rules):
    indegree = {page: 0 for page in pages}
    graph = defaultdict(list)

    for y in pages:
        for x in order_rules[y]:
            if x in pages:
                graph[x].append(y)
                indegree[y] += 1

    queue = deque([node for node in pages if indegree[node] == 0])
    sorted_pages = []

    while queue:
        node = queue.popleft()
        sorted_pages.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages


def middlePageNumber(pages):
    n = len(pages)
    return pages[n // 2] if n % 2 != 0 else pages[n // 2 - 1]


def sumMiddlePageNumbersIncorrectUpdates(rules, updates):
    order_rules = parseRulesTwo(rules)
    total_sum = 0

    for update in updates:
        pages = list(map(int, update.split(',')))
        if not isCorrectOrderTwo(pages, order_rules):
            sorted_pages = topologicalSort(pages, order_rules)
            total_sum += middlePageNumber(sorted_pages)

    return total_sum

# Example


file_path = './data.txt'
rules, updates = parseFile(file_path)

exempleRules = [
    "47|53", "97|13", "97|61", "97|47", "75|29", "61|13", "75|53",
    "29|13", "97|29", "53|29", "61|53", "97|53", "61|29", "47|13",
    "75|47", "97|75", "47|61", "75|61", "47|29", "75|13", "53|13"
]

exempleUpdates = [
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47"
]

print(sumMiddlePageNumbers(rules, updates))
print(sumMiddlePageNumbersIncorrectUpdates(rules, updates))
