def LongestWord(sen):
  a = 0
  for i in sen.split():
    string = ''.join(j for j in i if j.isalpha())
    if a < len(string):
      texto = string
  # code goes here
  return texto

# keep this functi'on call here 
a = LongestWord('fun&!! time')
print(a)