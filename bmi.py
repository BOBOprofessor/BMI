l = input('請輸入你的身高(公尺)')
W = input('請輸入你的體重(公斤)')
l = float(l)
W = float(W)
bmi = W / (l * l)
if bmi < 18.5:
	print('你的bmi是', bmi, '你目前體重過輕喔!!')
elif bmi >= 18.5 and bmi < 27:
	print('你的bmi是', bmi, '你目前非常健康')
elif bmi >= 24 and bmi <= 27:
	print('你的bmi是', bmi, '你目前體重過重喔!!')
elif bmi >= 27 and bmi < 30:
	print('你的bmi是', bmi, '你目前體重輕度肥胖喔!!')
elif bmi >= 30 and bmi < 35:
	print('你的bmi是', bmi, '你目前體重中度肥胖喔!!')
elif bmi >= 35:
	print('你的bmi是', bmi, '你目前體重度肥胖喔!!你這個死胖子')
