import random
import listcompl as lc
import string


def main():
    '''The three algorithms would take respectively an estimate runtime of:
       0.724 sec
       0.001 sec
       0.609 sec for an input size of 1000000 | see images for plots
    '''
    print(lc.find_max(random.sample(range(1, 10000000), 1000000)))
    lc.sort_int(random.sample(range(1, 10000000), 1000000))
    lc.make_lowercase(''.join(random.choice(string.ascii_letters) for i in range(1000000)))

if __name__ == "__main__":
    main()