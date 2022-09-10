

def guess_next_letter(pattern, used_letters=[], word_list=['about', 'abound']):
    """Returns a letter from the alphabet.
    Input parameters:
				pattern: current state of the game board, with underscores "_" in the
            places of spaces (for example, "____e", that is, four underscores
            followed by 'e').
        used_letters: letters you have guessed in previous turns for the same
            word (for example, ['a', 'e', 's']).
        word_list: list of words from which the game word is drawn.
    """
    pattern_list = list(pattern)
    search_list = word_list

    for i in range(len(pattern_list)):
        if pattern_list[i] != '_':
            # used_letters.append(pattern_list[i])
            if search_list != None:
                search_list = search_words(pattern_list[i], search_list)

    result = []
    for word in search_list:
        result.append(output_word(word, used_letters))

    return result


def search_words(letter, word_list):
    search_word_list = []
    length = len(word_list)
    for i in range(length):
        word_length = len(word_list[i])
        for j in range(word_length):
            if word_list[i][j] == letter:
                search_word_list.append(word_list[i])
                break

    return search_word_list

def output_word(word, used_letters):
    word_length = len(word)
    result = ""
    for i in range(word_length):

        if is_exists(word[i], used_letters):
            result += word[i]
        else:
            result += '_'

    return result

def is_exists(letter, used_letters):
    for forletter in used_letters:
        if letter == forletter:
            return True
    return False

def test_function_should_return_something():
	pattern = "____e"
	used_letters = list("abcde")
	word_list = ['about','abcde','isnot']
	assert guess_next_letter(pattern, used_letters, word_list) is not None

if __name__ == '__main__':

    word_list = ['about', 'abcde', 'likes', 'title']
    used_letters = []
    limit = 10
    i = 0
    while i < limit:
        pattern = input('请输入字母：')
        if not pattern.isalpha():
            print('请输入a-z的字母')
            continue
        used_letters.append(pattern)
        print('使用过的字母')
        print(used_letters)
        words = guess_next_letter(pattern, used_letters, word_list)

        if len(words) > 0:
            for w in words:
                print(w)
        else:
            print('false')
        i += 1

    print('输入次数达到上限')
