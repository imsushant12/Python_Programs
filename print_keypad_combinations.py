keys = [".", "abc", "def", "ghi", "jkl","mno","pqrs", "tu", "vwx", "yz"]

def print_keypad_combinations(input_string, output_string):
    # base case
    if len(input_string) == 0:
        print(output_string)
        return
    
    current_key = input_string[0]
    current_key_string = keys[int(current_key)]
    for i in range(len(current_key_string)):
        print_keypad_combinations(input_string[1:],output_string + current_key_string[i])            

if __name__ == "__main__":
    input_string = "23"
    output_string = ""
    print_keypad_combinations(input_string, output_string)