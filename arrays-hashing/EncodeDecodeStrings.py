def encode(strs):
    # make large string with all string elements and space
    combined_strs = ""
    for i in range(len(strs)):
        if (i != (len(strs)-1)):
            combined_strs = combined_strs + strs[i] + " "
        else:
            combined_strs = combined_strs + strs[i]
    print(combined_strs)
    return combined_strs


def decode(s):
    out_list = s.split(" ")
    print(out_list)
    return out_list

strs = [""]
print(encode(strs))
