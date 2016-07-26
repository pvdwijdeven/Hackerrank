def checkio(number):
    pigs = 1
    tot_pigs=1
    feed = 1
    while number > feed:
        pigs+=1
        tot_pigs+=pigs
        feed+=tot_pigs
        if feed>=number:
            if feed-number>pigs:
                return tot_pigs-pigs
            else:
                return tot_pigs-(feed-number)
    return feed


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
