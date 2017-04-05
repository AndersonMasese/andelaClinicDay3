def words(myWord):
    #sort the words while checking for tabs, spaces and line breaks by 
    #calling functions replace, and split
    try:
        wordLength = myWord.replace('\t', ' ').replace('\n', ' ').split(' ')
        wordCounter = {}
        for iterator in wordLength:
            if wordCounter.get(iterator, None) is None:
                wordCounter[iterator] = 1
            else:
                wordCounter[iterator] = wordCounter[iterator] + 1
        return wordCounter
    except IOError:
        print(function execution failed)
    finally:
        print(Done)