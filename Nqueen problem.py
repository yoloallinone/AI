from itertools import permutations
N=4
sol=0
cols = range(N)
for combo in permutations(cols):                      
    if N==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
        sol += 1          
        print("\n".join(' . ' * i + ' Q ' + ' . ' * (N-i-1) for i in combo) + "\n\n")

print("Found ",sol," solutions" )
