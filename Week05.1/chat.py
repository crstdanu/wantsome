def transform_string(input_string):
    if not input_string:
        return input_string

    transformed_string = ''
    current_char = input_string[0]
    char_count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            char_count += 1
        else:
            transformed_string += str(char_count) + current_char
            current_char = input_string[i]
            char_count = 1

    transformed_string += str(char_count) + current_char

    return transformed_string


# Example usage:
input_string = "AAAAA"
transformed_string = transform_string(input_string)
print(transformed_string)
