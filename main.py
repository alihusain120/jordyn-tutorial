
# Demonstrating imports

# both of the files are in the same directory
# we can just import them as "modules"
# you can still import modules from elsewhere btw
# but let's keep it simple

# Two ways to do so, I'll show both
# Notice: if you import them differently, the call (below) will be different.

# 1. import the whole module
import first_algo

# 2. import just what you need
from second_algo import second_algorithm

def main():

    # open friends.txt
    f = open('friends.txt', 'r')
    # iterate lines (or in your case, loop through photos in dir)
    for line in f:
        # call first algorithm on line/photo
        first_algo.first_algorithm(line.strip())
        # call second algorithm on line/photo
        second_algorithm(line.strip())
    
if __name__ == "__main__":
    main()