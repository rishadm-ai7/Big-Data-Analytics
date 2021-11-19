@outputSchema("num:long")

def get_len(data):
    char={}.join(chr(x) for x in data)
    return len(char)