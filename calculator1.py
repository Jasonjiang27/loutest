#!/usr/bin/env python3 
import sys
for arg in sys.argv[1:]:
    arg = arg.split(':')
    m = int(arg[1])
    if m <=3500:  #工资不高于起征点
        re = 0  #应交税额
        
    elif 3500 < m <=5000:
        re = (m - m*0.165-3500) * 0.03-0
    elif 5000< m <= 8000:
        re = (m-m*0.165-3500) * 0.1 - 105
    elif 8000 < m <= 12500:
        re = (m - m*0.165-3500) * 0.2 - 555
    elif 12500 < m <=38500:
        re = (m-m*0.165-3500) * 0.25 -1005
    elif 38500 < m <=58500:
        re = (m-m*0.165-3500)*0.30- 2755
    elif 58500 < m <= 83500:
        re = (m - m*0.165-3500)*0.35 - 5505
    elif 83500 < m:
        re = (m-m*0.165-3500)*0.45 - 13505
    else:
        print("Parameter Error")
    m_m = m - m*0.165 - re
    print(arg[0]+':'+format(re,".2f"))

