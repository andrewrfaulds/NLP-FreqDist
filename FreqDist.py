import string
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from  matplotlib import pyplot as plt




def tokenize_text():
    '''generate tokenised file w/o stopwords or uppercase'''
    stopword = set(stopwords.words('english'))
    with open('input.txt', 'r+') as file_in, open('tokens.txt', 'w+') as file_out:
        data_stream1 = file_in.read()
        data_trns = data_stream1.translate(str.maketrans('', '', string.punctuation))
        data_lower = data_trns.lower()
        tokens = word_tokenize(data_lower)
        no_stopwords = [word for word in tokens if word not in stopword]
        print((no_stopwords), file=file_out)



def freq_dist():
    '''calculate and plot frequency distribution of each word'''
    plt.title('Words by Freq Count.', size=25)
    plt.xlabel('word')
    plt.ylabel('counts')
    plt.tight_layout()
    #plt.xticks(size=20)
    #plt.yticks(size=20)
    filename = "tokens.txt"
    tokenizer = RegexpTokenizer(r'\w+')
    with open(filename, 'r+') as tokened_file:
        data_stream2 = tokened_file.read()
	#must re-tokenizse for freqdist
        re_tokenized = tokenizer.tokenize(data_stream2)
        fdist = FreqDist(re_tokenized)
        fdist.plot(20, cumulative=False)





def _main_():
    '''initiates program'''
    try:
        #clean()
        tokenize_text()
        freq_dist()
        print("success")
    except:
        print("failed")

# calls main to initiate program
_main_()