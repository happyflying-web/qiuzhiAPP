import jieba
import wordcloud
import jieba

class Tool():
    def __init__(self, filename_origin, filename_result):
        # 创建停用词list
        def stopwordslist(filepath):
            stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
            return stopwords

        # 对句子进行分词
        def seg_sentence(sentence):
            sentence_seged = jieba.cut(sentence.strip())
            stopwords = stopwordslist('hit_stopwords.txt')  # 这里加载停用词的路径
            stopwords.extend([str(i) for i in range(0, 10)])
            stopwords.extend(['岗位', '职责', '要求', '根据','岗位职责','以上学历','相关','优先','能力','业务','负责'])
            outstr = ''
            for word in sentence_seged:
                if word not in stopwords:
                    if word != '\t':
                        outstr += word
                        outstr += " "
            return outstr

        inputs = open(filename_origin, 'r', encoding='utf-8')
        outputs = open(filename_result, 'w', encoding='utf-8')
        for line in inputs:
            line_seg = seg_sentence(line)  # 这里的返回值是字符串
            outputs.write(line_seg + '\n')
        outputs.close()
        inputs.close()


if __name__ == '__main__':
    Tool('数据挖掘职位要求.txt','数据挖掘职位要求_result.txt')
    # Tool('java后端职位要求.txt','java后端职位要求_result.txt')
    # Tool('互联网产品经理职位需求.txt','互联网产品经理职位需求_result.txt')
    # Tool('图像算法工程师职位需求.txt', '图像算法工程师职位需求_result.txt')
