```py



'''两个集合是否相等（元素相同，就相等）'''
s={10,20,30,40}
s2={20,30,40,10}
print(s==s2) #True
print(s!=s2) #False

'''一个集合是否是另一个集合的子集'''
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
print(s2.issubset(s1)) #True
print(s3.issubset(s1)) #False

'''一个集合是否是另一个集合的超集'''
print(s1.issuperset(s2)) #True
print(s1.issuperset(s3)) #False

'''两个集合是否含有交集'''
print(s2.isdisjoint(s3)) #False 有交集False disjoint是没有交集的意思
s4={100,200,400}

print(s2.isdisjoint(s4)) #True 没有交集为True


```
