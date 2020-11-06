# export BERT_BASE_DIR = '绝对路径'
export BERT_BASE_DIR=/home/wujinjie/kesci_question_multilabel_classification/data/emb/chinese_L-12_H-768_A-12
# windows下
# export BERT_BASE_DIR = F:/program/uncased_L-12_H-768_A-12

python3 ./tf2pytorch/convert_checkpoint_to_pytorch.py \
  --tf_checkpoint_path  $BERT_BASE_DIR/bert_model.ckpt   \
  --bert_config_file  $BERT_BASE_DIR/bert_config.json  \
  --pytorch_dump_path  $BERT_BASE_DIR/pytorch_model.bin \