import re
A = open('blocklist.xml')
txt = A.read()
#%%
##### --- Question 1 --- #####
findword1=u'(<emItem blockID="i.*\d".*>)'
pattern = re.compile(findword1)
results = pattern.findall(txt)
count = 0  
for result in results :  
    print (result)
    count+=1
    
findword1=u'(<emItem blockID="d.*\d".*>)'
pattern = re.compile(findword1) 
results =  pattern.findall(txt)  
for result in results :  
    print (result)
    count+=1
    
print("The number of blockID is:",count)    
    
#%%
##### --- Question 2 --- #####
findword1=u'(<emItem.*id="[^(\/^{}|)].*com".*>)'
pattern = re.compile(findword1)
results = pattern.findall(txt)
count = 0  
for result in results :  
    print (result)
    count+=1
    
findword1=u'(<emItem.*id="[^(\/^{}|)].*org".*>)'
pattern = re.compile(findword1)
results =  pattern.findall(txt)  
for result in results :  
    print (result)
    count+=1

print("The number of id is: ",count)
