import re
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

# _____________ kill bad words

def no_bad_words(text):
    new_text = []
    for i in text:
        if i not in STOP_WORDS:
            new_text.append(i)
    return new_text


# ___________________ lowercases each string, removes bad characters,

def clean_text(text):
    new_string_list = []
    for string in text:
        string = string.lower()
        string = re.sub(r'[^a-z ]', '', string)
        new_string_list.append(string)
    return new_string_list



# -------------- sorts a 2 dimensional array by the second item

def my_sort(word_freq_dict):
    sorted_dict = sorted(word_freq_dict.items(), key=lambda x: (-x[1], x[0]), reverse=False)
    return sorted_dict


# __________________ smusher, smushes list of strings into a string
def smusher(list_of_strings):
    new_string = ""
    new_string = " ".join(list_of_strings)
    return new_string


# ____________ splits on space

def split_text(text):
    text = text.split()
    return text


# ___________ counter

def counter(a_list):
    counted_dict = {}
    for i in a_list:
        if i not in counted_dict:
            counted_dict.setdefault(i, 1)
        else:
            counted_dict[i] += 1
    return counted_dict

# ________printer
def output_print(a_list):
    a_list = a_list[:10]
    a_dict = dict(a_list)
    print()
    print(f"The word frequency in {file} is:".center(80))
    print("________________________________________".center(80))
    for word, frequency in a_dict.items():
        print("{} |  {} {}".format(word.rjust(18), str(frequency).ljust(3), "*" * frequency))
    print("________________________________________".center(80))


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as initial:
        initial_list = initial.readlines()
    cleaned_list = clean_text(initial_list)
    smushed_list = smusher(cleaned_list)
    split_list = split_text(smushed_list)
    good_words = no_bad_words(split_list)
    counted = counter(good_words)
    sorted_dict = my_sort(counted)
    output_print(sorted_dict)




if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
