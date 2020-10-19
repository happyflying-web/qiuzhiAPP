# -*-coding:utf-8-*-
import jieba.analyse

class Extract():
    def __init__(self,filename,result_file_name):
        self.read_file(filename)
        self.jieba_keywords()
        self.temp=''
        fw=open(result_file_name,'w',encoding='utf-8')
        for item in self.keywords:
            self.temp=self.temp+str(item)+'\n'
        fw.write(self.temp)
        fw.close()
    # 读取文件

    def read_file(self,filename):
        self.file = open(filename, 'r', encoding='utf-8').read()
        # return file

    # jieba分词器通过词频获取关键词

    # 基于TF-IDF算法的关键词抽取： import jieba.analyse

    def jieba_keywords(self):
        self.keywords = jieba.analyse.extract_tags(self.file, topK=50)
        print(self.keywords)


if __name__ == '__main__':

    # ex1=Extract('数据挖掘职位要求_result.txt','数据挖掘TOP.txt')
    # ex2=Extract('互联网产品经理职位需求_result.txt','互联网产品经理TOP.txt')
    # ex3=Extract('图像算法工程师职位需求_result.txt','图像算法工程师TOP.txt')
    ex4=Extract('java后端职位要求_result.txt','java后端TOP.txt')
