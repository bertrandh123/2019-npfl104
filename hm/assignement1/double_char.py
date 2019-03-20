def double_char(char):
  mot=''
  for i in range(len(char)):
    mot+=char[i]*2
  return mot

print("double_char('Azerty-')=='AAzzeerrttyy--' -> "+str(double_char('Azerty-')=='AAzzeerrttyy--'))
