def palindrom(word:str):
    i=0
    while i<int((len(word)/2)):
        if word[i]==word[-i-1]:
            i+=1              
        else:
            print("slovo",word,"-NE palindrom")
            break            
    else:
        print("slovo",word,"-yavlyaetsy palindrom")
    
palindrom("DOVOD")