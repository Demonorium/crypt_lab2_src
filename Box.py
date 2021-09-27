class Box:
    def __init__(self, alphabet_start, alphabet_end, size):
        self.start = ord(alphabet_start)
        self.end = ord(alphabet_end)
        self.size = size

    def print(self):
        for i in range(self.size):
            for j in range(self.size):
                char = self.start + i*self.size + j

                if char > self.end:
                    print('_', end = '\t')
                else:
                    print(chr(char), end = '\t')
            print()

    def encode(self, target: str):
        result = ''
        for i in range(len(target)):
            char = ord(target[i]) - self.start
            result += str(char% self.size + 1) + str(char // self.size + 1) + ' '
        return result