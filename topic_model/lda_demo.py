import jieba
import os
import re
from gensim import corpora, models, similarities
import pandas as pd
import pickle

Industries = ['互联网',
              '交通运输',
              '体育竞技',
              '党政机关',
              '医疗保健',
              '婚礼婚庆',
              '宠物行业',
              '房产建筑',
              '教育行业',
              '旅游行业',
              '美容保养',
              '节日庆典',
              '运动健身',
              '金融投资',
              '餐饮行业']

# data_df = pd.read_csv("/home/wujinjie/kesci_question_multilabel_classification/data/raw_data/baidu/nlp_db.baidu_text.csv")
# data_df = data_df[data_df.keyword=="金融投资"]
for label in Industries:
    """准备好训练语料，整理成gensim需要的输入格式"""
    fr = open('/home/wujinjie/Language-Model/data/corpus_jieba_%s.txt' % label, 'r', encoding='utf-8')
    train = []
    for line in fr.readlines():
        line = [word.strip() for word in line.split(' ')]
        train.append(line)
        # train: [['黄蜂', '湖人', '首发', '科比', '带伤', '战',...],[...],...]

    """构建词频矩阵，训练LDA模型"""
    dictionary = corpora.Dictionary(train)
    # corpus[0]: [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1),...]
    # corpus是把每条新闻ID化后的结果，每个元素是新闻中的每个词语，在字典中的ID和频率
    corpus = [dictionary.doc2bow(text) for text in train]

    lda = models.LdaModel(corpus=corpus, id2word=dictionary,)
    topic_list = lda.print_topics(100)
    # print("10个主题的单词分布为：\n")
    topic_words = {}
    for topic in topic_list:
        line = topic[1].replace(" ", "")
        word_items = line.split("+")
        for item in word_items:
            weight, word = item.strip().split("*")
            # print(weight, eval(word))
            word = eval(word)
            weight = eval(weight)
            if word in topic_words:
                topic_words[word] += weight
                topic_words[word] /= 2
            else:
                topic_words[word] = weight

    with open("/home/wujinjie/Language-Model/data/topic_model/lda_%s.pkl" % label, 'wb') as file:
        pickle.dump(topic_words, file)
