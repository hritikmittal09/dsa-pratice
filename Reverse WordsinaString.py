def reverseWords(self, s):
        r = s[::-1]
        f = ""
        word =""
        s = False
        for i in r :
           
            if i !=" " :
                word += i
                s = False
            else:
                if not s :
                    f+= word[::-1] +" "
                    word = ""
                    s = True
        f += word[::-1]        
        f = f.strip()
        print(f)
        return f        
        """
        :type s: str
        :rtype: str
        """