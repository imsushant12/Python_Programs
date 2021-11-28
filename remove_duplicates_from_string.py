def remove_duplicates(input_string):
    hash_map = []
    
    for i in range(len(input_string)):
        if input_string[i] not in hash_map:
            print(input_string[i], end="")
            hash_map.append(input_string[i])
            

if __name__ == "__main__":
    input_string = "abacdxbc"
    remove_duplicates(input_string)