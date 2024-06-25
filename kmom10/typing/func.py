# pylint: disable = consider-using-enumerate, cell-var-from-loop, snake_case, invalid-name
"""
func.py: All functions needed for the Type Test
"""
import time

FILE_LIST = ["./src/easy.txt", "./src/medium.txt", "./src/hard.txt"]

def easy():
    """Easy test"""
    compare_strings(0)

def medium():
    """Medium test"""
    compare_strings(1)

def hard():
    """Hard test"""
    compare_strings(2)


def quit_test():
    """Quit the test"""
    print("Test Ended.")

def not_valid():
    """Invalid option selected"""
    print("Please choose one of the options!")

def show_top_scores():
    """Show top scores"""
    unsorted_scores = []

    with open('./src/score.txt', 'r') as fil:
        for line in fil:
            line = line.strip()
            if not line:
                continue
            username, score, level = line.split()
            try:
                score = float(score)
            except ValueError:
                continue
            unsorted_scores.append((username, score, level))

    sorted_scores = sorted(unsorted_scores, key=lambda x: x[1], reverse=True)

    easy_scores = []
    medium_scores = []
    hard_scores = []

    for username, score, level in sorted_scores:
        if level == "easy":
            easy_scores.append((username, score))
        elif level == "medium":
            medium_scores.append((username, score))
        elif level == "hard":
            hard_scores.append((username, score))

    print("\n\tLevel:\t Easy")
    print("\t------------------")
    for username, score in easy_scores:
        print(f"\t{username}:\t {score:.2f}")

    print("\n\tLevel:\t Medium")
    print("\t------------------")
    for username, score in medium_scores:
        print(f"\t{username}:\t {score:.2f}")

    print("\n\tLevel:\t Hard")
    print("\t------------------")
    for username, score in hard_scores:
        print(f"\t{username}:\t {score:.2f}")



def compare_strings(file_index):
    """Compare two strings to find differences"""
    orig_lines = []
    test_lines = []
    user_lines = []
    total_time = 0
    orig_char_count = 0
    orig_wrd_count = 0
    user_wrd_count = 0

    # Open original text file
    with open(FILE_LIST[file_index], "r") as fil:
        for line in fil:
            if line != '\n':
                line = line.strip()
                orig_char_count += len(line)
                line2 = []
                for word in line.split():
                    word = list(word)
                    orig_wrd_count += len(word)
                    line2.append(word)
                test_lines.append(line2)
                orig_lines.append(line)

    for line in orig_lines:
        print("\033[0;32m\n", line, "\033[0m")
        start_time = time.time()

        user_line = input("-")
        line2 = []
        for word in user_line.split():
            line2.append(list(word))
        user_wrd_count += len(line2)
        user_lines.append(line2)

        end_time = time.time()

        total_time += (end_time - start_time)

    # Compare lines to find differences
    char_fails_dict, mistakes_counter = compare_lines(test_lines, user_lines)

    # Calculate score which returns score, error percentage and words per minute
    score, error_percentage, wpm = calc_score(mistakes_counter, orig_char_count, total_time, user_wrd_count)

    # Display results
    display_results(mistakes_counter, score, error_percentage, char_fails_dict, wpm)

    # Ask user for username to add score to high score list
    username = input('Enter username to add to highscore list (optional, press enter to skip): ')
    if username:
        test_type = FILE_LIST[file_index].split('/')[-1].replace('.txt', '')
        registr(username, score, test_type)



# Function to display results
def display_results(mistakes_counter, score, error_percentage, char_fails_dict, wpm):
    """Display results"""
    print("\n")
    print("\033[0;32mScore: \t\t\t", score, "\033[0m")
    print("\033[0;32mError percentage: \t", error_percentage, "\033[0m")
    print("\033[0;32mMistakes: \t\t", mistakes_counter["fails"], "\033[0m")
    print("\033[0;32mWords per minute: \t", wpm, "\033[0m")
    print("\n")
    print("\033[0;32mChar fails: \033[0m")
    for char, count in char_fails_dict.items():
        print("\t", char, ": ", count)


