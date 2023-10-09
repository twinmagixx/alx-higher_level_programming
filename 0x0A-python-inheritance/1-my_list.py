#!/usr/bin/python3
"""1-my_list.py
SA
"""


class MyList(list):
    """ Class inheriting the attributes references of class list

    Args:
        list: class list

    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
