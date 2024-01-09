#!usr/bin/python3
"""MyList Module - prints the list, but sorted (ascending sort)"""


class MyList(list):
    """class MyList manipulates list data"""

    def print_sorted(self):
        """sorts list in ascending order"""
        
        print(list.sort())
