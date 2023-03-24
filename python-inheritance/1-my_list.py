#!/usr/bin/python3
""" This class MyList inherits from list """


class MyList(list):
    """ Sorts lists object """

    def print_sorted(self):
        """ Print sorted list """
        copy_list = self[:]
        copy_list.sort()
        print("{}".format(copy_list))
