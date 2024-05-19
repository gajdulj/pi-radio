from flask import Flask, render_template, request, session
import vlc

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Define the radio stations
stations = {
    "BBC_ONE": "http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_one/bbc_radio_one.isml/bbc_radio_one-audio%3d96000.norewind.m3u8",
    "BBC_FOUR": "http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_fourfm/bbc_radio_fourfm.isml/bbc_radio_fourfm-audio%3d96000.norewind.m3u8",
    "LOCA_URBAN": "https://s3.we4stream.com:2020/stream/locaurban",
    "LOCA_TECH": "https://s3.we4stream.com:2020/stream/locafm",
}

# Initialize VLC player instance
player = vlc.MediaPlayer()


@app.route("/", methods=["GET", "POST"])
def index():
    if "volume" not in session:
        session["volume"] = 50
    if request.method == "POST":
        if "play" in request.form:
            station_name = request.form["station"]
            session["station_name"] = station_name
            play_station(stations[station_name])
        elif "stop" in request.form:
            player.stop()
        elif "volume" in request.form:
            volume = int(request.form["volume"])
            session["volume"] = volume
            player.audio_set_volume(volume)

    return render_template(
        "index.html",
        stations=stations,
        current_station=session.get("station_name", ""),
        volume=session["volume"],
    )


def play_station(station_url):
    player.stop()
    player.set_mrl(station_url)
    player.play()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
