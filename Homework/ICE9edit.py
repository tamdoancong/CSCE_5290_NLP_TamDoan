from numpy.random import choice
def convert_sentence( sentence):
    return ["<s>"] + ["<s>"] + [w.lower() for w in sentence] + ["</s>"]
def trigram(sentences):
    l_s_trigram = []
    l_s_bigram =[]
    for sentence in sentences:
        sentence = convert_sentence(sentence)
        # get bigram in each sentence
        s_bigram = [tuple(sentence[i:i + 2]) for i in range(len(sentence) - 2)]
        l_s_bigram+=s_bigram
        # get triagram in each sentence
        s_trigram = [tuple(sentence[i:i + 3]) for i in range(len(sentence) - 3)]
        l_s_trigram += s_trigram
    # print(l_s_trigram)
    # count all bigram in data and put them to dict
    bigram_counts={bigram: l_s_bigram.count(bigram) for bigram in set(l_s_bigram)}
    # count all trigram in data and put them into dict
    trigram_counts = {trigram: l_s_trigram.count(trigram) for trigram in set(l_s_trigram)}
    s = ["<s>", "<s>"]
    #while s[-1] != "</s>":
    for i in range(20):
        word1 = s[-2]# this must be inside a loop
        word2 = s[-1]## this must be inside a loop
        cw1w2 = 0
        cw1w2w3 = 0
        for k1,v1 in bigram_counts.items():
            if k1==(word1,word2):
                cw1w2+=v1
        l_word3 = []
        l_pro_word3 = []
        # print(trigram_counts.items())
        for k2,v2 in trigram_counts.items():
            if k2[0]==word1 and k2[1]==word2 :
                cw1w2w3+=v2
                word3=k2[2]
                # print(word3)
                pro_word3=(cw1w2w3/cw1w2)
                l_pro_word3.append(pro_word3)
                l_word3.append(word3)
        # print(l_word3)
        # print(l_pro_word3)
        # id=l_pro_word3.index(max(l_pro_word3))
        high_pro_word3 = choice(l_word3)
        s.append(high_pro_word3)
    generate_s = " ".join(s[2:-1])
    # print(generate_s)
    return generate_s
import nltk
from nltk.corpus import brown
nltk.download('brown')
print(trigram(brown.sents()[:1000]))