class Playfair:
    def __init__(self, alphabet_start, alphabet_end, slogan, size, df):
        
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
        self.df = ord(df) - self.start
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
                print(self._get(j, i), end = '\t')
            print()

    def _get(self, x, y):
        index = (y % self.size) * self.size + x % self.size
        if index + self.start > self.end:
            return str(index + self.start - self.end)
        else: 
            return str(chr(self.start + self.ralphabet[chr(self.start + index)]))

    def encode(self, target: str):
        result = ''
        i = 0
        dub = False
        while i < len(target):
            s1, s2 = 'a', 'a'
            if dub:
                s1 = self.df
                dub = False
                i -= 1
            else:
                s1 = self._get_index(target[i])

            if (i + 1) == len(target):
                s2 = self.df
            else:
                s2 = self._get_index(target[i+1])
            if s1 == s2:
                s2 = self.df
                dub = True
                i -= 1
            i += 2
            
            x1, y1 = s1 % self.size, s1 // self.size
            x2, y2 = s2 % self.size, s2 // self.size
            if y1 == y2:
                result += self._get(x1 + 1, y1) + self._get(x2+ 1, y2)
                continue
            if x1 == x2:
                result += self._get(x1, y1 + 1) + self._get(x2, y2 + 1)
                continue
            result += self._get(x2, y1) + self._get(x1, y2)
        return result

