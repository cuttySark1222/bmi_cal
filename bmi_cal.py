# BMI 计算器
# 并根据结果来显示体脂比是否正常
height_in_cm = input('请输入身高（公尺）： ')
weight_in_kg = input('请输入体重（公斤）： ')

height_in_cm = float(height_in_cm)
weight_in_kg = float(weight_in_kg)

bmi = weight_in_kg / height_in_cm ** 2 # BMI 计算公式

print(f"Your BMI is {bmi:.2f}") # BMI 打印数值保留小数点后两位

if bmi < 18.5:
	print("体重过轻。")
elif bmi >= 18.5 and bmi < 24:
	print("体重正常。")
elif bmi >= 24 and bmi < 27:
	print("体重过重。")
elif bmi >= 27 and bmi < 30:
	print("轻度肥胖。")
elif bmi >= 30 and bmi < 35:
	print("中度肥胖。")
else:
	print("重度肥胖。")