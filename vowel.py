ch=input()
if ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u'or ch=='A'or ch=='E'or ch=='I'or ch=='O'or ch=='U':
    print("Vowel")
elif ord(ch)>=97 and ord(ch)<=117 or ord(ch)>=65 and ord(ch)<=90:
    print("Consonant")
else:
    print("invalid")


