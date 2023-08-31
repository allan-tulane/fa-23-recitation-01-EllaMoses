"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	if len(mylist) == 0: #base case, empty list does not contain element so return -1
		return -1
	if mylist[left] > key: #if the key is smaller than the smallest element in list, it is not in the list so return -1
		return -1
	if mylist[right] < key: #if the key is greater than the largest element in list, it is not in the list so return -1
		return -1
	if len(mylist) == 1: #base case if list is size 1, if the element matches it is in the list at index 0, if it doesn't match it is not in the list
		if key == mylist[0]:
			return 0
		else:
			return -1
	middle = mylist[right//2] #center index
	if key == middle: # if the key is equal to the center index it is found in the list at that postion
		return right//2
	elif key < middle: #recursive call for key smaller than middle element
		return binary_search(mylist[0:right//2],key)
	else: #recursive call for key larger than middle element, must add 1+right//2 to account for the indices to the left of the middle element we are diving on
		return 1 + right//2 + binary_search(mylist[1 + (right//2):], key)
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	### TODO

	###




def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `sort_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO

	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO

	###

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

