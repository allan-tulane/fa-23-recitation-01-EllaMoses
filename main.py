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
	middle = (left+right)//2 #center index
	if key == mylist[middle]: # if the key is equal to the center index it is found in the list at that postion
		return middle
	elif right <= left: #base case to end recursion 
		return -1
	else:
		if mylist[middle] > key: #recursive call for key smaller than middle element, left stays the same right changes to one less than middle so it isn't searched twice
			return _binary_search(mylist, key, left, middle-1)
		elif mylist[middle] < key: #recursive call for key larger than middle element, right stays the same and left changes to one plus middle so it isn't searched twice
			return _binary_search(mylist, key, middle + 1, right)


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
	time1 = time.time()
	search_fn(mylist, key)
	time2 = time.time()
	return (time2-time1) * 1000

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
	linear_times = []
	binary_times = []
	for i in sizes:
		mylist= []
		n = 0
		while n < i:
			mylist.append(n)
			n+=1
		linear_times.append(time_search(linear_search, mylist, -1))
		binary_times.append(time_search(binary_search, mylist, -1))
	
	return(list(zip(sizes, linear_times, binary_times)))

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))
	
print_results(compare_search())

