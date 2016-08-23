from random import randint

CH_actions = ['E3', 'JAIL', 'C1', 'GO', 'H2', 'R1', 'NEXT R', 'NEXT R', 'NEXT U', '-3', 'STAY', 'STAY', 'STAY',
              'STAY', 'STAY', 'STAY']

CC_actions = ['STAY', 'JAIL', 'STAY', 'STAY', 'GO', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY', 'STAY',
              'STAY', 'STAY', 'STAY']

dict_board = {0: 'GO', 1: 'A1', 2: 'CC1', 3: 'A2', 4: 'T1', 5: 'R1', 6: 'B1', 7: 'CH1', 8: 'B2', 9: 'B3', 10: 'JAIL',
              11: 'C1', 12: 'U1', 13: 'C2', 14: 'C3', 15: 'R2', 16: 'D1', 17: 'CC2', 18: 'D2', 19: 'D3', 20: 'FP',
              21: 'E1', 22: 'CH2', 23: 'E2', 24: 'E3', 25: 'R3', 26: 'F1', 27: 'F2', 28: 'U2', 29: 'F3', 30: 'G2J',
              31: 'G1', 32: 'G2', 33: 'CC3', 34: 'G3', 35: 'R4', 36: 'CH3', 37: 'H1', 38: 'T2', 39: 'H2'}

dict_board_back = {'GO': 0, 'A1': 1, 'CC1': 2, 'A2': 3, 'T1': 4, 'R1': 5, 'B1': 6, 'CH1': 7, 'B2': 8, 'B3': 9,
                   'JAIL': 10, 'C1': 11, 'U1': 12, 'C2': 13, 'C3': 14, 'R2': 15, 'D1': 16, 'CC2': 17, 'D2': 18,
                   'D3': 19, 'FP': 20, 'E1': 21, 'CH2': 22, 'E2': 23, 'E3': 24, 'R3': 25, 'F1': 26, 'F2': 27, 'U2': 28,
                   'F3': 29, 'G2J': 30, 'G1': 31, 'G2': 32, 'CC3': 33, 'G3': 34, 'R4': 35, 'CH3': 36, 'H1': 37,
                   'T2': 38, 'H2': 39}


def get_action(current):
    current = dict_board[current]
    if current == "CC1" or current == "CC2" or current == "CC3":
        x = randint(0, 15)
        action = CC_actions[x]
    elif current == "CH1" or current == "CH2" or current == "CH3":
        x = randint(0, 15)
        action = CH_actions[x]
    elif current == "G2J":
        action = 'JAIL'
    else:
        action = 'STAY'
    return action


def get_new_pos(action, pos):
    if action in dict_board_back:
        return dict_board_back[action]
    elif action == 'STAY':
        return pos
    elif action == 'NEXT R':
        if pos < 4 or pos > 35:
            pos = 5
        elif 5 < pos < 15:
            pos = 15
        elif 15 < pos < 25:
            pos = 25
        elif 25 < pos < 35:
            pos = 35
        return pos
    elif action == 'NEXT U':
        if 12 < pos <= 27:
            return 28
        else:
            return 12
    elif action == "-3":
        pos -= 3
        if pos < 0:
            pos += 40
        if pos == 33:
            pos = get_new_pos(get_action(pos), pos)
        return pos
    else:
        exit("unknown action found: %s" % action)


def test(max_range):
    pos = 0

    result = [[0, dict_board[x]] for x in xrange(40)]
    n, k = map(int, raw_input().split())
    for x in xrange(max_range):
        d1 = randint(0, n - 1)
        d2 = randint(0, n - 1)
        pos += d1 + d2
        pos %= 40
        pos = get_new_pos(get_action(pos), pos)
        result[pos][0] += 1
    # print result
    result.sort(key=lambda z: z[0], reverse=True)
    my_res = result[:k]
    for x in my_res:
        print x[1],


test(1000000)
