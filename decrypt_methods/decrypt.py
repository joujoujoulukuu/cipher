def decrypt1(ciphertext, key):
    return ciphertext


async def analyze(ciphertext, output_file_path):
    char_counts = {}
    for char in ciphertext:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

        # Sort char_counts by values (character counts) in descending order
    sorted_char_counts = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    length = len(sorted_char_counts)
    with open(output_file_path, 'a') as output_file:

        for char, count in sorted_char_counts:
            print(f"'{char}': {count} : {round(count/length, 2)}%\n")
            output_file.write(f"'{char}': {count} : {round(count/length, 2)}%\n")