def decode(rec):
    data = rec.decode()
    temp1 = data.replace("'", "")
    decoded = temp1.strip('][').split(', ')
    return decoded