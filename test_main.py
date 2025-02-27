from main import *   

### PART One

def test_word_count_map():
    result = word_count_map('i am sam i am')
    expected = [('i', 1), ('am', 1), ('sam', 1), ('i', 1), ('am', 1)]
    print("Result:", result)
    print("Expected:", expected)
    assert result == expected

    
def test_word_count_reduce():
    result = word_count_reduce(['i', [1,1,1]])
    expected = ('i', 3)
    print("Result:", result)
    print("Expected:", expected)
    assert result == expected

def test_word_count():
    result = run_map_reduce(word_count_map, word_count_reduce, ['i am sam i am', 'sam is ham'])
    expected = [('am', 2), ('ham', 1), ('i', 2), ('is', 1), ('sam', 2)]
    print("Result:", result)
    print("Expected:", expected)
    assert result == expected

### PART TWO ###

def test_sentiment_map():
    result = sentiment_map('it was a terrible waste of time')
    expected = [('negative', 1), ('negative', 1)]
    print("Result:", result)
    print("Expected:", expected)
    assert result == expected

    
def test_sentiment():
    docs = [
        'it was not great but not terrible',
        'thou art a boil a plague-sore or embossed carbuncle in my corrupted blood',
        'it was a sockdolager of a good time'
    ]
    result = run_map_reduce(sentiment_map, word_count_reduce, docs)
    expected = [('negative', 3), ('positive', 3)]
    print("Result:", result)
    print("Expected:", expected)
    assert result == expected


# Add this at the end of the file to actually run the tests
# seperate testing method for Final check 
# printing results for each test to verify they are producing correct output.
# all tests passed only outputted if every test runs without exception.
if __name__ == "__main__":
    print("Testing word_count_map:")
    test_word_count_map()
    print("\nTesting word_count_reduce:")
    test_word_count_reduce()
    print("\nTesting word_count:")
    test_word_count()
    print("\nTesting sentiment_map:")
    test_sentiment_map()
    print("\nTesting sentiment:")
    test_sentiment()
    print("\nAll tests passed!")
