import re

SIGMA = 0.5

def read_file(file_name):
    s = open(file_name, 'r').read().split('\n')
    s = [re.findall(r'\d+', line) for line in s]
    s = [line for line in s if line]
    s = [[int(i) for i in line] for line in s]
    return s[0], s[1], s[2:]

prizes, penalties, costs = read_file("./Material-PCTSP/Instances/problem_100_100_100_1000.pctsp")

# NOT CHECKED YET
def calculate_solution(solution, prizes, penalties, costs):
    my_prizes = [prizes[i] for i in solution]
    all_prizes = sum(prizes)
    missed = [i for i in range(len(prizes)) if i not in solution]
    my_penalties = [penalties[i] for i in missed]
    my_costs = [costs[solution[i]][solution[i+1]] \
                for i in range(len(solution)-1)] + \
                [costs[solution[-1]][solution[0]]]
    return sum(my_costs) + sum(my_penalties), (my_prizes >= SIGMA * all_prizes)
