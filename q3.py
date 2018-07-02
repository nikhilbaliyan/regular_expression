import re
sentence = "A, very   very; irregular_sentence"
l=(" ".join(re.split('[;,\s_]+', sentence)))
print(l)