import statistics as stats
import numpy as np
import random


def find_median(r, s):
    # make r the longer array
    if len(s) > len(r):
        r_prime = [element for element in r]
        r = [element for element in s]
        s = r_prime
    # len(r)>len(s)
    # base case
    if len(s) < 3:
        # log(r) and happens once so does not change the order of the solution
        for element in s:
            r.append(element)
        r.sort()
        return stats.median(r)
    m = len(r)
    n = len(s)
    # Assumption: we have random access
    r_median = stats.median(r)
    s_median = stats.median(s)

    if r_median == s_median:
        return r_median
    # This one was a special case that was easier to handle separately
    if m % 2 == 0 and n % 2 == 0:
        if r_median > s_median:
            r_prime = r[:int(m - (n / 2) + 1)]
            s_prime = s[int((n / 2) - 1):]
            return find_median(r_prime, s_prime)
        else:
            r_prime = r[int((n / 2) - 1):]
            s_prime = s[: int((n / 2) + 1)]
            return find_median(r_prime, s_prime)
    #This is the general case
    if r_median > s_median:
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
    # the loop is for testing 1000 random cases
    for i in range(1000):
        # random length of r and s
        m = random.randint(3, 20)
        n = random.randint(3, 19)
        # filling r and s with random integers
        r = random.sample(range(10, 1000), m)
        s = random.sample(range(10, 1000), n)
        r.sort()
        s.sort()
        result = find_median(r, s)
        concat = np.concatenate((r, s))
        concat.sort()
        print(stats.median(concat) == result)
        if stats.median(concat) != result:
            break
    if i < 999:
        print("failed")
    else:
        print("success")
