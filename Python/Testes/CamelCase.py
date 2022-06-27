def CamelCase(strParam):
  a = ''
  count = 0
  frase = strParam
  for c in frase: 
    if not c.isalpha():
        frase = frase.replace(c,' ')
  for i in frase.split():
    palavra = i.lower()
    print(palavra)
    if count > 0:
      a += palavra.title()
    else:
        a += palavra
    count += 1
  # code goes here
  return a


# keep this functi'on call here 
a = CamelCase('cats AND*Dogs-are Awesome')
print(a)