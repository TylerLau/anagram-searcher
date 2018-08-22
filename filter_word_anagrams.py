output_file = raw_input("Output file name: ")

anagram_list = open('anagram_noun.txt','r')
output_list = open(output_file,'w')

mode = raw_input ("Filter word (mode1) or first word (mode2): ")
if mode == "mode1":
    filter_word = raw_input("Type word to include: ")
    print filter_word
    
    
    
    i = 0
    for line in anagram_list:
        i += 1
        print i
        words = line.split()
        flag = 0
        for word in words:
            if word == filter_word:
                flag = 1
        if flag == 1:
            output_list.write(line)
            print "ADDED"
    

    
elif mode == "mode2":
    i = 0
    first_words = set()
    for line in anagram_list:
        i+= 1
        print i
        words = line.split()
        first_words.add(words[0])
    for word in first_words:
        output_list.write(word + '\n')
print "DONE"
anagram_list.close()
output_list.close()