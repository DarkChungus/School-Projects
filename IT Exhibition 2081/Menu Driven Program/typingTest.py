import time
import random

def wpm():
    """
    This is a quick program that I made, it measures your words per minute. As said, it is a very quick program,
    so it is really not that accurate. I just used some logic, and it calculates your average wpm, doesn't
    count accuracy, or your actual speed. It just uses a simple formula that I made up, so your words per
    minute should be a little higher than the one you see here. It has around 70 common words in the list.
    =======================
    INSPIRED BY MONKEYTYPE
    =======================
    :return:
    """
    list = [
        'also', 'during', 'find', 'be', 'on', 'work', 'or', 'school', 'line', 'just', 'number',
        'any', 'become', 'many', 'do', 'as', 'both', 'down', 'hold', 'it', 'he', 'could', 'she',
        'become', 'who', 'present', 'any', 'when', 'into', 'no', 'and', 'how', 'help', 'leave',
        'know', 'face', 'will', 'way', 'govern', 'can', 'each', 'form', 'fact', 'system', 'ask',
        'very', 'of', 'make', 'work', 'program', 'eye', 'than', 'head', 'hand', 'would', 'give',
        'but', 'day'
    ]
    chosen_words = ""

    print("1. 10 Words")
    print("2. 30 Words")
    print("3. 50 Words")

    user_input = str(input("Enter which one you want to do: "))
    print()
    if user_input[0] == '1':

        # This gets 10 random words

        for i in range(1, 11):
            choice = random.choice(list)
            chosen_words = chosen_words + choice + " "

        print(chosen_words)
        print("Your input starts in...")
        time.sleep(.5)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print("GO!")
        start = time.time()
        str(input(""))
        end = time.time()
        length = end - start
        wpm = 600 / length # Calculation

        # Shows your words per minute
        print(f'You have {wpm} words per minute.')

    elif user_input[0] == '3':
        for i in range(1, 31):

            # This gets 30 random words

            choice = random.choice(list)
            chosen_words = chosen_words + choice + " "

        print(chosen_words)
        print("Your input starts in...")
        time.sleep(.5)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print("GO!")
        start = time.time()
        str(input(""))
        end = time.time()
        length = end - start
        wpm = 1800 / length # Calculation

        # Shows your words per minute
        print(f'You have {wpm} words per minute.')

    elif user_input[0] == '5':
        for i in range(1, 51):

            # This gets 50 random words

            choice = random.choice(list)
            chosen_words = chosen_words + choice + " "

        print(chosen_words)
        print("Your input starts in...")
        time.sleep(.5)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print("GO!")
        start = time.time()
        str(input(""))
        end = time.time()
        length = end - start
        wpm = 3000 / length # Calculation

        # Shows your words per minute
        print(f'You have {wpm} words per minute.')
