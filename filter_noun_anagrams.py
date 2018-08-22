# Parse words from list of anagrams
# Iterate over each line
#   Check each word in line
#     if word isn't noun, skip to next line
#   If all words are nouns, add anagram to output file

from PyDictionary import PyDictionary
dictionary = PyDictionary()

noun_list = set()
not_noun_list = set()

anagram_list = open('anagram list.txt','r')
output_list = open('output.txt','w')
      
i = 0    

for line in anagram_list:
    i += 1
    words = line.split()
    print i
    flag = 0
    for word in words:
        # Check if word has already been searched and whether it is a noun or not
        if word in noun_list:
            flag += 1
        elif word in not_noun_list:
            flag -= 1
        # If word has not been searched, use PyDictionary module to check if it is a noun and add to appropriate list
        else:
            if u'Noun' in dictionary.types(word):
                flag += 1
                noun_list.add(word)
            else:
                not_noun_list.add(word)   
    # If all words are nouns, add to output file
    if flag == len(words):
        print "ADDED"
        output_list.write(line)
            

output_list.close()
anagram_list.close()

print "Done"