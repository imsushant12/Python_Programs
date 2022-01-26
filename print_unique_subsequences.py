def print_unique_subsequences(input_string, output_string, hash_set):
    # base case
    if len(input_string) == 0:
        if output_string not in hash_set:
            print(output_string)
            hash_set.append(output_string)
            return
        else:
            return
    
    current_character = input_string[0]
    # not including current charater
    print_unique_subsequences(input_string[1:], output_string, hash_set)
    
    # including current character
    print_unique_subsequences(input_string[1:], output_string + current_character, hash_set)
            

if __name__ == "__main__":
    input_string = "aaa"
    output_string = ""
    hash_set = []
    print_unique_subsequences(input_string, output_string, hash_set)