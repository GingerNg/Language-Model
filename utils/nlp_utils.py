from utils.file_utils import readFile
import jieba
import re
import pickle


def remain(string):
    # string = "123我123456abcdefgABCVDFF？/ ，。,.:;:''';'''[]{}()（）《》"
    # print(string)
    # sub_str = re.sub(
    #     u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", string)
    sub_str = re.sub(
        u"([^\u4e00-\u9fa5\u0041-\u005a\u0061-\u007a])", "", string)
    # print(sub_str)
    return sub_str


def remove_stopword(word):
    word = remain(word)
    if len(word) == 1:
        return False
    if word in stopWordList:
        return False
    else:
        return True


def segment(mytext):
    """中文分词"""
    if isinstance(mytext, str) and len(mytext) > 0:
        return " ".join(filter(remove_stopword, jieba.cut(mytext)))
    else:
        return ""


def get_stop_word(inputFile):
    stopWordList = readFile(inputFile, encoding="utf-8").splitlines()
    return stopWordList


try:
    stopWordList = get_stop_word(
        "/home/wujinjie/kesci_question_multilabel_classification/data/stopwords.txt")  # 获取停用词
    stopWordList.append("无外乎")
except Exception:
    stopWordList = []


