"""
Lab 3: Recursion and String/List Processing

Name: Charles Stevens
UID: U00962336

"""
#problem 1
def power_2(n):
    #base case
    if n == 0:
        return 1
    elif n > 0:
        return 2 * power_2(n - 1)
    else:
        return 1 / power_2(-n)
    
#problem 2
def all_star(s):
    #base case
    if len(s) <= 1:
        return s
    return s[0] + "*" + all_star(s[1:])

#problem 3
def sum_odd_digits(n):
    #ensure integer in positive
    n = abs(n)
    #base case
    if n == 0:
        return 0

    last_digit = n % 10
    #check if odd
    if last_digit % 2 == 1:
        return last_digit + sum_odd_digits(n // 10)
    else:
        return sum_odd_digits(n // 10)

#problem 4
def find_first_upper(s):
    for i in range(len(s)):
        if s[i].isupper():
            return i
    return -1

#problem 5
def find_first_upper_recursive(s, index=0):
    #base case
    if index >= len(s):
        return -1
    if s[index].isupper():
        return index
    return find_first_upper_recursive(s, index + 1)

#problem 6
def count_vowels(s):
    #base case
    if len(s) == 0:
        return 0
    #check for vowel at index
    vowels = "aeiouAEIOU"
    if s[0] in vowels:
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

def recursive_match(lst1, lst2, index=0):
    #base case
    if index >= len(lst1):
        return 0

    #check for same value at index
    if lst1[index] == lst2[index]:
        return 1 + recursive_match(lst1, lst2, index + 1)
    else:
        return recursive_match(lst1, lst2, index + 1)

# --------------------------
# tests

# Problem 1
num1 = 3
num2 = -4
num3 = 0

print(f"power_2({num1}) returned {power_2(num1)}")
print(f"power_2({num2}) returned {power_2(num2)}")
print(f"power_2({num3}) returned {power_2(num3)}")

# Problem 2
print(f'all_star("baseball") -> {all_star("baseball")}')
print(f'all_star("hi") -> {all_star("hi")}')
print(f'all_star("a") -> {all_star("a")}')

# Problem 3
print(f"sum_odd_digits(103) -> {sum_odd_digits(103)}")
print(f"sum_odd_digits(11) -> {sum_odd_digits(11)}")
print(f"sum_odd_digits(88) -> {sum_odd_digits(88)}")

# Problem 4
print(f'find_first_upper("HelloWorld") -> {find_first_upper("HelloWorld")}')
print(f'find_first_upper("zyBook") -> {find_first_upper("zyBook")}')
print(f'find_first_upper("hi") -> {find_first_upper("hi")}')

# Problem 5
print(f'find_first_upper_recursive("HelloWorld") -> {find_first_upper_recursive("HelloWorld")}')
print(f'find_first_upper_recursive("zyBook") -> {find_first_upper_recursive("zyBook")}')
print(f'find_first_upper_recursive("hi") -> {find_first_upper_recursive("hi")}')

# Problem 6
print(f'count_vowels("HelloWorld") -> {count_vowels("HelloWorld")}')

# Problem 7
print(f"recursive_match([4, 2, 1, 6], [4, 3, 7, 6]) -> "
      f"{recursive_match([4, 2, 1, 6], [4, 3, 7, 6])}")
