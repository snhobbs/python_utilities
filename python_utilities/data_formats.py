# Breakup lines into key value pairs
# Any value not in a key value pair and has none white space characters is added to a list
def ReadKeyValueDataFile(string, header_char='#', delim = ':'):
    lines = string.split("\n")
    key_value = list()
    data = list()
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue # skip line
        if line[0] == header_char:
            split = line.split(delim)
            key = split[0].strip().lstrip(header_char)
            value = delim.join(split[1:])
            key_value.append((key, value))
        else:
            data.append(line)
    return key_value, data