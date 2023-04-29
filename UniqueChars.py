s=input().lower()
l=[]
for i in s:
	if i in l:
		continue;
	l.append(i)
print(",".join(l))
