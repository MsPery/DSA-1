
import tools
import profile
import random

# 3
# a
@profile
def find_max(lst):
    lst.sort()
    return lst[-1]

# b
@profile
def make_lowercase(string):
    return string.lower()

# c
@profile
def sort_int(lst):
    lst.sort()
    return lst

def main():
    print(find_max([10, 2, 5, 10, 5, 8, 9, 0]))
    print(make_lowercase("HOLAA SenIoriTa"))
    print(sort_int([10, 1, 5, 7, 12, 9, 3]))

if __name__ == "__main__":
    main()