#!/usr/bin/env python2

from optparse import OptionParser, OptionValueError
import ConfigParser

from xbmcjson import XBMC, PLAYER_VIDEO

class XbmcClient(object):
  def __init__(self, options):
    self.options=options
    self.initializeXbmc()

  def initializeXbmc(self):
    host=self.getHost()
    user=self.getUser()
    password=self.getPassword()
    print host, user, password
    if host is not None:
      self.xbmc=XBMC(self.getJsonRpc(host), user, password)
    else:
      print "No host found"

  def getJsonRpc(self, host):
    jsonrpc="jsonrpc"
    if not host.endswith("/"):
      jsonrpc="/"+jsonrpc
    return host+jsonrpc

  def getHost(self):
    if self.options.host is not None:
      return self.options.host
  def getUser(self):
    if self.options.user is not None:
      return self.options.user
  def getPassword(self):
    if self.options.password is not None:
      return self.options.password

  def execute(self):
    res = None
    if self.options.playpause:
      res = self.xbmc.Player.PlayPause([PLAYER_VIDEO])
    if self.options.stop:
      res = self.xbmc.Player.Stop([PLAYER_VIDEO])
    if self.options.notify:
      title="Notification title"
      message="Notification message"
      if self.options.notify_title is not None:
        title=self.options.notify_title
      if self.options.notify_message is not None:
        message=self.options.notify_message
      res = self.xbmc.GUI.ShowNotification({"title":title, "message":message})
    if self.options.left:
      res = self.xbmc.Input.Left()
    if self.options.right:
      res = self.xbmc.Input.Right()
    if self.options.up:
      res = self.xbmc.Input.Up()
    if self.options.down:
      res = self.xbmc.Input.Down()
    if self.options.back:
      res = self.xbmc.Input.Back()
    if self.options.info:
      res = self.xbmc.Input.Info()
    if self.options.sendtext is not None:
      res= self.xbmc.Input.SendText({"text": self.options.sendtext})
    print res
    if res is not None:
        if res.has_key("result") and res["result"]=="OK":
          exit(0)
        elif res.has_key("error") and res["error"].has_key("message"):
          print res["error"]["message"]
        else:
          print "Unknown error"
    exit(-1)


def main():

  parser = OptionParser("usage: %prog [options]")
  # XBMC instance options
  parser.add_option("--host", action="store", type="string", dest="host", help="XBMC http host")
  parser.add_option("--user", action="store", type="string", dest="user", help="XBMC http user")
  parser.add_option("--password", action="store", type="string", dest="password", help="XBMC http password")

  # Playback options
  parser.add_option("-p","--playpause", action="store_true", dest="playpause", help="Plays or pauses playback")
  parser.add_option("-s","--stop", action="store_true", dest="stop", help="Stops playback")

  # Notifications options
  parser.add_option("-n","--notify", action="store_true", dest="notify", help="Sends a notification")
  parser.add_option("-t","--title", action="store", type="string", dest="notify_title", help="Notification title")
  parser.add_option("-m","--message", action="store", type="string", dest="notify_message", help="Notification message")

  # Input options
  parser.add_option("--left", action="store_true", dest="left", help="Send 'Left' key")
  parser.add_option("--right", action="store_true", dest="right", help="Send 'Right' key")
  parser.add_option("--up", action="store_true", dest="up", help="Send 'Up' key")
  parser.add_option("--down", action="store_true", dest="down", help="Send 'Down' key")
  parser.add_option("--back", action="store_true", dest="back", help="Send 'Back' key")
  parser.add_option("--info", action="store_true", dest="info", help="Send 'Info' key")
  parser.add_option("--sendtext", action="store", type="string", dest="sendtext", help="Send a custom text input")

  # Window options

  (options, args) = parser.parse_args()
  print options
  print args

  p = XbmcClient(options)
  p.execute()

if __name__=="__main__":
  main()
