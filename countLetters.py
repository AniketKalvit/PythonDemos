def countLetters(str):
    counts={}
    
    for ch in str:
        if ch.isalpha():
            lower=ch.lower()
            
            if lower in counts:
                counts[lower]+=1
            else:
                counts[lower]=1
                
    return counts

input="w3resource"

result=countLetters(input)
print(result)