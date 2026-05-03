def count_names_and_vowels(file_name):
    with open(file_name, 'r') as file:
        names = [line.strip() for line in file]

    total_names = len(names)
    vowel_names = [name for name in names if name[0].lower() in 'aeiou']
    longest_name = max(names, key=len)

    print(f"Total names: {total_names}")
    print(f"Names starting with vowel: {len(vowel_names)}")
    print(f"Longest name: {longest_name}")

count_names_and_vowels('name.txt')