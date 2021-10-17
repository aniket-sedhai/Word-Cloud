#Author Aniket Sedhai (From Coursera IT Automation with Python Course)
#Date 10/17/2021

# Here are all the installs and imports you will need for your word cloud script and uploader widget

!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    words = file_contents.split()
    words_nopunc = []
    char_scanner = 0
    for word in words:
        if(word.isalpha()):
            words_nopunc.append(word)
        else:
            noPuncWord = ""
            loopBreaker = False
            for letter in word:
                if letter.isalpha() != True:
                    loopBreaker = True
                if(loopBreaker == False):
                    noPuncWord += letter
            words_nopunc.append(noPuncWord)
    
    #punctuations cleared
    processed_words = []
    for word in words_nopunc:
        if word not in uninteresting_words:
            processed_words.append(word.lower())
    
    frequency_dictionary = {}
    for word in processed_words:
        if(word not in frequency_dictionary.keys()):
            freq = processed_words.count(word)
            frequency_dictionary[word] = freq
        
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequency_dictionary)
    return cloud.to_array()

  
  # Display your wordcloud image
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
