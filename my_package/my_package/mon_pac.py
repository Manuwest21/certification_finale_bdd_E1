from setuptools import setup, find_packages
from ML_master import pr


def fonction_module1():
    print("Ceci est la fonction du module 1.")

def merge(list1, list2):
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Add any remaining elements from list1 or list2
    while i < len(list1):
        merged_list.append(list1[i])
        
        
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list