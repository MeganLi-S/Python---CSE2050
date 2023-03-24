from my_functions import my_float, generate_monotonic_matrix, my_generate_monotonic_matrix, my_search, my_search_linear
import random
import unittest

class MonotonicMatrixTests(unittest.TestCase):

    def test_comparison_counter(self):

        A = my_float(3)
        B = my_float(4)

        L1 = my_float.comparison_counter

        if (B == A):
            print("A and B are equal")

        L2 = my_float.comparison_counter

        self.assertEqual(L2 - L1, 1)

        if (B <  A):
            print("B is smaller than A")

        if (A < B):
            print("A is smaller than B")

        L3 = my_float.comparison_counter

        self.assertEqual(L3 - L2, 2)

    def test_comparison_counter_other(self):
        A = my_float(11.3)
        B = my_float(25.8)

        L1 = my_float.comparison_counter

        if (B != A):
            print("A and B are different.")

        L2 = my_float.comparison_counter

        self.assertEqual(L2 - L1, 1)

        if (B <=  A):
            print("B is less or equal than A")

        if (A <= B):
            print("A is less or equal than B")

        L3 = my_float.comparison_counter

        self.assertEqual(L3 - L2, 2)

    def test_example_monotonic(self):

        N = 10
        Q = my_generate_monotonic_matrix(N)
        for i in range(N):
            for j in range(N):
                if (i < N-1): # We can check monotonicity for the current column
                    self.assertTrue(Q[i, j] < Q[i + 1, j])

                if (j < N-1):
                    self.assertTrue(Q[i, j] < Q[i, j + 1])


    def test_linear_search(self):
        random.seed(4)
        N = 50
        Q = generate_monotonic_matrix(N)

        before1 = my_float.comparison_counter;
        print('\n' + str(my_search_linear(Q, 70.2)))
        after1 = my_float.comparison_counter;

        self.assertEqual(after1 - before1, 2500)

        before2 = my_float.comparison_counter;
        print('\n' + str(my_search(Q, 70.2)))
        after2 = my_float.comparison_counter;

        print("test_linear_search: Your implementation  requires {} comparisons (as compared to 2500 for linear search)".format(after2 - before2))

        self.assertLess(after2 - before2, 500)



    def test_search(self):
        random.seed(1)
        N = 4
        Q = generate_monotonic_matrix(N)

        print(Q)

        for i in range(N):
            for j in range(N):
                self.assertTrue(my_search(Q, Q[i,j]))

        bad_values = [0.8, 0.9, 1.1, 1.2, 1.3 , 3.1, 3.7, 4.1, 4.2 ]
        for bv in bad_values:
            self.assertFalse(my_search(Q, bv))


    def test_efficiency(self):
        random.seed(2)
        N = 50
        Q = generate_monotonic_matrix(N);

        M = 20

        comp_counts = []

        for i in range(M):
            x = random.randint(N // 2, N - 1)
            y = random.randint(N // 2, N - 1)

            before1 = my_float.comparison_counter;
            my_search(Q, Q[x, y])
            after1 = my_float.comparison_counter;
            count1 = after1 - before1

            comp_counts.append(count1)

            for c in comp_counts:
                self.assertLessEqual(c, 500)

if __name__ == '__main__':
   unittest.main()