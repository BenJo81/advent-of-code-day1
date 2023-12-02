with open("input.txt") as f:
    content = f.read().splitlines()

number_box = []

number_1 = ""
number_2 = ""


def check_number_words_left(current_letter, current_word):
    number_text = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if current_word[current_letter: current_letter + 3] == number_text[0]:
        return "1"
    elif current_word[current_letter: current_letter + 3] == number_text[1]:
        return "2"
    elif current_word[current_letter: current_letter + 3] == number_text[5]:
        return "6"
    elif current_word[current_letter: current_letter + 4] == number_text[3]:
        return "4"
    elif current_word[current_letter: current_letter + 4] == number_text[4]:
        return "5"
    elif current_word[current_letter: current_letter + 4] == number_text[8]:
        return "9"
    elif current_word[current_letter: current_letter + 5] == number_text[2]:
        return "3"
    elif current_word[current_letter: current_letter + 5] == number_text[6]:
        return "7"
    elif current_word[current_letter: current_letter + 5] == number_text[7]:
        return "8"
    else:
        return "nada"


def check_number_words_right(current_letter, current_word):
    number_text = ["eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]
    if current_word[current_letter: current_letter + 3] == number_text[0]:
        return "1"
    elif current_word[current_letter: current_letter + 3] == number_text[1]:
        return "2"
    elif current_word[current_letter: current_letter + 3] == number_text[5]:
        return "6"
    elif current_word[current_letter: current_letter + 4] == number_text[3]:
        return "4"
    elif current_word[current_letter: current_letter + 4] == number_text[4]:
        return "5"
    elif current_word[current_letter: current_letter + 4] == number_text[8]:
        return "9"
    elif current_word[current_letter: current_letter + 5] == number_text[2]:
        return "3"
    elif current_word[current_letter: current_letter + 5] == number_text[6]:
        return "7"
    elif current_word[current_letter: current_letter + 5] == number_text[7]:
        return "8"
    else:
        return "nada"


for word in content:
    letter_count_left = 0
    letter_count_right = 0
    left_count = True
    right_count = True
    word_flip = word[::-1]
    while left_count:
        if word[letter_count_left].isalpha():
            word_check = check_number_words_left(letter_count_left, word)
            if word_check == "nada":
                letter_count_left += 1
            elif word_check != "nada":
                number_1 = word_check
                left_count = False
        else:
            number_1 = word[letter_count_left]
            left_count = False
    while right_count:
        if word_flip[letter_count_right].isalpha():
            words_check = check_number_words_right(letter_count_right, word_flip)
            if words_check == "nada":
                letter_count_right += 1
            elif words_check != "nada":
                number_2 = words_check
                right_count = False
        else:
            number_2 = word_flip[letter_count_right]
            right_count = False
    new_number = number_1 + number_2
    number_box.append(int(new_number))
print(number_box)
answer = sum(number_box)

print(answer)
