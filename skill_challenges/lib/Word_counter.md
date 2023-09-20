# EXAMPLE

//should this be a class??\\

1. Describe the problem:
    As a user
    So that I can manage my time
    I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

2. Design the Function Signature
    def get word_count (NB may not be worth making into a function)
        parameters= 1 text string
        returns: number of words

    def find how many minutes (i.e. sets of 200 words) and remainder words
        takes number of words as arg
        returns full mins and remainder seconds as tuple
        NB make sure it rounds /up/ to nearest second

    gives the user a string with "It will take x mins and y seconds"



To note: do you want to have minute and minutes/ second and seconds pluralising appropriately??