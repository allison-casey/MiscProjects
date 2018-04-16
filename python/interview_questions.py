

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


def target_number(nums, target):
    """Return every distinct pair that adds up to the target value."""
    pairs = []
    checked = set()
    for num in nums:
        if num not in checked and \
                target - num in nums:
            checked.add(num)
            checked.add(target - num)
            pairs.append((num, target - num))

    return pairs

from collections import Counter
import Queue as Q
def adjacent_characters(string):
    frequencies = Counter()
    for char in string:
        frequencies[char] += 1
    
    fixed_str = ''
    q = Q.PriorityQueue()

    for val in frequencies.most_common(): q.put([ -val[1], val[0] ])
    
    last_pair = [float('inf'), None]
    while q.qsize() != 0:
        print(q.queue)
        temp = q.get()
        fixed_str += temp[1]
        temp[0] += 1

        if last_pair[0] < 0:
            q.put(last_pair)

        last_pair = temp
    return fixed_str if len(fixed_str) == len(string) else 'NOT POSSIBLE'

def stagger(arr):
    arr.sort(key = lambda x: x[1])
    return arr

if __name__ == "__main__":
    #  fizz_buzz(10)
    #  print(string_manip('zz'))
    #  print(target_number([1, 4, 45, 6, 10, 8, 12, 4, 12], 16))
    #  print(adjacent_characters('aaab'))
    print(stagger(['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']))
    












