import textdistance
from pypinyin import lazy_pinyin

class Similarity(object):

    def __init__(self):
        pass

    def comput_char_jaccard(self,s1,s2):
        return textdistance.jaccard.normalized_similarity(s1,s2)

    def comput_pinyin_jaccard(self,s1,s2):
        s1_pinyin = lazy_pinyin(s1)
        s2_pinyin = lazy_pinyin(s2)
        return textdistance.jaccard.normalized_similarity(s1_pinyin,s2_pinyin)

    def comput_char_editdistance(self,s1,s2):
        return textdistance.levenshtein.normalized_similarity(s1,s2)

    def match_sentence(self,s1,s2):
        jaccard_pinyin = self.comput_pinyin_jaccard(s1,s2)
        jaccard_char = self.comput_char_jaccard(s1,s2)
        edit_char = self.comput_char_editdistance(s1,s2)

        sim_val = (jaccard_pinyin+jaccard_char+edit_char) / 3
        return sim_val