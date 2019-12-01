class Caesar:
    def __init__(self):
        self.alphabet_size = 26
        
    def caesarEncode(self, char, shift):
        if not char.isalpha():
            return char
        lower = char.islower()
        if lower:
            char = char.upper()
        if ord(char) - ord('A') + shift < self.alphabet_size:
            char = chr(ord(char) + shift)
        else:
            char = chr(ord(char) + shift - self.alphabet_size)
        if lower:
            char = char.lower()
        return char

    def formAnswer(self, message, shift):
        shift = shift % self.alphabet_size 
        string = ''.join(map(lambda char: self.caesarEncode(char, shift), message))
        return string
