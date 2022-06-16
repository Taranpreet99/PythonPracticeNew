
#from jmespath import search
from unit_tester import test
from binary_search import search_binary

#wrote tests first, now will write search_linear function
def search_linear(xs, target):
    for(i, v) in enumerate(xs):
        if v == target: #probe
            return i
    return -1


friends = ["Joe", "Zoe", "Brad", "Angelina","Zuki", "Thandi","Paris"]
test(search_linear(friends,"Zoe") == 1)
test(search_linear(friends,"Joe") == 0)
test(search_linear(friends,"Paris") == 6)
test(search_linear(friends,"Bill") == -1)


#A different approach

vocab = ["apple", "boy", "dog", "down","fell","girl","grass","the","tree"]
book_words = "the apple fell from the tree to the grass".split()

#wrote tests first - now function
def find_unknown_words(vocab, wds):
    result = []
    for w in wds:
        #if(search_linear(vocab, w) < 0):
        #Changing it to binary now
        if(search_binary(vocab, w) < 0):
            result.append(w)
        return result

test(find_unknown_words(vocab, book_words) == ["from", "to"])
test(find_unknown_words([],book_words) == book_words)
test(find_unknown_words(vocab,["the","boy","fell"]) == [])

#Load words from the file we downloaded
def load_words_from_file(filename):
    f = open(filename, "r") #f is handle to access file
    file_content = f.read() #Reading all contens of the file
    f.close() #closed handler
    wds = file_content.split() #Converted file_content to a list wds
    return wds #returned list

#now let's test this method
bigger_vocab = load_words_from_file("vocab.txt")
print("There are {0} words in the vocab, starting with \n {1} ".format(len(bigger_vocab), bigger_vocab[:6]))

#text_to_words function, will make use of translate method, to remove all punctuation
def text_to_words(the_text):

    my_substitutions = the_text.maketrans(
        #Replacing any of the below with the others mentioned after ","
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\","abcdefghijklmnopqrstuvwxyz                                          ")

    #Translate text now
    cleaned_text = the_text.translate(my_substitutions) #This is text clear of any punctuation and all in lowercase
    wds = cleaned_text.split() #Created a list of words from the text 
    return wds 


#tests for converting text to words function
test(text_to_words("My name is Earl!") == ["my","name","is","earl"])
test(text_to_words('"well, I never!",said Alice.') == ["well","i","never","said","alice"])

#Get text from a file and then convert it to 
def get_words_in_book(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

book_words = get_words_in_book("alice_in_wonderland.txt")
print("There are {0} words in the book, the first 100 are\n{1}".format(len(book_words),book_words[:100]))


#find words that are not in our vocab
missing_words = find_unknown_words(bigger_vocab, book_words)

print("There are {0} unknown words.".format(len(missing_words)))


