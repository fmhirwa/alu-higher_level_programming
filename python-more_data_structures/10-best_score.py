#!/usr/bin/python3


def best_score(a_dictionary):
    best_key = None
    best_value = None
    for k, v in a_dictionary.items():
        if best_value is None or Value > best_value:
            best_key = k
            best_value = v
    return best_key
