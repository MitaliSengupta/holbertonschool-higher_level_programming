#!/usr/bin/python3
from sys import argv

"""
This modules finds all solutions for N queens problem
"""


class Queen:
    """
    Class defined as Queen to solve nQueens problem
    using recursion
    """
    def can_move(self, x, y, right):

        """
        Function to see if queen can move in the vaild constraint
        column provided
        """
        for a in range(x):
            if right[a] == y:
                return (False)
            if abs(right[a] - y) == (x - a):
                return (False)
        return (True)

    def solution(self, n, N, right):
        """
        function to find all the right combos that can happen
        using recursion.
        """
        if n == N:
            print("[", end="")
            for j in range(N):
                print("[{}, {}]".format(j, right[j]), end="")
                if j < N - 1:
                    print(", ", end="")
            print("]")
            return

        for j in range(N):
            if self.can_move(n, j, right):
                right[n] = j
                self.solution(n + 1, N, right)

if __name__ == "__main__":
    count = len(argv)

    if count != 2:
        print("Usage: nqueens N")
        exit(1)
    else:
        try:
            N = int(argv[1])
        except:
            print("N must be a number")
            exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    final = Queen()
    final.solution(0, N, [None for i in range(N)])
