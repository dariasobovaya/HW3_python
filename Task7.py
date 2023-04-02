slovo = input()
proverka1 = slovo.find('f')
proverka2 = slovo.rfind('f')
if proverka1 == proverka2:
   print(proverka1)
elif proverka1 != proverka2:   
   print(proverka1, proverka2)
