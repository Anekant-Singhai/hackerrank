def siddh(s,a):
	count = 0
	for i in range(len(s)): 
		if (s[i:i+len(a)] == a):  #we use slicing to discard the previous letters so that another pattern forming may be counted

		    count+=1              
	return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = siddh(string, sub_string)
    print(count)