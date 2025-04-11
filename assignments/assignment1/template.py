import time
from math import floor
from random import randint
from contextlib import contextmanager

# In this assignment, you will implement and test Insertion-Sort, Merge-Sort and
# Quicksort. First, you are given three utility functions, that are used for
# testing. Your task is to implement the insertion_sort, merge_sort and
# quicksort functions and their associated sub-procedures.


### UTILITY FUNCTIONS ###

@contextmanager
def performance():
    """A context manager that keeps track of time"""
    t1 = t2 = time.perf_counter()
    yield lambda: t2 - t1
    t2 = time.perf_counter()


def get_unsorted_lists(size, kind='random', n_copies=3):
    """
    Create two unsorted list of size `size` that is either completely random,
    almost sorted or reversed, depending on the `kind` argument
    """
    if kind == 'random':
        l = [randint(0, 10_000) for _ in range(size)]

    elif kind == 'almost_sorted':
        l = [randint(i - 2, i + 2) for i in range(size,)]

    elif kind == 'reversed':
        l = list(range(size, 0, -1))

    return l.copy() for _ in range(n_copies)


def is_sorted(A):
    """Checks if the list `A` is sorted"""
    return all(A[i] <= A[i+1] for i in range(len(A) - 1))


### YOUR IMPLEMENTATION GOES HERE ####


def insertion_sort(A, n):
    # IMPLEMENT THIS
    pass


def merge(A, p, q, r):
    # IMPLEMENT THIS
    pass


def merge_sort(A, p, r):
    # IMPLEMENT THIS
    pass


def partition(A, p, r):
    # IMPLEMENT THIS
    pass


def quicksort(A, p, r):
    # IMPLEMENT THIS
    pass


if __name__ == '__main__':

    # different sizes of input to test on
    sizes = [1000, 10_000, 15_000, 25_000, 50_000, 100_000, 1_000_000]

    # keep track of much time each algorithm spends
    ms_max_time, is_max_time, qs_max_time = 0, 0, 0

    # set to 'random' to get a list of random number
    # set to 'reversed' to get a list in reversed sorted order
    # set to 'almost_sorted' to get an... almost sorted list
    kind = 'random'  # experiment with changing this values

    # main test loop
    for size in sizes:
        print(f"Test for size {size}")

        # since we are sorting in-place, we need 2 instances of the input list
        # (one for insertion sort and one for merge sort)
        l1, l2, l3 = get_unsorted_lists(size, kind=kind)

        # test Insertion-Sort, only if it took less than 5 seconds last time
        if is_max_time < 5:

            # the 'with'-statement is just a helper to track time
            with performance() as is_time:
                # PUT YOUR CALL TO insertion_sort HERE!
                pass

            # assert that the list godt sorted properly
            assert is_sorted(l1), 'Oh oh, something wrong with insertion sort!'

        # test Merge-Sort, only if it took less than 5 seconds last time
        if ms_max_time < 5:

            # the 'with'-statement is just a helper to track time
            with performance() as ms_time:
                # PUT YOUR CALL TO merge_sort HERE!
                pass

            # assert that the list got sorted properly
            assert is_sorted(l2), 'Oh oh, something wrong with merge sort!'

        # test QuickSort, only if it took less than 5 seconds last time
        if qs_max_time < 5:

            # the 'with'-statement is just a helper to track time
            with performance() as qs_time:
                # PUT YOUR CALL TO quicksort HERE!
                pass

            # assert that the list got sorted properly
            assert is_sorted(l3), 'Oh oh, something wrong with quicksort!'

        print(f'Insertion sort: {"-" if is_max_time > 5 else f"{is_time():0.2f}s"}')
        print(f'Merge sort: {"-" if ms_max_time > 5 else f"{ms_time():0.2f}s"}')
        print(f'Quicksort: {"-" if qs_max_time > 5 else f"{qs_time():0.2f}s"}')

        is_max_time = max(is_time(), is_max_time)
        ms_max_time = max(ms_time(), ms_max_time)
        qs_max_time = max(qs_time(), qs_max_time)

        print()
