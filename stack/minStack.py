class MinStack(object):

    def __init__(self):
        self. s = []
        self .m = []
        

    def push(self, val):
        if len(self.m) == 0 or val <= self.m[-1]:
            self.m.append(val)
        self.s.append(val)
        
        

    def pop(self):


      
        
         if self.s:  # Ensure stack is not empty before popping
            e = self.s.pop()
            if self.m and e == self.m[-1]:  # Check min stack before popping
                self.m.pop()

        

    def top(self):
         
        if self.s:  # Check if stack is not empty
            return self.s[-1]
        return None 
        
        

    def getMin(self):
        if self.m:  # Check if min stack is not empty
            return self.m[-1]
        return None  # R
        
         