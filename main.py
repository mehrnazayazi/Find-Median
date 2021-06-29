import statistics as stats
import numpy as np
import random


def find_median(r, s):
    if len(s) > len(r):
        r_prime = [element for element in r]
        r = [element for element in s]
        s = r_prime
    # len(r)>len(s)
    if len(s) < 3:
        # log(r) and happens once
        for element in s:
            r.append(element)
        r.sort()
        return stats.median(r)
    m = len(r)
    n = len(s)
    r_median = stats.median(r)
    s_median = stats.median(s)
    # alpha >beta
    if r_median == s_median:
        return r_median
    if m%2 == 0 and n%2 == 0:
        if r_median > s_median:
            r_prime = r[:int(m - (n / 2)+1)]
            s_prime = s[int((n / 2)-1):]
            return find_median(r_prime, s_prime)
        else:
            r_prime = r[int((n / 2)-1):]
            s_prime = s[: int((n / 2)+1)]
            return find_median(r_prime, s_prime)
    if r_median > s_median:
        # r is odd & s is odd
        if n % 2 == 1:
            r_prime = r[:int(m - ((n - 1) / 2))]
            s_prime = s[int(((n - 1) / 2)):]
            return find_median(r_prime, s_prime)
        else:
            r_prime = r[:int(m - (n / 2))]
            s_prime = s[int((n / 2)):]
            return find_median(r_prime, s_prime)
    else:
        if n % 2 == 1:
            r_prime = r[int((n - 1) / 2):]
            s_prime = s[:int((n + 1) / 2)]
            return find_median(r_prime, s_prime)
        else:
            r_prime = r[int(n / 2):]
            s_prime = s[: int(n / 2)]
            return find_median(r_prime, s_prime)


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    # assumption: r and s are both have len odd
    # r = [i for i in range(0, 17, 2)]
    # s = [i for i in range(1, 15, 2)]
    for i in range(1000):
        m = random.randint(3,20)
        n = random.randint(3,19)
        r = random.sample(range(10, 1000), m)
        s = random.sample(range(10, 1000), n)
        r.sort()
        s.sort()
        # r = [191, 330, 437, 539, 541, 556, 767, 956]
        # s =[109, 170, 390, 436, 673, 768, 823, 931]
        print(r)
        print(s)
        # Assumption : n>m
        result = find_median(r, s)
        print(result)
        concat = np.concatenate((r, s))
        concat.sort()
        print(concat)
        print(stats.median(concat))
        print(stats.median(concat) == result)
        if stats.median(concat) != result:
            break
    print(i)
