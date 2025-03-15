def find_short(s):
    words = s.split()
    I = min(len(word)for word in words) 
    return I