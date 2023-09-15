"""	Program to count occurrences of a given character in a string.
	Count character 'e' in the below string.
	Input "geeksforgeeks".
"""
def count_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

""""input_string = "geeksforgeeks"
character_to_count = "e"
result = count_occurrences(input_string, character_to_count)
print(f"The character '{character_to_count}' appears {result} times in the string.")"""""

"""input_string = "abccdefgaa"
character_to_count = "a"
result = count_occurrences(input_string, character_to_count)
print(f"The character '{character_to_count}' appears {result} times in the string.")"""