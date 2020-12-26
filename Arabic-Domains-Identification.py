import wordninja
import enchant

import extract_domain_hostname as support

path_file = '/Users/imanory/Desktop/ArabicDomainsIdentification/sample-without-lable.txt'
dictionary = enchant.Dict("en_UK")

with open(path_file) as domains_file :
    for line in domains_file:
        num_english_words = 0
        num_non_english_words = 0
        line = line.strip()
        hostname = support.getHostName(line)
        words = wordninja.split(hostname)
        for word in words:
            check = dictionary.check(word) 
            if (check == True):
                num_english_words+=1
            else:
                num_non_english_words+=1
        if (num_non_english_words > 0):
            print(line + "\t" + "Non-English")
        else:
            print(line + "\t" + "English")
