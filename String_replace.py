s = input("Enter a string ")
s1 = ""
s2=""
s3="" #For storing the first character after cn=onversion as well as the final string
c = 0
vowel = ""
vowel_index =0
special_char = "_!#$%^&*'()<>?/\"|}{~:;[]"
first_letter = s[0] #Extracting the first letter
for j in special_char:#5.For special characters (e.g - #, ', ", _, - etc.) replace it with "@"
        s = s.replace(j, '@')
#print(s)
if first_letter.lower() in ('a', 'e', 'i', 'o', 'u'):
    #Checking if the first letter is vowel
    for i in s:
        if i.lower() not in ('a', 'e', 'i', 'o', 'u',' ','@'):#4.No need to replace spaces/blanks with anything.
                s=s.replace(i, first_letter)
    print(s.lower())
    
    
else: #1.When the first letter is not a vowel
    for i in s:
        if i.lower() in ('a', 'e', 'i', 'o', 'u'):
            c=c+1 # Counter for the first vowel
        if c == 1:
            vowel = i
            vowel_index = s.rfind(vowel,1,len(s)) #Storing the index value of the 1st vowel
            s1=s.replace(s[0],i) #Replacing the first character by a vowel
            c=c+1
        
        s2=s1[1:len(s1)]
        s3=s1[0:1]
        for j in s2:#2.Replacing the character which is not a vowel, by the first character
            if j.lower() not in ('a', 'e', 'i', 'o', 'u',' ','@'):
                s2=s2.replace(j, first_letter) 
        
        s2=s2.replace(vowel,first_letter)#3.Replacing every instance of that specific vowel which replaced the first character by the first character
    
    s3=s3 + s2 #Joining the first character with the rest of the string
    
    
print(s3.lower())
