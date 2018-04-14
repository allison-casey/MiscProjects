

def fizz_buzz(iterations):
    """Fizz Buzz with special rules.
    
    Rule 1: digits add to 9 print Fizz
    Rule 2: divisible by 5 print Buzz
    """
    def get_digits(val):
        digits = []
        while val:
            digits.append(val % 10)
            val /= 10
        return digits
    
    
    for i in range(iterations):
        s = ''
        if sum(get_digits(i)) == 9:
            s += 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'

        print( s if len(s) != 0 else i )

def string_manip(string):
    """Count number of words that end in y or z"""

    #  tokens = string.split(' ')
    #  count = 0
    #  for token in tokens:
    #      if token[-1] in ['y', 'z']:
    #          count += 1
    if len(string) == 0:
        return 0
    
    letters = ['y', 'z']
    count = 0
    last_space = 0
    for i in range(len(string)):
        if string[i] == ' ':
            if string[i-1] in letters:
                count += 1
            last_space = i

    return(count + 1 if string[-1] in letters else count)

from collections import defaultdict
def target_number(nums, target):
    
    pairs = []
    checked = set()
    for val in nums:
        temp = target - val
        if temp >= 0 and temp in checked:
            pairs.append((val, temp))
        checked.add(val)

    return pairs


    #  frequencies = defaultdict(int)
    #  for val in nums:
    #      frequencies[val] += 1
    #  
    #  pairs = []
    #  for key in frequencies.keys():
    #      if (target - key) in frequencies:
    #          pairs.append((key, target - key))
    #          del frequencies[key]
    #          if target - key != key:
    #              del frequencies[target - key]
    #  
    return pairs
    

if __name__ == "__main__":
    #  fizz_buzz(10)
    #  print(string_manip('zz'))
    print(target_number([1, 4, 45, 6, 10, 8, 12, 4, 12], 16))
