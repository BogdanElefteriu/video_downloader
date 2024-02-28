import streamlit as st
import os
from pytube import YouTube
import youtube_dl


def download_yt(link):
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

def download_fb(link):
    with youtube_dl.YoutubeDL({"format": "best"}) as ydl:
        ydl.download([link])


def download_video():
    link = st.session_state.user_input
    if link:
        try:
            if 'youtube' in link.lower():
                download_yt(link)
                st.session_state.user_input = ""
            elif 'facebook' in link.lower():
                download_fb(link)
                st.session_state.user_input = ""
        except:
            st.write(":red[A aparut o eroare in procesul de descarcare a acestui video. Te rog sa incerci alt video.]")
                



st.title("Descarca video (Youtube; Facebook)")


link = st.text_input(label="Introdu link-ul video-ului:", key="user_input", on_change=download_video)

for file in os.listdir():
    if '.mp4' in file:
        st.video(os.path.join(os.getcwd(), file))

        if st.download_button(label = "Descarca video-ul",
                                file_name=file,
                                data = open(file, "rb")):
           
            os.remove(os.path.join(os.getcwd(), file))
            st.rerun()

