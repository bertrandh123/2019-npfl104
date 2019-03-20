def cat_dog(char):
  cat,dog=0,0
  for i in range(len(char)-2):
    if char[i:(i+3)]=='cat':
      cat+=1
    if char[i:(i+3)]=='dog':
      dog+=1
  return cat==dog


print("cat_dog('catchiendogchat')==True"+" -> "+str(cat_dog('catchiendogchat')==True))


