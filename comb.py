

import itertools
vett=["Piero","Marco","Francesco","Piergiorgio"]

if __name__ == "__main__":
    lst = list(itertools.combinations(vett, 3))
    for i in range(0,len(lst)):
        print(str(lst[i]))