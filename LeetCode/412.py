class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fin = []
        for num in range(1, n+1):
            fizz = not num%3
            buzz = not num%5
            ret_str = ""
            
            ret_str += "Fizz" if fizz else ""
            ret_str += "Buzz" if buzz else ""
            ret_str += str(num) if not len(ret_str) else ""
            fin.append(ret_str)
        return fin
