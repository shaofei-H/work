import requests
import csv
from bs4 import BeautifulSoup

# 获取
url = 'https://www.chinabond.com.cn/cb/cn/xxpl/ywgg/tgywgg/20230129/161991420.shtml'
response = requests.get(url)

# 解析表格内数据信息，只保留包含数字序号的行数据
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', attrs={'class': 't1'})
rows = table.find_all('tr')

data = []
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 0 and cells[0].text.isdigit():
        row_data = [cell.text.strip() for cell in cells]
        data.append(row_data)

# 保存成有效csv文件
with open('D:/chinabond_data.csv', mode='w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['序号', '债券代码', '债券名称', '计息方式', '债券面额（万元）', '年利率(%)'])
    writer.writerows(data)