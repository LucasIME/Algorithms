class Trie:
    def __init__(self, wordList):
        self.root = {}
        self.end = '_end_'
        for word in wordList:
            self.add(word)

    def add(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end] = self.end

    def containsWord(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        if self.end in node:
            return True
        return False


def main():
    wordList = ['foo', 'bar', 'baz', 'barz', 'looked', 'just', 'like', 'her', 'brother']
    trie = Trie(wordList)
    print(trie.root)
    print(trie.containsWord('foo'))
    print(trie.containsWord('f'))
    print(trie.containsWord('bar'))
    print(trie.containsWord('baz'))
    print(trie.containsWord('he'))

main()
