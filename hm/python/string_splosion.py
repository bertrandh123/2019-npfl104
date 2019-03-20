def string_splosion(mot):
  char=''
  l=len(mot)
  for i in range(l):
    char+=mot[:(i+1)]
  return char

print("string_splosion('Code') =='CCoCodCode' -> "+str(string_splosion('Code') =='CCoCodCode'))
