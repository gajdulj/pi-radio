import streamlit as st
import vlc

# Define the radio stations
stations = {
    "BBC_ONE": "http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_one/bbc_radio_one.isml/bbc_radio_one-audio%3d96000.norewind.m3u8",
    "BBC_FOUR": "http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_fourfm/bbc_radio_fourfm.isml/bbc_radio_fourfm-audio%3d96000.norewind.m3u8",
    "LOCA_URBAN": "https://s3.we4stream.com:2020/stream/locaurban",
    "LOCA_TECH": "https://s3.we4stream.com:2020/stream/locafm",
}

# Create a VLC player instance
if "player" not in st.session_state:
    st.session_state.player = vlc.MediaPlayer()


def play_station(station_url):
    st.session_state.player.stop()
    st.session_state.player.set_mrl(station_url)
    st.session_state.player.play()


# Streamlit interface
st.title("Internet Radio Player")

# Select a radio station
station_name = st.selectbox("Select a station", list(stations.keys()))

if st.button("Play"):
    play_station(stations[station_name])
    st.write(f"Playing {station_name}")

if st.button("Stop"):
    st.session_state.player.stop()
    st.write("Stopped playing")

# Volume control
volume = st.slider("Volume", 0, 100, 50)
st.session_state.player.audio_set_volume(volume)
st.write(f"Current volume: {volume}")
