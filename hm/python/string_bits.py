def string_bits(char):
  mot=''
  l=len(char)
  if l%2==0:
    for i in range(l//2):
      mot+=char[2*i]
  else:
    for i in range(1+l//2):
      mot+=char[2*i]
  return mot


print("string_bits('Hello') =='Hlo' -> "+str(string_bits('Hello') =='Hlo'))

