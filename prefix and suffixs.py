class WordFilter:
    def __init__(self, words):
        self.trie = {}
        for weight, word in enumerate(words):
            word_hash = word + '#' + word
            n = len(word)
            # insert all suffix#word combinations for this word
            for i in range(n + 1):
                cur = self.trie
                # key = suffix (word[i:]) + '#' + word
                key = word_hash[i:i + n + 1 - i]  # word[i:] + '#' + word
                node = self.trie
                for ch in word[i:] + '#' + word:
                    if ch not in node:
                        node[ch] = {}
                    node = node[ch]
                    node['weight'] = weight  # always overwrite -> keeps latest (largest) index

    def f(self, prefix, suffix):
        node = self.trie
        key = suffix + '#' + prefix
        for ch in key:
            if ch not in node:
                return -1
            node = node[ch]
        return node.get('weight', -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)