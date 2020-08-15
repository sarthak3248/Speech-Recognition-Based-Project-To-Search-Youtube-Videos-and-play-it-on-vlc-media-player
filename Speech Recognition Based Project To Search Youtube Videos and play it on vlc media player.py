#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install SpeechRecognition


# In[2]:


import speech_recognition as spr


# In[4]:


import webbrowser as wb


# In[5]:


pip install pafy


# In[8]:


pip install python-vlc


# In[9]:


pip install beautifulsoup4


# In[10]:


import vlc


# In[11]:


import urllib.request


# In[12]:


from bs4 import BeautifulSoup


# In[13]:


import time


# In[ ]:


linklist=[]


# In[18]:


pip install PyAudio


# In[ ]:


mc=spr.Microphone(device_index=0)


# In[30]:


recog1=spr.Recognizer()
recog2=spr.Recognizer()


# In[ ]:


with mc as source:
    print("Search Youtube Video to play")
    print("----------------------------")
    print("You can speak now")
    audio=recog1.listen(source)


# In[ ]:


#Based on speech, open youtube search page in a browser, get the first video link and play it in VLC media player
if 'search' in recog1.recognize_google(audio):
    recog1 = spr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with mc as source:
        print('Searching for the video(s)...')
        audio = recog2.listen(source)
        
        try:
            get_keyword = recog1.recognize_google(audio)
            print(get_keyword)
            wb.get().open_new(url+get_keyword)
            response = urllib.request.urlopen(url+get_keyword)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
                linklist.append('https://www.youtube.com' +vid['href'])
            videolink = pafy.new(linklist[1])
            bestlink = videolink.getbest()
            media = vlc.MediaPlayer(bestlink.url)
            media.play()
#             time.sleep(60)
#             media.stop()
        except spr.UnknownValueError:
            print("Unable to understand the input")
        except spr.RequestError as e:
            print("Unable to provide required output".format(e))


# In[ ]:


media.stop()

