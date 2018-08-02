#
# The challenge is to fix the function 'pick_evens' so that it performs as planned 100% of the
# time. Also, reduce any inefficiencies in the algorithm to improve runtime/readability. 
#
#-----------------------------------------------------------------------------------------------
import random as rnd
import time
import timeit
#-----------------------------------------------------------------------------------------------

n = 3 

##  Selects n even values from a list, my_list.
#   @param n       : The number of values to select.
#   @param my_list : The list ot collect values from.
#   @return        : A list of n even values from my_list
def pick_evens(n, my_list):

    to_move = [] # Stores the selected values.
    evens = [integer for integer in my_list if integer%2 == 0]

    def gather_values():
        nonlocal to_move
        nonlocal evens
        if (len(to_move) < n): # If to_move has enough values.
            for dummy in range(n):
                rnd.seed(time.time())
                value = evens[rnd.randint(0, len(evens)-1)]
                if value in to_move: # If to_move has the chosen value already.
                    gather_values()
                else:
                    to_move.append(value)
    gather_values()

    return to_move

################################################ main ##########################################

# The goal is to randomly move n even elements from list1 to list2. There should be no duplicate
# elements in either list, so if a duplicate is incurred by the move, it should be removed.
# After moving the elements both lists should be sorted.

list1 = [1, 2, 5, 10, 9, 15, 34, 78, 230, 4, 1, 3, 5, 9]
list2 = [81, 4, 18, 2, 45, 9, 29, 4, 192, 923]

# Times the function call.
start = timeit.default_timer()
list1_evens = pick_evens(n, list1)
stop = timeit.default_timer()

# Prints the results of the call.
print(str(round(1000000*(stop - start), 3)) + ' usec')
print(list1_evens)

# Moves the values.
for value in list1_evens:
    list2.append(value)
    list1.remove(value)

# Sorts and prints the new lists.
list1 = list(set(list1))
list2 = list(set(list2))
list1.sort()
list2.sort()
print(list1)
print(list2)



