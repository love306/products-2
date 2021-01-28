#載入作業系統函式庫
import os

def check_file(filename):

	#檢察檔案是否存在
	if os.path.isfile(filename):
			print('找到檔案')
	else:
			print('沒有找到檔案喔')

def read_file(filename):
	products = []	
	#讀取檔案
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			#加入continue略過商品價格，不加入到products清單中
			if '商品,價格' in line:
				continue
			#先strip多餘空格與\n換行符號，再以讀取資料內的「,」為分割，並且一次存在兩個變數中
			name, price = line.strip().split(',')
			#存入成二維清單
			products.append([name, price])
	#印出清單內容
	print(products)
	return products

def user_input(products):	
	#輸入資料並存入清單
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		products.append([name, price])
	print(products)
	return products

def print_products(products):	
	#印出每個products的資料
	for p in products:
		print(p[0], '的價格為', p[1])

def write_file(filename, products):
	#寫入檔案
	with open(filename, 'w', encoding='utf-8') as f:
		#在第一行加入標籤
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')
#加入開關
def on_off(on=True):
	while True:
		#自定義開啟檔名
		filename = input('請輸入需開啟之檔案（含副檔名）: ')
		if os.path.isfile(filename):
			print('找到檔案')
			products = read_file(filename)
			products = user_input(products)
		else:
			print('沒有找到檔案喔')
			break
		#決定讀取後動作
		write_or_print = input('列出清單內容並寫入檔案輸入1，直接寫入檔案輸入2，只列出清單內容輸入3: ')
		if write_or_print == '1':
			print_products(products)
			write_file(filename, products)
			break
		elif write_or_print == '2':
			write_file(filename, products)
			break
		elif write_or_print == '3':
		 	print_products(products)
		 	break
on_off()





