 s1 = ''
        s2 = ""
        t = l1
        while t :
            s1 += str( t .val)
            t = t.next
        t = l2
        while t :
            s2 += str(t .val)
            t = t.next
        s =int(s1 [::-1]) + int(s2[::-1])
        s = str(s)[::-1]
        print(s)
        h = None
        t=None
        for i in s:
            n = ListNode(int(i))
            if h is None :
                h = n
                t = h
            else :
                t. next = n
                t  = n
        return h            


                

        