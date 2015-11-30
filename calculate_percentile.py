#input array
m_a=[82,89,94,110,74,122,112,95,100,78,65,60,90,83,87,75,114,85,69,94,124,115,107,88,97,74,72,68,83,91,90,102,77,125,108,65]

#percentile value, example 25 percentile
p=.75
#number of samples
n=len(m_a)
k=n*p
#sort the array
m_a.sort()

#check if k is an integer
if(k-int(k) !=0):
	k=int(k)+1
	print(m_a[k-1])

else:
	ans= ((m_a[int(k)-1] +m_a[int(k)])/2)
	print(ans)
