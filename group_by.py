import itertools

def get_groups(nums):
    inp = map(int, list(nums))
    out = [(len(list(g)), k) for k,g in itertools.groupby(inp)]
    print('7', 'out', out)
    print(*out, sep=' ')
        
get_groups('1222311')