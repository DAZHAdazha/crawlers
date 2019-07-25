import requests
from bs4 import BeautifulSoup
import re
import json
import jsonpath


def getLink(url):
    try:
        r = requests.get(url, params=mykv, timeout=10, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        soup = BeautifulSoup(demo, "html.parser")
        #print(soup.div.string)
        count = 0
        for link in soup.find_all('div',"name"):
            listItem.append(re.findall("/product/\d{3}/\d{4}", str(link.parent)))
            count += 1
            #print(link.parent)
        print("一共找到了" + str(count) + "个结果")#第二个一般为stattrack
    except:
        return "fail"


def newLink(url):
    try:
        r = requests.get(url, params=mykv, timeout=10, headers=kv)
        r.raise_for_status()
        r.encoding = 'utf-8'
        data = json.loads(r.text)
        page_count = jsonpath.jsonpath(data,'$.page.page_count')[0]
        infile = open('data.text', 'w')
        for count in range(page_count):
            itemUrl = "https://www.igxe.cn/product/trade" + product_num + "?sort_rule=0&buy_method=0&status_locked=0&is_sticker=0&" \
                      "gem_attribute_id=&gem_id=&paint_seed_type=0&paint_seed_id=0&page_no=" + str(count) + '&cur_page=1&product_id='+ product_id
            re = requests.get(itemUrl, params=mykv, timeout=10, headers=kv)
            re.encoding = 'utf-8'
            newData = json.loads(re.text)
            for i in range(10):
                mywear = '$.d_list[' + str(i) + '].exterior_wear'
                myprice = '$.d_list[' + str(i) + '].unit_price'
                data = ''.join(jsonpath.jsonpath(newData, mywear)) + ' ' + ''.join(jsonpath.jsonpath(newData, myprice)) + '\n'
                infile.write(data)

    except:
        return "失败"


def compare():
    outfile = open('data.text', 'r')
    for line in outfile.readlines():
        wear_list.append(line.split()[0])
        price_list.append(line.split()[1])
        dict[line.split()[1]] = line.split()[0]
    wear_list.sort()
    price_list.sort()
    high = input("输入期待的最高价格")
    for price in price_list:
        if float(price) > float(high):
            break
        else:
            compare_list.append(dict[price])
    compare_list.sort()
    for key in dict:
        if dict[key] == compare_list[0]:
            print('这个价位最好磨损：' + key + '\n' + compare_list[0])
    print(dict)


compare_list = []
price_list = []
wear_list = []
dict = {}
keyword = input("请输入关键字")
page_count = 0
list = []
listItem = []
mainurl ="https://www.igxe.cn"
url = "https://www.igxe.cn/csgo/730?keyword="
myurl = url + keyword
kv = {'user-agent':'Chrome/10'}
mykv = {'wd':'Pypy'}
getLink(myurl)
choice = 0
newurl = mainurl +  "".join(listItem[choice])
print(newurl)
product_num = "".join(listItem[choice]).split('/product')[1]
product_id = product_num.split('/')[2]
dataLink ="https://www.igxe.cn/product/trade" + product_num +"?sort_rule=0&buy_method=0&status_locked=0&is_sticker=0&" \
                                                             "gem_attribute_id=&gem_id=&paint_seed_type=0&paint_seed_id=" \
                                                             "0&page_no=2&cur_page=1&product_id=" + product_id
newLink(dataLink)
compare()
