
def fizz_buzz(val, tests):
    ret_str = ''
    
    for key, divisor in tests:
        ret_str += key if val % divisor == 0 else ''

    return ret_str if len(ret_str) != 0 else val

if __name__ == "__main__":
    
    tests = [
                ('Fizz', 3),
                ('Buzz', 5),
                ('Bizz', 6)
            ]

    for i in range(100 + 1):
        print(fizz_buzz(i, tests))
