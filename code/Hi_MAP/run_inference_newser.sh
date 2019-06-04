CUDA_VISIBLE_DEVICES=0,1 python translate.py -gpu 0 \
                    -batch_size 8 \
                    -beam_size 4 \
                    -model model_newser_atten/Feb17__step_15000.pt \
                    -src Newser_data_test_src/test.txt.src.tokenized.fixed.cleaned.final.cleaned.final \
                    -output output_newser/Feb17__step_15000_full.output\
                    -min_length 200 \
                    -max_length 300 \
                    -verbose \
                    -stepwise_penalty \
                    -coverage_penalty summary \
                    -beta 5 \
                    -length_penalty wu \
                    -alpha 0.9 \
                    -verbose \
                    -block_ngram_repeat 3 \
                    -ignore_when_blocking "story_separator_special_tag"