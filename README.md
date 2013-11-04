xbmc-client
===========

xbmc-client is a XBMC command line client which control your XBMC instance throught JSON API.


Available options :

```sh
Usage: xbmc-client [options]

Options:
  -h, --help            show this help message and exit
  -c CONFIG, --config=CONFIG
                        Configuration file. Default is located in ~/.config
                        /xbmc-client/config
  --host=HOST           XBMC http host
  --user=USER           XBMC http user
  --password=PASSWORD   XBMC http password
  --ping                Send a ping
  -p, --playpause       Plays or pauses playback
  -s, --stop            Stops playback
  --mute                Mute
  --unmute              Unmute
  -n, --notify          Sends a notification
  -t NOTIFY_TITLE, --title=NOTIFY_TITLE
                        Notification title
  -m NOTIFY_MESSAGE, --message=NOTIFY_MESSAGE
                        Notification message
  --left                Send 'Left' key
  --right               Send 'Right' key
  --up                  Send 'Up' key
  --down                Send 'Down' key
  --back                Send 'Back' key
  --info                Send 'Info' key
  --select              Send 'Select' key
  --sendtext=SENDTEXT   Send a custom text input
  --window=WINDOW       Open a custom window
  --home                Open the Home window
  --weather             Open the Weather window
  --settings            Open the Settings window
  --videos              Open the Videos window
  --scan=SCAN           Scan the given library. Set it to 'audio' or 'video'
  --clean=CLEAN         Clean the given library. Set it to 'audio' or 'video'
```
