import os



#讀取購買紀錄
def read_file(filename):
	productlist=[]
	with open(filename,'r',encoding='utf-8') as f:
	    #print("購買紀錄如下"+'\n'+"---------")
	    for line in f:
	    	if '商品,價格' in line:
	    		continue
	    	name,price = line.strip().split(',')
	    	productlist.append([name,price])
	    	print(name+':'+price)
	
	return productlist
#輸入購買項目
def user_input(products):
	while True:
	    name = input('輸入商品名稱')
	    if name == 'q':
	        break
	    price = input('輸入商品價格')
	    price = int(price)

	    #p =[name,price]
	    #productlist.append(p)
	    products.append([name, price])
	    #print(productlist)
	return products
#列出所有購買紀錄
def print_list(products):
	for line in products:
		print(line)
#寫入檔案
def write_file(filename,products):
	with open(filename,'w',encoding='utf-8') as f:
		f.write('商品'+','+'價格'+'\n')
		for line in products:
			f.write(line[0]+','+str(line[1])+'\n')
	return products
def main ():
	filename='products.csv'
	if os.path.isfile(filename):
		products=read_file(filename)
		products=user_input(products)
		print_list(products)
		write_file(filename,products)
	else:
		print('無購買紀錄')

main()