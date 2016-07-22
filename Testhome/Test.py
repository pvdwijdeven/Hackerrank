def four_on_a_row(rows):
    found = []
    for x in rows:
        for y in x:
            if found == []:
                found.append(y)
            else:
                if found[0] == y:
                    found.append(y)
                else:
                    found = [y]
            if len(found) >= 4: return True
    return False


def checkio(matrix):
    # replace this for solution
    columns = [[] for x in xrange(len(matrix[0]))]
    diag1 = [[] for x in xrange(len(matrix) - 3)]
    diag2 = [[] for x in xrange(len(matrix) - 3)]
    for i, x in enumerate(matrix):
        for j, y in enumerate(matrix):
            columns[j].append(matrix[i][j])
    if four_on_a_row(columns):
        return True
    if four_on_a_row(matrix):
        return True
    for x in xrange(len(matrix)):
        for y in xrange(len(matrix)):
            found = []
            i = x
            j = y
            while i <= len(matrix) - 1 and j <= len(matrix) - 1:
                if found == []:
                    found.append(matrix[i][j])
                else:
                    if found[0] == matrix[i][j]:
                        found.append(found[0])
                    else:
                        found = [matrix[i][j]]
                i += 1
                j += 1
                if len(found) >= 4: return True
    for x in xrange(len(matrix)):
        for y in xrange(len(matrix)):
            found = []
            i = x
            j = y
            while i <= len(matrix) - 1 and j >= 0:
                if found == []:
                    found.append(matrix[i][j])
                else:
                    if found[0] == matrix[i][j]:
                        found.append(found[0])
                    else:
                        found = [matrix[i][j]]
                i += 1
                j -= 1
                if len(found) >= 4:
                    print found
                    return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #print  checkio([[7,1,1,8,1,1],[1,1,7,3,1,5],[2,3,1,2,5,1],[1,1,1,5,1,4],[4,6,5,1,3,1],[1,1,9,1,2,1]])


    # assert checkio([
    #     [1, 2, 1, 1],
    #     [1, 1, 4, 1],
    #     [4, 3, 1, 6],
    #     [1, 7, 2, 1]
    # ]) == True, "Vertical"
    # assert checkio([
    #     [7, 1, 4, 1],
    #     [1, 2, 5, 2],
    #     [3, 4, 1, 3],
    #     [1, 1, 8, 1]
    # ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [1, 1, 1, 3, 1],
        [1, 5, 6, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    # assert checkio([
    #     [7, 1, 1, 8, 1, 1],
    #     [1, 1, 7, 3, 1, 5],
    #     [2, 4, 1, 1, 5, 1],
    #     [1, 4, 1, 5, 1, 4],
    #     [4, 6, 5, 1, 3, 1],
    #     [1, 1, 9, 1, 2, 1]
    # ]) == True, "Diagonal"
