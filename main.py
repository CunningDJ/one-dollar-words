from os import path

pwd = path.abspath(path.dirname(__file__))
langDir = path.join(pwd, 'english-language')
langFile = path.join(langDir, 'words.txt')

letters_raw = 'abcdefghijklmnopqrstuvwxyz'
uppLetters = list(letters_raw.upper())
lowLetters = list(letters_raw)

nums = list(range(1,27))

pointMap = dict([(letter, num) for letter, num in zip(lowLetters+uppLetters, nums+nums)])


def main():
    TARGET_SCORE = 100  # $1.00 == 100 cents

    print('Checking all English words for words that are worth $1.00:')

    with open(langFile, 'r') as f:
        wordMatchCounter = 0
        for word in f:
            word = word.strip()
            if findScore(word) == TARGET_SCORE:
                print(word)
                wordMatchCounter += 1
            else:
                #print('XXX')
                pass
        print('TOTAL ONE DOLLAR WORDS:', wordMatchCounter)



def findScore(word):
    totalScore = 0
    for letter in word:
        try:
            totalScore += pointMap[letter]
        except KeyError as e:
            continue
    return totalScore



if __name__ == "__main__":
    main()
