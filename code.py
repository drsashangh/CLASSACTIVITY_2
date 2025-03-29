def find_cube_pairs(target): #colon error
    solutions = [] # no semicolon required
    max_num = round(target ** (1/3)) #3 asteriks  and target not targ

    for a in range(1, max_num + 1): #colon error and range not ranges
        for b in range(a, max_num + 1): #colon error and range not ranges
            if a**3 + b**3 == target : #target name error, 3 asteriks error and colon error
                solutions.append((a, b));#no semicolon req and name error solutions not sol
    return solutions #name error initially it was sol

pairs = find_cube_pairs(1729)#no comma required
print("Valid cube pairs for 1728:")#not printf its print and no comma
for a, b in pairs: #colon error and pairs not pair
    print(f" → {a}³ + {b}³ = {a**2} + {b**2} = 1728")
#not printf its print