def hash(list,sum):

    d={}
    for i,e in enumerate(list):
        if sum-e in d:
            print((list[d.get(sum-e)],list[i]))
        d[e]=i

list=[2,3,5,7,9,4]
sum=11
hash(list,sum)
