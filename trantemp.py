choose=input('請輸入轉換類別(1:攝氏轉華氏2:華氏轉攝氏)：')
temp=input('請輸入溫度:')

if choose=='1':
    trantemp=float(temp)*9/5+32
else:
    trantemp=(float(temp)-32)/9*5
print(trantemp)