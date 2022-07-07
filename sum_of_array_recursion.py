def find_sum(array):
    if len(array) == 1:
        return array[0]
    
    return array[0] + find_sum(array[1:])

if __name__ == "__main__":
    array = [2, 5, 4, 15, 9, 11]

    print(find_sum(array))
