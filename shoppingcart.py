productlist=[]
while True:
    name = input('輸入商品名稱')
    if name == 'q':
        break
    price = input('輸入商品價格')
    price = int(price)

    #p =[name,price]
    #productlist.append(p)
    productlist.append([name, price])
#print(productlist)

for line in productlist:
	print(line)
with open('products.csv','w') as f:
	f.write('商品'+','+'價格'+'\n')
	for line in productlist:
		f.write(line[0]+','+str(line[1])+'\n')