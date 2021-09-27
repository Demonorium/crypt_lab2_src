class Cesar:
    def __init__(self, alphabet_start, alphabet_end, offset):
        self.alphabet_start=ord(alphabet_start)
        self.alphabet_len=ord(alphabet_end) - ord(alphabet_start) + 1
        self.offset = offset
    
    def encode(self, target:str):
        result=""
        for i in range(len(target)):
            if target[i] == ' ':
                result += ' '
                continue
            result += chr(
                self.alphabet_start
                +(ord(target[i])-self.alphabet_start+self.offset) 
                    % self.alphabet_len
                )
        return result

    def decode(self, target:str):
        result=""
        for i in range(len(target)):
            if target[i] == ' ':
                result += ' '
                continue
            result += chr(
                self.alphabet_start
                +(ord(target[i])-self.alphabet_start-self.offset) 
                    % self.alphabet_len
                )
        return result