# Function to compare lines
def compare_lines(test_lines, user_lines):
    """Compare lines to find differences"""
    mistakes_counter = {"fails": 0}
    char_fails_dict = {}
    user_words = []
    test_words = []

    # make lines the same length
    for i in range (len(test_lines)):
        words_count = len(user_lines[i]) - len(test_lines[i])

        # user typed extra words
        if words_count > 0:
            mistakes_counter["fails"] += words_count
            while words_count > 0:
                user_lines[i].pop()
                mistakes_counter["fails"] += 1
                words_count -= 1
            
            user_words.append(user_lines[i])
            test_words.append(test_lines[i])

        # user typed less words
        elif words_count < 0:
            while words_count < 0 :
                wordx = test_lines[i].pop()
                for char in wordx:
                    add_to_char_fails_dict(char_fails_dict, char, mistakes_counter)
                words_count += 1


            test_words.append(test_lines[i])
            user_words.append(user_lines[i])
        
        else:
            test_words.append(test_lines[i])
            user_words.append(user_lines[i])
    
    compare_words(test_words, user_words, char_fails_dict, mistakes_counter)

    return char_fails_dict, mistakes_counter
    

# Function to compare words
def compare_words(test_words, user_words, char_fails_dict, mistakes_counter):
    """Compare words to find differences"""
    test_chars = []
    user_chars = []

    # loop through lines
    for i in range(len(test_words)):
        
        # loop through words
        for j in range(len(test_words[i])):

            # make the words the same length
            if len(test_words[i][j]) != len(user_words[i][j]):
                chars_count = len(user_words[i][j]) - len(test_words[i][j])

                # user typed less characters
                if chars_count < 0:
                    while chars_count < 0:
                        wordx = test_words[i][j].pop()
                        add_to_char_fails_dict(char_fails_dict, wordx, mistakes_counter)
                        chars_count += 1
                    test_chars.append(test_words[i][j])
                    user_chars.append(user_words[i][j])

                # user typed more characters
                elif chars_count > 0:
                    while chars_count > 0:
                        user_words[i][j].pop()
                        chars_count -= 1
                    
                    test_chars.append(test_words[i][j])
                    user_chars.append(user_words[i][j])
                
            else:
                test_chars.append(test_words[i][j])
                user_chars.append(user_words[i][j])
    
    compare_chars(test_chars, user_chars, char_fails_dict, mistakes_counter)


# Function to compare characters
def compare_chars(test_chars, user_chars, char_fails_dict, mistakes_counter):
    """Compare characters to find differences"""
    for i in range(len(test_chars)):
        for j in range(len(test_chars[i])):
            if test_chars[i][j] != user_chars[i][j]:
                add_to_char_fails_dict(char_fails_dict, test_chars[i][j], mistakes_counter)




# Function to add wrong characters to dictionary
def add_to_char_fails_dict(char_fails_dict, char, mistakes_counter):
    """Add missing or wrong characters to dictionary"""
    mistakes_counter["fails"] += 1
    if char not in char_fails_dict:
        char_fails_dict[char] = 1
    else:
        char_fails_dict[char] += 1



# function to calculate score
def calc_score(mistakes_counter, orig_lines_len, total_time, user_wrd_count):
    """ calculating score """
    err_pe = 100 * (mistakes_counter["fails"] / orig_lines_len)
    scor = (orig_lines_len * (100 - err_pe)) / total_time
    score = round(scor, 2)
    err_per = round(err_pe, 2)
    totMins = total_time / 60
    wpm = round(user_wrd_count / totMins , 2)
    return score, err_per, wpm


# function to register top score
def registr(username, score, test_type):
    """ register top score after test """
    fil = open('./src/score.txt', 'a')
    fil.write(f"{username} \t {score} \t {test_type}\n")
    fil.close()
