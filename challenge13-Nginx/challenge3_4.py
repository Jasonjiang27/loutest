# -*- coding:utf-8 -*-

import re
from datetime import datetime
from collections import Counter

#使用正则表达式解析日志文件，返回数据列表
def open_parser(filename):
    with open(filename) as logfile:
        #使用正则解析日志
        pattern = (r''
                   r'(\d+.\d+.\d+.\d+)\s-\s-\s'   #IP地址
                   r'\[(.+)\]\s'   #时间
                   r'"GET\s(.+)\s\w+/.+"\s'  #请求路径
                   r'(\d+)\s'   #状态码
                   r'(\d+)\s'   #数据大小
                   r'"(.+)"\s'   #请求头
                   r'"(.+)"'   #客户端信息
                   )
        parsers = re.findall(pattern,logfile.read())
    return parsers

def logs_count():

    #使用正则表达式解析日志文件
    logs = open_parser('/home/shiyanlou/Code/nginx.log')
    """
    1.解析文件就是分离不同类型数据(IP，时间，状态码等)
    2.从解析后的文件中统计挑战需要的需要的信息
    """
    ip_list = []
    url404_list = []

    for log in logs:
        dt = datetime.strptime(log[1][:-6],"%d/%b/%Y:%H:%M:%S")
        if int(dt.strftime("%d")) == 11:
            ip_list.append(log[0])
        if log[3] == "404":
            url404_list.append(log[2])
    return ip_list,url404_list

def main():
    ip_counts = Counter(logs_count()[0])
    url404_counts = Counter(logs_count()[1])
    
    sorted_ip = sorted(ip_counts.items(),reverse = True, key=lambda x: x[1])
    sorted_url404 = sorted(url404_counts.items(),reverse = True, key=lambda x: x[1])
    ip_dict = dict([sorted_ip[0]])
    url_dict = dict([sorted_url404[0]])
    return ip_dict,url_dict

if __name__ == '__main__':
    main()
    print(main())
