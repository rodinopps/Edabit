def remove_smallest(numbers):
    if len(numbers) <= 1:
        return []
    else:
        ind = numbers.index(min(numbers))
        return numbers[:ind] + numbers[ind + 1:]
