import requests
from lxml import etree

# 请求头，添加你的浏览器信息后才可以正常运行
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

# 小说主页
main_url = "https://www.xpaozww.com/indexl/500258/1.html"

# 使用get方法获取主页内容
main_resp = requests.get(main_url, headers=headers)
# 将响应数据解码为文本形式,可以看下网页实际的格式
main_text = main_resp.content.decode('utf-8')
# 将文本内容创建为可解析元素
main_html = etree.HTML(main_text)

print(main_text)

# print(main_text)

# 获取章节列表的URL
chapter_list = main_html.xpath('//*[@id="list"]/dl/dd/a/@href')

print(chapter_list)

# 依次获取书籍的标题、作者、最近更新时间和简介
# main_html.xpath返回的是列表，因此需要加一个[0]来表示列表中的首个元素
# bookTitle = main_html.xpath('//*[@id="info"]/h1/text()')[0]  # 书籍标题
# author = main_html.xpath('//*[@id="info"]/p[1]/a/text()')[0]  # 作者
# update = main_html.xpath('//*[@id="info"]/p[3]/text()')[0]  # 最近更新时间
# introduction = main_html.xpath('//*[@id="intro"]/text()')[0]  # 简介

# 遍历所有章节
# 循环用于遍历chapter_list中的每个元素，索引值（index）记录完成的章节数
for index, chapter_url in enumerate(chapter_list):
    # 拼接完整的章节URL，章节URL与一个主页URL拼接起来
    full_chapter_url = main_url + chapter_url
    # 使用requests库发送GET请求获取该URL对应的网页内容
    chapter_resp = requests.get(full_chapter_url, headers=headers)
    chapter_resp.encoding = 'utf-8'  # 设置响应的编码格式为'gbk'
    chapter_text = chapter_resp.text  # 将网页内容解码为文本形式
    chapter_html = etree.HTML(chapter_text)  # 将可解析元素赋值给变量chapter_html

    # 获取章节标题和内容
    title = chapter_html.xpath('//*[@id="chaptertitle"]/text()')[0]
    contents = chapter_html.xpath('//*[@id="novelcontent"]/text()')
    print(title)
    print(contents)
    continue

    # 写入文件
    with open("前妻青梅她们" + '.txt', 'a', encoding='utf-8') as f:
        # 写入文件， 'w'会把文件中内容清空，'a'追加内容，不会覆盖前面的内容
        f.write(title + '\n\n')  # 写入标题
        for content in contents:  # 写入内容
            f.write(content)
            f.write('\n\n')  # 换行

    # 打印进度信息
    print(f'已下载章节: {title}')

print("下载完成！")
