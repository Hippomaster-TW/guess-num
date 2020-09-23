import random
start = input('請決定隨機數字開始值： ')
end = input('請決定隨機數字結束值： ')
start = int(start)
end = int(end)
r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜數字：')
	num = int(num)
	if num == r:
		print('你猜中了！')
		print('這是你猜的第', count, '次') #為了必需表示次數而添加
		break
	elif num > r:
		print('你多猜了！')
	elif num < r:
		print('你少猜了！')
	print('這是你猜的第', count, '次')