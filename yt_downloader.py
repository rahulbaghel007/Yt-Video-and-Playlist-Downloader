from pytube import YouTube

link = "https://www.youtube.com/watch?v=rUWxSEwctFU"
youtube_1 = YouTube(link) #variable

#print(youtube_1.title) #print title of video
video_stream = youtube_1.streams.all()#all formate
audio_stream = youtube_1.streams.filter(only_audio = True)#all formate
stream_list = list(enumerate(audio_stream))#give index no.
for i in stream_list:
    print(i)
print()
strm_index = int(input("enter: "))

audio_stream[strm_index].download()
print("Successfully")