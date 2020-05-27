# Binary Search


def binarySearch(List, target):
    """
    :param List: Sorted list of items
    :param target: Item to be retrieved
    :return: Index of item being searched
    """
    # Assumes List to already be sorted
    length = len(List)
    return recursiveSection(List, target, 0, length-1)


def recursiveSection(List, target, start, end):
    """
    :param List: Sorted list of items
    :param target: Item to be retrieved
    :param start: Start index of the list
    :param end: End index of the list
    :return: False if not found, the index if found
    """
    # Rounds in case of odd number being divided
    mid = start + round((end - start)/2)
    # In case the middle value
    if target == List[mid]:
        return mid
    # If true, means the index is lower than the midpoint, causing it to be in the lower half
    if min(target, List[mid]) == target:
        return recursiveSection(List, target, start, mid)
    # Else would thus be in the case of it being higher than the mid, so no need for elif
    else:
        return recursiveSection(List, target, mid, end)


test = [1,2,3,4,5,6,7]
target = 5
print(binarySearch(test,target))


