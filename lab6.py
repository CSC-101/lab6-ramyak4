import data
from typing import Optional
from data import Book

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        m_index = index_smallest_from(values, idx)
        tmp = values[m_index]
        values[m_index] = values[idx]
        values[idx] = tmp


# Part 1
# This function sorts through a list of books and alphabetizes it by title
# input: list of book objects
# output: list of book objects
def  selection_sort_books(books:list[Book]) -> list[Book]:
    for i in range(len(books)):
        min_i = i
        for j in range(i + 1, len(books)):
            if books[j].title < books[min_i].title:
                min_i = j
        temp = books[i]
        books[i] = books[min_i]
        books[min_i] = temp
    return books

# Part 2
# This function "swaps" the case of all characters in a string, lower to upper and vice versa
# input: one string variable
# output: one string variable
def swap_case(word:str) -> str:
    new_word = []
    for i in word:
        if i.islower():
            new_word.append(i.upper())
        elif i.isupper():
            new_word.append(i.lower())
        else:
            new_word.append(i)
    return "".join(new_word)

# Part 3
# This functions swaps every instance of a character in a string with another given character
# input: 3 string variables
# output: 1 string variable
def str_translate(word: str, old: str, new: str) -> str:
    new_word = []
    if len(old) == 1 and len(new) == 1:
        for i in word:
            if i == old:
                new_word.append(new)
            else:
                new_word.append(i)
    return "".join(new_word)

# Part 4
# This function counts every word in a piece of text
# input: 1 string variable
# output: 1 dictionary list
def histogram(text: str) -> dict[str, int]:
    counts = {}
    for i in text.split():
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

