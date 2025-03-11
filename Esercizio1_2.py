def score_word(word, available):
    """
    Compute the score for an acceptable word

	word : word to be scored
	available : string of the available letters
    
    >>> score_word('card', 'ACDLORT')
    1
    >>> score_word('color', 'ACDLORT')
    5
    >>> score_word('cartload', 'ACDLORT')
    15
    """
    points = 0
    if len(word)== 4:
        points += 1
    elif len(word) >4:
        points += len(word)
        lista = []
        for w in word:
            for a in available:
                if w.lower() == a.lower():
                    if (w.lower() in lista) == False:
                        lista.append(w)
        
        if len(lista) == len(available):
            points += 7
    return points

#if __name__ == "__main__":
    import doctest
#doctest.testmod()