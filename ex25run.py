import ex25 # If there is only 1 file imported you can do from ex25 import *, imports everything, gets ,confusing if you have many files
# you can also do import ---- as -- to make it shorter and easier to write 
sentence = "All good things come to those who wait. "
words =ex25.break_words(sentence)
print(words)
sorted_words = ex25.sort_words(words)
print(sorted_words)
ex25.print_first_word(words)
ex25.print_last_word(words)
print(words)
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
print(sorted_words)
sorted_words + ex25.sort_sentence(sentence)
print(sorted_words) #prints
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)
print(words)