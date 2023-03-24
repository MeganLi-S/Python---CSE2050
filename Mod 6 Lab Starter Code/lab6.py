
def find_min(L, m = 1, start = 0, end = None, lower = None, upper = None):
    if end == None:
        end = len(L)
    median = (start + end) // 2
    lower = median - m
    upper = median + m

    if L[lower] > L[median] and upper > len(L) - 1:
        return L[median]

    if median - m < 0:
        lower = median - 1

    if median + m > len(L) - 1:
        upper = median + 1

    if L[lower] > L[median] < L[upper]:
        return L[median]

    if L[median] < L[lower]:
        return find_min(L, m, median, end)
    else:
        return find_min(L, m, start, median)

if __name__ == "__main__":
    print(find_min([1,3,4,9]))
            