# -*- coding: utf-8 -*-
"""ETF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NFb2ferWkM0GunTtGdQpKqxyWKj7TC3d
"""

!pip install gspread

import requests
#import time

res = requests.get("https://www.twse.com.tw/exchangeReport/TWTASU?response=json&date=&_=1594474165127")
db = res.json()
#col = len(res.json())
row = len(db['data'])-2
i =0
print_list = []    
while i<=row:
  for j in range(1,5,2):
    k = 0
    value = []
    val = db['data'][i][j] 
    # 抓值
    while k<=len(val)-1:
      if val[k].isdigit():
        value.append(int(val[k])) 
      k=k+1
    if len(value)>=5:
        print("warning!")
        print(db['data'][i])
        print_list.append(db['data'][i])
        
        break
  i=i+1
print("請到google sheet上查看")
length=len(print_list)
# for a in print_list:
#   print(print_list[0][0])
#google sheet
import gspread
from google.colab import auth
from oauth2client.client import GoogleCredentials
auth.authenticate_user()
credentials = GoogleCredentials.get_application_default()
gc = gspread.authorize(credentials)
from pydrive.auth import GoogleAuth
from google.colab import auth
from oauth2client.client import GoogleCredentials
gauth = GoogleAuth()
auth.authenticate_user()
gauth.credentials = GoogleCredentials.get_application_default()
gc = gspread.authorize(gauth.credentials)
sh = gc.create('My_Sheet')
sh = gc.open('My_Sheet')
worksheet = sh.add_worksheet(title='worksheet_1', rows= length, cols='5')
# 依照工作表名稱選取
worksheet = sh.worksheet('worksheet_1')

# # 依標籤
# # worksheet.update_acell('B1', 'Bingo!')

# new_row = ["See Google Sheets and Pyton", "on", "Youtube. Thank you Twilio and friends"]
# index=4 
# worksheet.insert_row(new_row,index)
# row_result = worksheet.row_values(4)
#print(row_result)
new_row =[]
index=5 
for a in range(length):
  new_row=db['data'][a]
  worksheet.insert_row(new_row,index)
  row_result = worksheet.row_values(5)
  print(row_result)


# worksheet.insert_row(new_row,index)
# row_result = worksheet.row_values(4)
# print(row_result)
    
    

# # 依座標
# for a in range(length):
#   for b in range(5):
    
#     worksheet.update_cell(a+1, b+1,db['data'][a][b] )

# # # 指定範圍
# cell_list = worksheet.range('A1:C7')
# for cell in cell_list:
#     cell.value = 'O_o'
# worksheet.update_cells(cell_list)

#下載excel
# import pygsheets
# gc = pygsheets.authorize(service_file='/Users/max/Desktop/Google python.json')
# output = open('data.xls','w',encoding='utf_8')
# output.write('證券名稱\t融券賣出成交數量\t融券賣出成交金額\t借券賣出成交金額\n')
# for i in range(len(print_list)):
# 	for j in range(len(print_list[i])):
# 		output.write(str(print_list[i][j]))    #write函数不能写int类型的参数，所以使用str()转化
# 		output.write('\t')   #相当于Tab一下，换一个单元格
# 	output.write('\n')       #写完一行立马换行
# output.close()


#證券名稱	融券賣出成交數量	融券賣出成交金額	借券賣出成交數量	借券賣出成交金額

import requests
#import time

res = requests.get("https://www.twse.com.tw/exchangeReport/TWTASU?response=json&date=&_=1594474165127")
db = res.json()
print(db)

res.json()

val='4,001,200'
print(val[1])
i = 0
while i<=len(val)-1:
  if val[i].isdigit():
     print(int(val[i]))
     print('aa',i)
  i = i+1
#print(a.type())

val = db['data'][1080][4]
print(val)
k=0
value = []

while k<=len(val)-1:
    if val[k].isdigit():
      value.append(int(val[k]))
    a=len(value) 
    if a>=4:
      print("warning!")
      break
    k=k+1
print(value)

val = "10.10"
if val.isdigit():
  print(int(val))

db = res.json()

len(res.json())

len(db['data'])

db['data']

db['data'][0][4]

for j in range(1,4):
  print(j)

for j in range(1,5,2):
  print(j)

