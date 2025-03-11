def check_word(word, avaible, required):
    
    """
    Check whether a word is acceptable

	word : word to check
	available : string of seven available letters
	required : string of the single required letter
    
    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
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
#if __name__ == "__main__":
    import doctest
#doctest.testmod()

#print(check_word('color', 'ACDLORT', 'R'))

            