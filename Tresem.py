class Tresem:
    def __init__(self, alphabet_start, alphabet_end, slogan, size):
        key_set = set()
        key = ''
        for i in range(len(slogan)):
            if not slogan[i] in key_set:
                key += slogan[i]
                key_set.add(slogan[i])
        
        self.alphabet = {}
        self.ralphabet = {}
        self.start = ord(alphabet_start)
        self.end = ord(alphabet_end)
        self.asize = self.end - self.start

        for i in range(ord(alphabet_start), ord(alphabet_end) + 1):
            si = i - ord(alphabet_start)
            if si < len(key):
                self.alphabet[key[si]] = si
                self.ralphabet[chr(i)] = ord(key[si]) - self.start
            else:
                for j in range(ord(alphabet_start), ord(alphabet_end) + 1):
                    if not chr(j) in key_set:
                        key_set.add(chr(j))
                        self.alphabet[chr(j)] = i - self.start
                        self.ralphabet[chr(i)] = j - self.start
                        break
        self.size = size
    def _get_index(self, char):
        return self.alphabet[char]

    def _get_r_index(self, char):
        return self.ralphabet[char]
    def print(self):
        for i in range(self.size):
            for j in range(self.size):
                char = self.start + i*self.size + j
                if char > self.end:
                    print('_', end = '\t')
                else:
                    char = self.start + self._get_r_index(chr(char))
                    print(chr(char), end = '\t')
            print()

    def encode(self, target: str):
        result = ''
        for i in range(len(target)):
            index = self._get_index(target[i])
            j = index // self.size + 1
            result += chr(self.start + (self.size*j + index % self.size) % self.asize)
        return result