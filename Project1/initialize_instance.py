import re

def read_file(file_name):
    s = open(file_name, 'r').read().split('\n')
    s = [re.findall(r'\d+', line) for line in s]
    s = [line for line in s if line]
    s = [[int(i) for i in line] for line in s]
    return s[0], s[1], s[2:]

prizes, penalties, costs = read_file("./Material-PCTSP/Instances/problem_100_100_100_1000.pctsp")

# # TODO: build adjacency list from adjancency matrix? (easier to find shortest path?)
