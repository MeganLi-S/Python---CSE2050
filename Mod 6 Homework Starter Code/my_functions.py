import numpy as np
import random


class my_float(float):
    comparison_counter = 0

    def __eq__(self, other):
        my_float.comparison_counter += 1
        return super().__eq__( other)

    def __gt__(self, other):
        my_float.comparison_counter += 1
        return super().__gt__(other)
    
    def __lt__(self, other):
        my_float.comparison_counter += 1
        return super().__lt__(other)

    def __le__(self, other):
        my_float.comparison_counter += 1
        return super().__le__(other)

    def __ge__(self, other):
        my_float.comparison_counter += 1
        return super().__ge__(other)
    
    def __ne__(self, other):
        my_float.comparison_counter += 1
        return super().__ne__(other)

    # Add the other required magic methods

def my_generate_monotonic_matrix(size):

    M = np.zeros([size, size])

    for i in range(size):
        randomlist = []
        for k in range(size):
            n = random.randint(0,100)
            randomlist.append(n)
        randomlist.sort()
        for j in range(size):
            M[i,j] = randomlist[j]
    print(M)
    return M

    

    # Write your code that for a given size generates a square
    # row-column monotonic matrix
    pass

# Do not modify the function generate_monotonic_matrix
def generate_monotonic_matrix(size):
    n = size;
    Q = np.full([n, n], my_float)

    S_row_0 = 0
    for i in range(n):
        for j in range(n):
            delta = random.random()

            if (i == 0):
                S_row_0 += delta
                Q[i, j] = my_float(round(S_row_0, 1))
            elif (i != 0 and j == 0):
                Q[i, j]  = my_float(round(Q[i-1, j] + delta, 1))
            elif (i != 0 and j != 0):
                Q[i, j] = my_float(round(max(Q[i-1, j], Q[i, j-1]) + delta,1))

    return Q

def my_search_linear(Q, item):

   # Implement a simple element-by-element search from left to right and top to bottem
    for i in Q:
        for j in range(len(i)):
            if item == i[j]:
                return True
            else:
                pass
    return False

def find_val(L, item, start = 0, end = None):
    if end == None:
        end = len(L)
    median = (start + end) // 2

    if end - start <= 1:
        return L[median] == item
        
    elif L[median] < item:
        return find_val(L, item, median, end)
    else:
        return find_val(L, item, start, median)
    

def helper(Q, item, median):
    right = len(Q[0]) - 1
    bottom = len(Q) - 1
    median_val = Q[right//2][bottom//2]
    #print(median_val)
    #print(Q)
    if item == median_val:
        return True
    elif right <= 1 and bottom <= 1:
        return item == median_val
    elif item > median_val:
        Check1 = helper(Q[:right//2, (bottom//2) + 1:bottom], item, median_val)
        if Check1:
            return True
        else:
            Check2 = helper(Q[(right//2) + 1:right, 0:(bottom//2)], item, median_val)
            
            if Check2:
                return True
            else:
                return helper(Q[(right//2) + 1:right, (bottom // 2) + 1:bottom], item, median_val)
    elif item <= median_val:
        Check1 = helper(Q[0: right // 2, 0:bottom//2], item , median_val)
        if Check1:
            return True
        else:
            Check2 = helper(Q[(right//2) + 1: right, 0:(bottom//2) + 1], item, median_val)
            if Check2:
                return True
            else:
                return helper(Q[0:right //2, bottom//2:bottom], item, median_val)

def my_search(Q, item):
    right = len(Q[0]) - 1
    bottom = len(Q[0]) - 1
    top = 0
    left = 0
    depth = bottom - top
    median_depth = (bottom + top) // 2
    length = right - left
    median_length = (right + left) // 2
    median_val = Q[median_depth][median_length]
    return helper(Q, item, median_val)
   # Implement an efficient version of the search for an element in a row-column
   # monotonic matrix Q


if __name__ == "__main__":
    my_generate_monotonic_matrix(5)
    print(generate_monotonic_matrix(5))
    print(find_val([1,3,5,6,7], 7))
    random.seed(1)
    N = 4
    Q = generate_monotonic_matrix(N)
    print(Q)
    for i in range(N):
        for j in range(N):
            #print(Q[i,j])
            print(my_search(Q, Q[i,j]))
            #print("end")
    bad_values = [0.8, 0.9, 1.1, 1.2, 1.3 ,  3.7, 4.1, 4.2 ]
    for bv in bad_values:
        print(my_search(Q, bv))
    print(my_float.comparison_counter)

