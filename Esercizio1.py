def check_word(word, avaible, required):
    if len(word)<4 :
        return False
    else:
        check_required = False
        counter = 0
        for letter in word:
            if letter.lower() == required.lower():
                counter += 1
        if counter == 0:
            return False
    
        for letter in word:
            counter = 0
            for letter_avaible in avaible:
                if letter.lower() == letter_avaible.lower():
                    counter += 1
            if counter == 0:
                return False
        return True

print(check_word('color', 'ACDLORT', 'R'))

            