class Solution:

    def encode(self, strs: List[str]) -> str:
        # we are given a list of string. 
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        return result
            


    def decode(self, s: str) -> List[str]:
        # we are given one long string to decode 
        # ex. 2#hi5#tacos
        result = []
        index = 0

        # go over the whole string s
        while index < len(s):
            # we want to find the start of the index
            findKeyword = index
            while s[findKeyword] != "#":
                findKeyword += 1
            length = int(s[index:findKeyword])
            result.append(s[findKeyword+1:findKeyword+1+length])
            index = findKeyword +1 + length
        return result



            


        

