'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, index = 0, occurences = 0):
    
    if len(word) != index:

        if word[index] == "t" and word[index + 1] == "h":
            index += 1
            occurences += 1
        else: 
            new_index = index
            count_th(word, new_index, occurences= 0)
    
    else: 
        return occurences
  
        


word = "pizza is the best food the the"
print(count_th(word))
