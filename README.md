# igxe-csgo饰品磨损比价爬虫



## 自学web以及python爬虫的第一个练手项目

> 难度：简单

> 应用技术：request库 re库 jsonpath库 BeautifulSoup库

> 主要收获：
>
> + 利用浏览器开发者工具中的Network 的XHR来或许网页异步发送的请求（比如翻页之后的信息）
> + 通过jsonpath库 来抓取json格式的数据文件
> + 简单的使用re库获取信息

> 不足：igxe网站反爬虫难度不大，未设有登录验证以及滑块验证码等复杂操作，因此难度过于简单

## 使用方法

>环境要求：request库 BeautifulSoup库 jsonpath库（使用pip install 指令安装）
>
>具体用法：
>
>+ 输入关键字（建议输入完整的商品名称 e.g. **AWP | 二西莫夫 (久经沙场)** )
>+ 输入期待的最高价格，程序会给出改价格内能买到的最低的磨损
>+ 程序会在根目录生成 **data.text** 文件，里面包含了该商品的所有磨损及对应价格
>+ 源码中的 **choice** 变量默认为0，但若搜索的饰品包含了StatTrack则将 **choice** 改成1可显示带计数器的皮肤

## 后记

> 该项目只是第一个练手，我根据情况说不定会更新其他饰品网站的比价程序（呼声较高的是网易BUFF），但是其他网站说不定会更难爬取一些，一切看我情况再说啦(。・∀・)ノ

