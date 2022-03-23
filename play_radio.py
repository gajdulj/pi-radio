#!/usr/bin/env python3

import schedule
import subprocess
import time

### Setup daily alarm ###
SCHEDULE_TIME = '08:30'
STATION_NAME = 'BBC_ONE'
TIMEOUT_SECONDS = 360
TEST_RUN =  False
#########################


def play_radio(station_name=STATION_NAME, timeout_seconds=TIMEOUT_SECONDS):
    stations = {
            'BBC_ONE':'http://stream.live.vc.bbcmedia.co.uk/bbc_radio_one',
            'BBC_FOUR':'http://stream.live.vc.bbcmedia.co.uk/bbc_radio_fourfm',
            }
    station_url = stations[station_name]

    play_command = f"sudo timeout {timeout_seconds}s mplayer {station_url} -noconsolecontrols -really-quiet"
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
        # print(time.asctime( time.localtime(time.time()) ))
        schedule.run_pending()
        time.sleep(1)

if TEST_RUN:
    job()
else:
    run_schedule()
