from bs4 import BeautifulSoup

def extract_text_from_html(html_content):
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取非代码部分的文本内容，并去除行与行之间的空格
    text = '\n'.join(line.strip() for line in soup.get_text(separator='\n').splitlines() if line.strip())

    # 返回提取的文本内容
    return text

# 读取HTML文件
with open('index.html', 'r') as file:
    html_content = file.read()

# 提取文本内容，并去除行与行之间的空格
text_content = extract_text_from_html(html_content)

# 将提取的内容保存到文本文件
with open('output.txt', 'w') as file:
    file.write(text_content)