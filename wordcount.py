# opens a file and counts how many times each space-separated word occurs
# in that file. Your program should then print those counts to the screen
#counts words and returns counts
#add words to dictionary by looping througn and adding count by changing 
#dictionary values


def get_word_count(filename):
    """Reads file and returns count of each word"""
    text = open(filename)

    for line in text:
        print(line)

get_word_count("test.txt")