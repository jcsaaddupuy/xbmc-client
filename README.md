xbmc-client
===========

xbmc-client is a XBMC command line client which control your XBMC instance throught JSON API.

```sh
pip install xbmc-client
```

Available options :

```sh
Usage: xbmc-client [options]

Options:
  -h, --help            show this help message and exit
  -c CONFIG, --config=CONFIG
                        Configuration file. Default is located in
                        ~/.config/xbmc-client/config
  --host=HOST           XBMC http host. Will override configuration.
  --user=USER           XBMC http user. Will override the configuration.
  --password=PASSWORD   XBMC http password. Will override the configuration.
  --ping                Send a ping
  -p, --playpause       Plays or pauses playback
  -s, --stop            Stops playback
  --mute                Mute
  --unmute              Unmute
  --volume=VOLUME       Set the volume to the given value
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
  --url=URL             Play a URL
  --youtube=YOUTUBE_URL
                        Open a youtube url
  --window=WINDOW       Open a custom window
  --home                Open the Home window
  --weather             Open the Weather window
  --settings            Open the Settings window
  --videos              Open the Videos window
  --scan=SCAN           Scan the given library. Set it to 'audio' or 'video'
  --clean=CLEAN         Clean the given library. Set it to 'audio' or 'video'
  --addon=ADDON_ID      Execute the given addon. Parameters not yet
                        supporteds.

```
