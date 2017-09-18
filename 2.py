def run():
    theList = [2, 2]
    print challenge2(theList)

def challenge2(l):
    # descend the list and sum the list
    l.sort()
    total = sum(l)
    if total % 3 == 0:
        # no need to delete any item
        return intifyResult(l)
    else:
        for i in l[:]:
            # try removing the from the smallest and devided by 3 again
            # we should delete an item whose remainder is 1 or 2,
            # then the sum can be devided by 3.
            if (total - i) % 3 == 0:
                l.remove(i)
                return intifyResult(l)
        # all items that cannot devided by 3 have the same remainder,
        # that's why removing 1 item is not working.
        # so we need to delete 2 smallest items whose remainder are
        # not 0
        x = 0
        for i in l[:]:
            if i % 3 != 0 and x < 2:
                l.remove(i)
                x += 1
        return intifyResult(l)

def intifyResult(resultList):
    try:
        result = ''.join(str(e) for e in reversed(resultList))
        return int(result)
    except ValueError:
        # this means no value matches, return 0
        return 0

if __name__ == '__main__':
    run()
