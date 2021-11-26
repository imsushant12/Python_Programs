def move_X_to_end(input_string):
    countX = 0
    result_string = ""
    for i in range(len(input_string)):
        if input_string[i] == 'x':
            countX += 1
        else:
            result_string += input_string[i]
    
    for i in range(countX):
        result_string += 'x'

    print(result_string)


def move_X_to_end_improved(input_string):
    countX = 0
    for i in range(len(input_string)):
        if input_string[i] == 'x':
            countX += 1
        else:
            print(input_string[i], end="")
  
    for i in range(countX):
        print("x", end="")

if __name__ == "__main__":
    input_string = "abxcdxex"
    move_X_to_end_improved(input_string)