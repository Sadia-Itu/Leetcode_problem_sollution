def isPalindrom(s):
    start=0
    end=len(s)-1
    s= "".join(char for char in s if char.isalnum())
    s.lower()
    
    while start<end:
          if s[start]!=s[end]:
             return False
          
          start+=1
          end-=1   
    return True



palindromcheck=isPalindrom("madam")
print(palindromcheck)