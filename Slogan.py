class Slogan:
    def __init__(self, alphabet_start, alphabet_end, slogan):
        self.encode_table = {}
        self.decode_table = {}
        key_set = set()
        key = ''
        for i in range(len(slogan)):
            if not slogan[i] in key_set:
                key += slogan[i]
                key_set.add(slogan[i])

        
        for i in range(ord(alphabet_start), ord(alphabet_end) + 1):
            si = i - ord(alphabet_start)
            if si < len(key):
                self.encode_table[chr(i)] = key[si]
                self.decode_table[key[si]] = chr(i)
            else:
                for j in range(ord(alphabet_start), ord(alphabet_end) + 1):
                    if not chr(j) in key_set:
                        key_set.add(chr(j))
                        self.encode_table[chr(i)] = chr(j)
                        self.decode_table[chr(j)] = chr(i)
                        break
        
                
    
    def encode(self, target:str):
        result=""
        for i in range(len(target)):
            result += self.encode_table[target[i]]
        return result

    def decode(self, target:str):
        result=""
        for i in range(len(target)):
            result += self.decode_table[target[i]]
        return result