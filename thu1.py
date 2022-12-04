flag = False
while flag == False:
    gbt = int(input('chọn giờ báo thức: '))
    if gbt < 1 or gbt > 24:
        print('giờ không tồn tại, vui lòng nhập lại giờ báo thức: ')
    else:
        flag = True
flag = False
while flag == False:
    pbt = int(input('chọn phút báo thức: '))
    if pbt < 0 or pbt > 59:
        print('phút không tồn tại, vui lòng nhập lại phút báo thức: ')
    else:
        flag = True

from datetime import datetime

now = datetime.now()

current_hour = now.strftime("%H")
current_minute = now.strftime("%M")
print('giờ hiện tại: ',current_hour)
print('phút hiện tại: ',current_minute)
