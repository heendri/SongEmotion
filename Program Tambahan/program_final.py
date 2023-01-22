import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

data = pd.read_csv('final_data.csv')
data = data[(data['Artist'].isnull() == False)] #cek artist yg 
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
data['Lirik_bersih'] = data['Lirik'].apply(lambda x: stopword.remove(x))
jml = data['Artist'].unique()
artist_list = data['Artist'].unique()

text_length = [0] * len(artist_list) #array * 10  
my_lyrics = data[data.Artist =='Selvi Kitty'] #cari lyrics yang artist nya ''
text_length[0] = len(my_lyrics)

for i in range(1,len(artist_list)):
    text_length[i] = len(data[data['Artist']==artist_list[i]]['Lirik_bersih'])
    my_lyrics = my_lyrics.append(data[data.Artist == artist_list[i]])
    i+=1
    
warray = [['']] * len(artist_list)
fav_words = [['']] * len(artist_list)
word_cnt = [0] * len(artist_list)

tfidf = TfidfVectorizer(norm='l2', use_idf=True, smooth_idf=True, stop_words='english')
i = 0
kata_sering_muncul = []
for artist, songs in my_lyrics.groupby('Artist'):
    my_texts = data[data['Artist']==artist_list[i]]['Lirik_bersih']
    tfidf.fit_transform(my_texts)
    cnt = np.sum(tfidf.transform(songs['Lirik_bersih']).toarray(), axis=0)
    warray[i] = tfidf.get_feature_names()
    word_cnt[i] = len(warray[i])
    sort_freq = np.argsort(cnt.flatten())[::-1]
    fav_words[i] = [tfidf.get_feature_names()[idx] for idx in sort_freq.tolist()[:50]]
    kata_sering_muncul.append([artist_list[i],fav_words[i]])
    i+=1
kamus_kata = pd.DataFrame(kata_sering_muncul, columns=['Artist','Kata'])
kamus_kata.to_csv('kamus_kata.csv')
comb_texts = ['']*len(artist_list)
comb_length = [0]*len(artist_list)
i=0
j=0
mn=0
while (i!=len(my_lyrics)):
    comb_texts[j] += (my_lyrics.iloc[i]['Lirik'])
    if (i == text_length[j]+ mn ):
        mn+=text_length[j]
        j+=1
    i+=1
for l in range (0,len(artist_list)):
    comb_length[l] = len(comb_texts[l])
artists_stats = pd.DataFrame()
artists_stats['Artist'] = artist_list
artists_stats['Lagu'] = text_length
artists_stats['Kata'] = word_cnt
artists_stats['all_length'] = comb_length
file_emotion = pd.read_csv('kamus_emotion.csv')
topics = file_emotion['Kata'].tolist() #0 - 730: joy , 731 - end: sad
topic_cnt = np.zeros((len(artist_list),len(topics)), int)
i = 0
j = 0
for text in comb_texts:
    for topic in topics:
        topic_cnt[i][j] = text.count(topic)
        j+=1
    j=0
    i+=1
freq_df = pd.DataFrame(topic_cnt)
freq_df.rename(columns=lambda x: topics[int(x)], inplace=True)
col_list_joy = list(freq_df.iloc[:,0:730])
col_list_sad = list(freq_df.iloc[:,731:1657])
freq_df['joy'] = freq_df[col_list_joy].sum(axis=1)
freq_df['sad'] = freq_df[col_list_sad].sum(axis=1)
freq_df['artist'] = artist_list
freq_df['mood'] = np.where((freq_df['joy'] >= freq_df['sad']), "Joy", "Sad")
baru = freq_df.ix[:,'artist':'mood']                   # table of word frequencies by artist
baru.to_csv("hasil.csv")
print(baru)