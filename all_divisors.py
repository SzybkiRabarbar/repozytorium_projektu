'''
https://blog.finxter.com/how-to-get-all-divisors-of-a-number-in-python/
'''
def divisors(n):
    result = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
    return list(result)
print(divisors(24))