print(''' 
Частота появления букв английского алфавита:

\t\t a = 8.17% \t n = 6.75% 
\t\t b = 1.49% \t o = 7.51%  
\t\t c = 2.78% \t p = 1.93%
\t\t d = 4.25% \t q = 0.10%
\t\t e = 12.7% \t r = 5.99%
\t\t f = 2.23% \t s = 6.33%
\t\t g = 2.02% \t t = 9.06% 
\t\t h = 6.09% \t u = 2.76%
\t\t i = 6.97% \t v = 0.98%
\t\t j = 0.15% \t w = 2.36% 
\t\t k = 0.77% \t x = 0.15%
\t\t l = 4.03% \t y = 1.97%
\t\t m = 2.41% \t z = 0.05%
''')

name = input("File-name: ")
text = ""

try:
	with open(name,"r") as file:
		original = file.read()
except FileNotFoundError:
	print("Файл не найден!")
else:
	original=original.lower()
	
	for i in original:
		if i >="a" and i <="z":
			text += i
		else: 
			pass

dict = {i for i in text}

def check(words, char):
	k = 0
	for i in words:
		if i == char: k += 1
	return k

percent = 100
length = len(text) 
var = 0
print('''
Частота появления букв в тексте: 
''')

for symbol in dict:
	stat = percent * check(text,symbol) / length
	if var%2 == 0:
		print("\t\t{0} - {1}%\t".format(symbol,round(stat,2)),end=""); var += 1
	else:
		print("{0} - {1}%".format(symbol,round(stat,2))); var += 1

if var%2 == 0: print()
else: print("\n")