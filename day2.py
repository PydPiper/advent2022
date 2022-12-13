'''
score:
6 = win
0 = lose
3 = tie
1 = rock, A, X
2 = paper, B, Y
3 = scissor, C, Z
'''

def part1():
    score = 0
    # there are 3*3 combinations
    lose = 0
    win = 6
    tie = 3
    rock = 1
    paper = 2
    scissor = 3
    score_dict = {
        'A X': tie + rock,
        'A Y': win + paper,
        'A Z': lose + scissor,
        'B X': lose + rock,
        'B Y': tie + paper,
        'B Z': win + scissor,
        'C X': win + rock,
        'C Y': lose + paper,
        'C Z': tie + scissor,
    }
    with open('day2.data', 'r') as f:
        for line in f:
            score += score_dict[line.strip()]

    print(f'Game score is {score}')

def part2():
    score = 0
    # there are 3*3 combinations
    # X need to lose
    # Y need to tie
    # Z need to win
    lose = 0
    win = 6
    tie = 3
    rock = 1
    paper = 2
    scissor = 3
    score_dict = {
        'A X': lose + scissor,
        'A Y': tie + rock,
        'A Z': win + paper,
        # interesting this was the same
        'B X': lose + rock,
        'B Y': tie + paper,
        'B Z': win + scissor,
        'C X': lose + paper,
        'C Y': tie + scissor,
        'C Z': win + rock,
    }
    with open('day2.data', 'r') as f:
        for line in f:
            score += score_dict[line.strip()]

    print(f'Game score is {score}')

if __name__ == '__main__':
    part1()
    part2()