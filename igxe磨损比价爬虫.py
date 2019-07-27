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
            listItem.append(re.findall("/product/\d{3}/\d+", str(link.parent)))
            count += 1
            #print(link.parent)
        print("一共找到了" + str(count) + "个结果")#第二个一般为stattrack
        return count
    except:
        return "fail"


def newLink(url, num, id):
    try:
        r = requests.get(url, params=mykv, timeout=10, headers=kv)
        r.raise_for_status()
        r.encoding = 'utf-8'
        data = json.loads(r.text)
        page_count = jsonpath.jsonpath(data,'$.page.page_count')[0]
        infile = open('data.text', 'w')
        for count in range(page_count):
            itemUrl = "https://www.igxe.cn/product/trade" + num + "?sort_rule=0&buy_method=0&status_locked=0&is_sticker=0&" \
                      "gem_attribute_id=&gem_id=&paint_seed_type=0&paint_seed_id=0&page_no=" + str(count) + '&cur_page=1&product_id='+ id
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
    if float(high) < float(price_list[0]):
        print('算了吧，你这预算，毛都买不到(￣_￣|||)')
        return
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


def main():
    keyword = input("请输入关键字")
    myurl = url + keyword
    count = getLink(myurl)
    if count <= 0:
        print('输入关键词有误，未查到商品，请输入商品完整名称')
        return
    newurl = mainurl + "".join(listItem[choice])
    print('默认为你选择不带StatTrak的商品')
    print('以下为商品链接，也可以自己手动查看')
    print(newurl)
    product_num = "".join(listItem[choice]).split('/product')[1]
    product_id = product_num.split('/')[2]
    dataLink = "https://www.igxe.cn/product/trade" + product_num + "?sort_rule=0&buy_method=0&status_locked=0&is_sticker=0&" \
                                                                   "gem_attribute_id=&gem_id=&paint_seed_type=0&paint_seed_id=" \
                                                                   "0&page_no=2&cur_page=1&product_id=" + product_id
    newLink(dataLink, product_num, product_id)
    compare()


compare_list = []
price_list = []
wear_list = []
dict = {}
page_count = 0
list = []
listItem = []
mainurl ="https://www.igxe.cn"
url = "https://www.igxe.cn/csgo/730?keyword="
kv = {'user-agent':'Chrome/10'}
mykv = {'wd':'Pypy'}
choice = 0
main()

