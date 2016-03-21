def Strstr(str1,str2):
	for index in range(len(str1)):
		t=index
		for num in range(len(str2)):
			if str1[t]!=str2[num]:
				break
			else:
				t+=1
		if num==len(str2)-1:
			return index
	return -1
str1=raw_input()
str2=raw_input()
a=Strstr(str1,str2)
print a
