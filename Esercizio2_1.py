def clean_book(source_filename, destination_filename):
    """
    Remove everything except the book itself. Return the number of lines of the cleaned book

    source_filename : where to find the book to be cleaned
    destination_filename : where to store the cleaned book

    >>> clean_book("stevenson.txt", "stevenson_clean.txt")
    2530
    """
    f_source = open(source_filename)
    f_destination = open(destination_filename,"w")

    start = False
    end = False
    total_line = 0

    for line in f_source:
        if line[0:len(line)-1] == "*** END OF THIS PROJECT GUTENBERG EBOOK THE STRANGE CASE OF DR. ***":
            end = True
        if start == True and end == False:
            f_destination.write(line)
            total_line+=1
        if line[0:len(line)-1] == "*** START OF THIS PROJECT GUTENBERG EBOOK THE STRANGE CASE OF DR. ***":
            start = True
        
    return total_line


if __name__ == "__main__":
    import doctest
doctest.testmod()