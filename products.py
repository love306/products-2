products = []
#讀取檔案
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		#加入continue略過商品價格，不加入到products清單中
		if '商品,價格' in line:
			continue
		#先strip多餘空格與\n換行符號，再以讀取資料內的「,」為分割，並且一次存在兩個變數中
		name, price = line.strip().split(',')
		#存入成二維清單
		products.append([name, price])
print(products)
#輸入資料並存入清單
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)
#印出每個products的資料
for p in products:
	print(p[0], '的價格為', p[1])
#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	#在第一行加入標籤
	f.write('商品,價格\n')

	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
