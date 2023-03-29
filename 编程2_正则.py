long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

# 按行分割文本
lines = long_text.strip().split('\n')

# 初始化结果字典
result = {
    'name': '',
    'lei': '',
    'sub_fund': []
}

# 解析结果字典中的name和lei字段
result['name'] = lines[0]
result['lei'] = lines[1]

# 解析结果字典中的sub_fund字段
sub_fund = []
for i in range(2, len(lines)):
    line = lines[i]
    # 如果是数字开头，则表示一个新的sub_fund
    if line[0].isdigit():
        sub_fund_title = line.split('. ')[1]
        sub_fund_isin = []
    # 如果是字母开头，则表示一个isin
    else:
        sub_fund_isin.append(line)
    # 如果下一行是数字开头或者已经到达文本末尾，则表示sub_fund的结束
    if i == len(lines)-1 or lines[i+1][0].isdigit():
        sub_fund.append({
            'title': sub_fund_title,
            'isin': sub_fund_isin
        })

# 将解析后的sub_fund字段添加到结果字典中
result['sub_fund'] = sub_fund

# 打印结果字典
print(result)