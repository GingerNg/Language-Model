import os
from enum import Enum


proj_path = os.path.dirname(__file__)

raw_data_path = "/home/wujinjie/kesci_question_multilabel_classification/data/raw_data/"
baidu_raw_data_path = os.path.join(raw_data_path, "baidu/nlp_db.baidu_text.csv")

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