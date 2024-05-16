#!/usr/bin/env python3

import schedule
import subprocess
import time

### Setup daily alarm ###
SCHEDULE_TIME = '08:00'
STATION_NAME = 'LOCA_TECH'
TIMEOUT_SECONDS = 360
TEST_RUN =  True
AUDIO_DEVICE = "0.0"
#########################


def play_radio(station_name=STATION_NAME, timeout_seconds=TIMEOUT_SECONDS):
    stations = {
            'BBC_ONE':'http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_one/bbc_radio_one.isml/bbc_radio_one-audio%3d96000.norewind.m3u8',
            'BBC_FOUR':'http://as-hls-ww-live.akamaized.net/pool_904/live/ww/bbc_radio_fourfm/bbc_radio_fourfm.isml/bbc_radio_fourfm-audio%3d96000.norewind.m3u8',
            'LOCA_URBAN':'https://s3.we4stream.com:2020/stream/locaurban',
            'LOCA_TECH': 'https://s3.we4stream.com:2020/stream/locafm'
            }
    station_url = stations[station_name]

    play_command = f"timeout {timeout_seconds}s mpv {station_url} -really-quiet"
    print("Executing following command:", play_command)

    return [play_command]

def job():
    subprocess.run(play_radio(), shell=True)

def schedule_for(time):
    schedule.every().monday.at(time).do(job)
    schedule.every().tuesday.at(time).do(job)
    schedule.every().wednesday.at(time).do(job)
    schedule.every().thursday.at(time).do(job)
    schedule.every().friday.at(time).do(job)

def run_schedule():
    schedule_for(SCHEDULE_TIME)
    while True:
        print(time.asctime( time.localtime(time.time()) ))
        schedule.run_pending()
        time.sleep(1)

if TEST_RUN:
    job()
else:
    run_schedule()
