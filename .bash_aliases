alias radio_check="echo $(pgrep -f 'sudo python3 pi-radio/play_radio.py')"
alias radio_off="sudo kill $(pgrep -f 'sudo python3 pi-radio/play_radio.py')"
alias radio_on="nohup sudo python3 pi-radio/play_radio.py > radio.log &"
alias ra="vim pi-radio/play_radio.py"
alias re="radio_off && radio_on"
alias mix="alsamixer"
