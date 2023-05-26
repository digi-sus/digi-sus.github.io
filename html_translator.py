from bs4 import BeautifulSoup
import openai
def translate_text(text, target_language):
    # 设置OpenAI API凭证
    openai.api_key = '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'

    # 调用GPT进行翻译
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text},
            {"role": "assistant", "content": "Translate the text to " + target_language + "."}
        ]
    )

    # 提取翻译结果
    translation = response['choices'][0]['message']['content']
    return translation

# 读取原始HTML文件
with open('index.html', 'r') as file:
    html_content = file.read()

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 找到需要翻译的文本并进行翻译
tags_to_translate = soup.find_all(text=True)

for tag in tags_to_translate:
    if tag.strip() != '':
        # 调用翻译函数进行翻译
        translated_text = translate_text(tag.strip(), 'de')
        # 替换文本内容
        tag.string.replace_with(translated_text)

# 将修改后的HTML保存到文件
with open('de_test.html', 'w') as file:
    file.write(str(soup))