def bubblesort(array):
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                unsorted = True
                array[i], array[i+1] = array[i+1], array[i]
    return array
