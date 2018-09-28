# 朴素贝叶斯算法, 代码参考了《机器学习》郑捷
import numpy as np


class NBayes(object):
    def __init__(self):
        self.vocabulary = []
        self.idf = 0
        self.tf = 0
        self.tdm = 0  # p(x/y)  贝叶斯公式的分子
        self.Pcates = {}  # p(yi)
        self.labels = []
        self.doclength = 0
        self.vocablen = 0
        self.testset = 0

    def train_set(self, trainset, classvec):
        """
        导入数据集
        :param trainset:
        :param classvec:
        :return:
        """

    def cate_prob(self, classvec):
        """
        计算数据集中的分类概率p(yi)
        :param classvec:
        :return:
        """
        self.labels = classvec
        labeltemps = set(self.labels)
        for labeltemp in labeltemps:   # 遍历所有Label
            self.Pcates[labeltemp] = float(self.labels.count(labeltemp)) / float(len(self.labels))

    def calc_wordfreq(self, trainset):
        """
        生成普通词频向量
        :param trainset:
        :return:
        """
        self.idf = np.zeros([1, self.vocablen])    # 逆向文件频率（在几个文件出现过）
        self.tf = np.zeros([self.doclength, self.vocablen])  # 词语频率
        for indx in range(self.doclength):
            # 找到一个词就把词频统计
            for word in trainset:   # 句子中的每个词
                self.tf[indx, self.vocabulary.index(word)] += 1  # 统计词语频率
            for signleword in set(trainset[indx]):    # 第indx文件出现的所有词语集合中遍历每个词语
                self.idf[0, self.vocabulary.index(signleword)] += 1

    def build_tdm(self):
        """
        计算每个维度p(x/yi)
        :return:
        """
        self.tdm = np.zeros([len(self.Pcates), self.vocablen])   # y的类别x词典长，每个元素是p(xj/yi)
        sumtdm = np.zeros([len(self.Pcates), 1])
        for indx in range(self.doclength):
            self.tdm[self.labels[indx]] += self.tf[indx, :]      # tf就代表了p(xj/yi)
            sumtdm[self.labels[indx]] = np.sum(self.tdm[self.labels[indx]])
        self.tdm = self.tdm/sumtdm


