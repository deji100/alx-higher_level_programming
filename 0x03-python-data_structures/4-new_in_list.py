#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if idx < 0 or idx > (len(my_list) - 1):
        new_copy = my_list.copy()
        return new_copy

    copy = [x for x in my_list]
    copy[idx] = element
    return (copy)
