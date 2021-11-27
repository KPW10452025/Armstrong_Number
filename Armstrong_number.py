from functools import reduce

def tool_function_01(num):
    if num == 0:
        return []
    else:
        return [num % 10] + tool_function_01(num // 10)

def check_number(number):
    digits = tool_function_01(number)
    if reduce(lambda sum, d: sum + d ** len(digits), digits, 0) == number:
        return True
    else:
        return False

def show_Armstrong(n):
    Armstrong_number_list = []
    for i in range(0, 10 ** n):
        if check_number(i):
            Armstrong_number_list.append(i)
    return Armstrong_number_list

print("歡迎來到「阿姆斯壯數」查詢系統！")
print("阿姆斯壯數：")
print("在數論中，阿姆斯壯數（Armstrong number）")
print("也被稱為超完全數字不變數（pluperfect digital invariant, PPDI）")
print("自戀數、自冪數、水仙花數（Narcissistic number）")
print("用來描述一個N位非負整數，其各位數字的N次方和等於該數本身。")
print("")
index_num = input("查詢單一數字數否為阿姆斯壯數，請按1\n查詢n位數以下所有的阿姆斯壯數，請按2\n請依照條件輸入 1 或 2 : ")

if index_num == "1":
    check_num = int(input("請輸入欲查詢非負整數： "))
    if check_number(check_num):
        print("您輸入的數字 {} 是阿姆斯壯數！".format(check_num))
    else:
        print("您輸入的數字 {} 不是阿姆斯壯數！".format(check_num))
elif index_num == "2":
    digit_number = int(input("請輸入欲查詢幾位數以下之所有阿姆斯壯數： "))
    print(show_Armstrong(digit_number))
else:
    print("請輸入正確編號")
