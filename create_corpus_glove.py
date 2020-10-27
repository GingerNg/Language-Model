from utils import file_utils
from utils.nlp_utils import segment
import pandas as pd

data_df = pd.read_csv("/home/ginger/Projects/contests/kesci_question_multilabel_classification/data/raw_data/baidu/nlp_db.baidu_text.csv")
datas = []
for line in data_df.values.tolist():
    # print(line)
    words = segment(line[1])
    if len(words) > 1:
        datas.append(words)
name = ['sentence']
data_pd = pd.DataFrame(columns=name, data=datas)

train_path = "./data/corpus_glove.txt"
file_utils.writeData(data_pd["sentence"].to_list(), train_path)