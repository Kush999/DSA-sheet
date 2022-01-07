#Find the median 
def find_median(v,n):
	v.sort()
	if n==2:
		return (v[0]+v[1])//2
	elif n%2!=0:
		return v[n//2]
	else:
		return (v[(n//2)-1]+v[n//2])//2

v=[18, 2, 10, 13, 8, 8]
n=len(v)
print(find_median(v,n))