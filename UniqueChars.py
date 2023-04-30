#Description: Write a program in Python to print the number of unique letters in a string. Only new letters from the string should be counted and not duplicates.

s=input("Enter a String:").lower()
l=[]
for i in s:
	if i in l:
		continue;
	l.append(i)
print("Unique Letters:",end=" ")
print(",".join(l))
