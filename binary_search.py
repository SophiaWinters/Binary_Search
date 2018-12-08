# binary search (requires sorted array)

def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else: 
			if item < item_list[mid]:
				last = mid - 1
			else: 
				first = mid + 1
	return found
	
# 1 = low, 8 = high and the middle(or 'mid') is low + high/2
# since the mid value is greater than 6 in the first print line

print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))


