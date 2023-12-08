class Codec:
    def __init__(self):
        self.delimeter = "-"

    def encode(self, strs: list) -> str:
        """Encodes a list of strings to a single string.
        """
        output = ""
        for s in strs:
            s = f"{len(s)}{self.delimeter}{s}"
            output += s
        return output
        

    def decode(self, s: str) -> list:
        """Decodes a single string to a list of strings.
        """
        #using nested loop approach
        j = 0
        str_len = ""
        output = []
        while j < len(s):
            while s[j] != self.delimeter:
                str_len += s[j]
                j += 1
            j += 1
            output.append(s[j:j+int(str_len)])
            j += int(str_len)
            str_len = ""
        return output
        
        # not using two pointer approach
        # output = []
        # i = 0
        # delim_found = False
        # str_len = ""
        # while i < len(s):
        #     if not delim_found:
        #         if s[i] == self.delimeter:
        #             str_len = int(str_len)
        #             delim_found = True
        #             if str_len == 0:
        #                 output.append("")
        #                 delim_found = False
        #                 str_len = ""
        #         else:
        #             str_len += s[i]
        #         i += 1
        #     else:
        #         output.append(s[i:i+str_len])
        #         i += str_len
        #         delim_found = False
        #         str_len = ""
        # return output



        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))