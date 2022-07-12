def subsets(array, i, answer):
    if i >= len(array):
        print(answer)
        return

    # including the current element
    subsets(array, i+1, answer+[array[i]])

    # excluding the current element
    subsets(array, i+1, answer)


array = [1, 2, 3]
# an answer list that will store the results
answer = []
startIndex = 0
print("Subsets are: ")
subsets(array, startIndex, answer)
