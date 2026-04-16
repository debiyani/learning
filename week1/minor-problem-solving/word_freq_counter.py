subject = ['dsa','dsa','os','os','ai','ai','dsa','ai','dsa','os','os','os','os','oop','.net']
freq={} #creating empty dict to store frequency
for sub in subject:
    if sub in freq:
        freq[sub] +=1
    else:
        freq[sub] =1
print(freq)
    
