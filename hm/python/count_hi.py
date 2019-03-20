def count_hi(char):
  S=0
  for i in range(len(char)-1):
    if char[i:(i+2)]=='hi':
      S+=1
  return S

print("count_hi('hihihihihi')==5 -> "+str(count_hi('hihihihihi')==5)) 

