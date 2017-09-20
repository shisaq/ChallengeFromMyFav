def run():
    height = 3
    queueList = [1, 4, 7]
    challenge2_2(height, queueList)

def challenge2_2(h, q):
    result = []
    for i in q:
        if (i < 2**h - 1):
            result.append(calc(i))
        else:
            result.append(-1)
    print result

def calc(i):
    # ref: https://stackoverflow.com/a/20457938/5769598
    count = 0
    while( i & (i+1) !=0 and (i+1) & (i+2) != 0):
        mid_num = mask_off(i, upper_bit(i))
        count += i - mid_num
        i = mid_num
    if (i & (i+1)) == 0:
        return i * 2 + 1 + count
    elif ((i+1) & (i+2)) == 0:
        return i + 1 + count

# Clear most-significant non-zero bit
# ref: https://stackoverflow.com/a/20200778/5769598
def upper_bit(x):
    while x & (x - 1):
        x &= x - 1
    return x

def mask_off(x, mask):
    return (x & ~mask) + 1

if __name__ == '__main__':
    run()
