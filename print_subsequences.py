def print_subsequences(input_string, output_string):
    # base case
    if len(input_string) == 0:
        print(output_string)
        return
    
    # not including current charater
    print_subsequences(input_string[1:], output_string)
    
    # including current character
    print_subsequences(input_string[1:], output_string + input_string[0])
            

if __name__ == "__main__":
    input_string = "abc"
    output_string = ""
    print_subsequences(input_string, output_string)