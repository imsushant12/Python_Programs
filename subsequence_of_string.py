def generateSubsequences(string, index, currentAnswer):
    if index >= len(string):
        if len(currentAnswer) == 0:
            print('" "')
        else:
            print(currentAnswer)
        return

    generateSubsequences(string, index+1, currentAnswer+string[index])
    # not adding current character
    generateSubsequences(string, index+1, currentAnswer)


string = "abc"
generateSubsequences(string, 0, "")
