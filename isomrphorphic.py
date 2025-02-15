def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        z = {}
        mapped_values = set()
        
        for char_s, char_t in zip(s, t):
            if char_s in z:
                if z[char_s] != char_t:
                    return False
            else:
                if char_t in mapped_values:  # Prevent many-to-one mapping
                    return False
                z[char_s] = char_t
                mapped_values.add(char_t)

        return True