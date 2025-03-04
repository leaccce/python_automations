import os
os.chdir('Projects/word_counter')
def counter(filename):
    with open(filename,'r') as f:
        t=f.read().strip().split()
        g=set(t)
        for i in g:
            N=t.count(i)
            print(f"{i} - {N}")

        

counter('readthis.txt')
