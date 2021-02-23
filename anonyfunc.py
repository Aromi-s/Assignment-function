terms=10
result=list(map(lambda x:2**2,range(terms)))
print("The total terms are:",terms)
for i in range(terms):
	print("Raised to power",i,"is",result[i])
