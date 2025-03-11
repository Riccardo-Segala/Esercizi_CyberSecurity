def count_unique_words(filename):
    """
    Count the number of unique words in a file

    filename : path to a file

    >>> count_unique_words("stevenson_clean.txt")
    6039
    """
    
    unique_words=[]
  
    for line in open(filename, "r"):
        # Rimuovi eventuali spazi bianchi all'inizio e alla fine della riga
        line = line.strip()
        
        # Usa split() per ottenere le parole, separando per spazi
        words = line.split()

        for w in words:
            if w not in unique_words:
                unique_words.append(w)
    
    return len(unique_words)    

if __name__ == "__main__":
    import doctest
doctest.testmod()
        
        
 
#print(count_unique_words("stevenson_clean.txt"))