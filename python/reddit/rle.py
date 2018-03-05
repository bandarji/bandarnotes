# Simple run-length encoder

def rle(array):
    result = []
    for i, element in enumerate(array):
        if i == 0:
            count = 1
            continue
        if element == array[i - 1]:
            count += 1
        else:
            result.append(array[i - 1])
            result.append(count)
            count = 1
    result.append(element)
    result.append(count)
    return result

print(rle(["g","g","e","w","w"]))
