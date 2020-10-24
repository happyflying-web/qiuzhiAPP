from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator


class FormWordCloud:
    def __init__(self, text_path, wordCloud_name):
        # text_path = 'java后端TOP.txt'  # 设置要分析的文本路径
        font_path = r'C:\Windows\Fonts\simfang.ttf'
        # 设置词云属性
        wc = WordCloud(
            font_path=font_path,  # 设置字体
            background_color="white",  # 背景颜色
            max_words=2000,  # 词云显示的最大词数
            # mask=back_coloring,  # 设置背景图片
            max_font_size=100,  # 字体最大值
            random_state=42,
            width=1000, height=860, margin=2,  # 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
        )
        #
        text = open(text_path, 'r', encoding='utf-8').read()
        print(text)
        wc.generate(text)
        plt.figure()
        # 以下代码显示图片
        plt.imshow(wc)
        plt.axis("off")
        plt.show()
        # 绘制词云
        # 保存图片
        wc.to_file(wordCloud_name)


if __name__ == '__main__':
    # FormWordCloud('互联网产品经理TOP.txt', '互联网产品经理-词云图.jpg')
    # FormWordCloud('数据挖掘TOP.txt', '数据挖掘-词云图.jpg')
    FormWordCloud('java后端TOP_test_10_21.txt', 'java后端-词云图_test_10_21.jpg')
    # FormWordCloud('图像算法工程师TOP.txt', '图像算法工程师-词云图.jpg')
