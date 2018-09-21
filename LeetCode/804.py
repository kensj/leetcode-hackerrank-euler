class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        fin = {}
        
        for word in words:
            morse = ""
            for letter in word:
                morse += code[alphabet.index(letter)]
            fin[morse] = fin.get(morse, 0) + 1
        
        total = 0
        for key in fin:
            total += 1
        return total
                