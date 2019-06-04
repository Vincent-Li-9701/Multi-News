python preprocess.py -train_src /home/lily/af726/spring-2019/summarization_general/data-final/data-truncated-opennmt/train.txt.src.tokenizd.fixed.cleaned.truncated \
                     -train_tgt /home/lily/af726/spring-2019/summarization_general/data-final/data-truncated-opennmt/train.txt.tgt.tokenizd.fixed.cleaned.truncated \
                     -valid_src /home/lily/af726/spring-2019/summarization_general/data-final/data-truncated-opennmt/val.txt.src.tokenizd.fixed.cleaned.truncated \
                     -valid_tgt /home/lily/af726/spring-2019/summarization_general/data-final/data-truncated-opennmt/val.txt.tgt.tokenizd.fixed.cleaned.truncated \
                     -save_data newser_sent_500/newser_sents \
                     -src_seq_length 10000 \
                     -tgt_seq_length 10000 \
                     -src_seq_length_trunc 500 \
                     -tgt_seq_length_trunc 300 \
                     -dynamic_dict \
                     -share_vocab \
                     -max_shard_size 10000000
