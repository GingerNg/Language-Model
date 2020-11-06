from utils import file_utils
from utils.nlp_utils import segment
import pandas as pd
import cfg

labels = cfg.Industries
for label in labels:
    data_df = pd.read_csv(cfg.baidu_raw_data_path)
    data_df = data_df[data_df.keyword==label]
    datas = []
    for line in data_df.values.tolist():
        # print(line)
        words = segment(line[1])
        if len(words) > 1:
            datas.append(words)
    name = ['sentence']
    data_pd = pd.DataFrame(columns=name, data=datas)

    train_path = "./data/corpus_jieba_%s.txt" % label
    file_utils.writeData(data_pd["sentence"].to_list(), train_path)
