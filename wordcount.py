def get_word_count(filename):
    """Reads file and returns count of each word in a file"""
    
    #opens file
    text_file = open(filename)

    #empty list for words and counts
    words_counts_list = {}

    #loops though lines and separates words into a list
    for line in text_file:
        line = line.strip()
        words = line.split()
        
        #takes out punctuation marks and adds words to word count
        for word in words:
            word = word.strip(",.?")
            word = word.title()
            words_counts_list[word] = words_counts_list.get(word, 0) + 1

    #prints out counts of each word in file 
    for word, count in words_counts_list.items():
        print(word, count)
        

get_word_count("test.txt")