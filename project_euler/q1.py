"""
Multiples of 3 and 5
https://projecteuler.net/problem=1
"""

print("------------------------------")
print("Solution 1 - Iteration")

def sum_multiples_iter(n):
    sum = 0
    for i in range(n):
        if not (i % 5) or not (i % 3):
            sum += i
    return sum


print("------------------------------")
print("Solution 2 - Algebraic")

def sum_multiples(n, factor):
    # use the summation identity for sum from k = 1 to n of k
    max_mult = (n - 1) // factor
    return factor*max_mult*(max_mult+1) / 2

def sum_all_multiples(n):
    sum = 0
    for i in (3, 5):
        sum += sum_multiples(n, i)
    # subtracting the common multiples
    sum -= sum_multiples(n, 3*5)
    return sum

if __name__ == "__main__":
    n = 1000
    print(sum_multiples_iter(n))
    print(sum_all_multiples(n))