from nltk.util import ngrams
import numpy as np
import argparse

def compare(ngrams1, ngrams2):
    ngrams1 = list(ngrams1)
    ngrams2 = list(ngrams2)
    common=[]
    for gram in ngrams1:
        if gram in ngrams2:
            common.append(gram)
    return len(common)

def select_target(ngram, input_data, output_src, output_tgt):
    
    lines = input_data.readlines()

    target_length=300
    for index in range(len(lines)):
        line = lines[index].strip()
        splited = line.split('story_separator_special_tag')
        overlap_list=[]
        if len(splited) == 1:
            target = splited[0]
        else:
            if len(splited) == 2:
                first_split = splited[0].lower().split()
                second_split = splited[1].lower().split()
                if len(first_split) > len(second_split):
                    target = splited.pop(0)
                else:
                    target = splited.pop(1)
            else: 
                for i in range(len(splited)):
                    target_split = splited[i].lower().split()
                    if len(target_split) > target_length:
                        target_split = target_split[:target_length]
                    overlap=[]
                    for j in range(len(splited)):
                        if i != j:
                            ngrams1 = ngrams(target_split, ngram) 
                            ngrams2 = ngrams(splited[j].lower().split(), ngram)
                            overlap.append(compare(ngrams1,ngrams2))

                    overlap_list.append(sum(overlap) // len(overlap))
                index = overlap_list.index(max(overlap_list))
                target = splited.pop(index)
        
        if (len(target.split()) > target_length):
            target_split = target.split()
            target_split = target_split[:target_length]
            target = " ".join(target_split)
        
        output_src.write('story_separator_special_tag'.join(splited)+'\n')
        output_tgt.write('- ' + target.strip() +'\n')

    output_src.close()
    output_tgt.close()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Output the best target based on n-gram overlap')
    parser.add_argument('--ngram', type=int, required=True, help='What N-Grams Overlap are you trying to calculate')
    parser.add_argument('--input_data', type=str, required=True, help='Input data path')
    parser.add_argument('--output_src', type=str, required=True, help='Output training data path')
    parser.add_argument('--output_tgt', type=str, required=True, help='Output target data path')
    
    args = parser.parse_args()
    input_data = open(args.input_data, 'r')
    output_train = open(args.output_src, 'w')
    output_target = open(args.output_tgt, 'w')
    
    select_target(args.ngram, input_data, output_src, output_tgt)
