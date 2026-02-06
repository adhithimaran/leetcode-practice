def sol(strs):
    strs_alpha = []
    for i in range(len(strs)):
        curr = sorted(strs[i])
        curr_alpha = "".join(curr)
        curr_alpha = curr_alpha.lower()
        strs_alpha.append(curr_alpha)
    
    ana_dict = {}
    for i in range(len(strs)):
        curr_original = strs[i]
        curr_sorted = strs_alpha[i]
        if curr_sorted in ana_dict:
            ana_dict[curr_sorted].append(curr_original)
        else:
            ana_dict[curr_sorted] = [curr_original]

    out = []
    for key, value in ana_dict.items():
        print(value)
        out.append(value)
    return out


strs=["act","pots","tops","cat","stop","hat"]

print(sol(strs))