#!/usr/bin/env python

import os
from optparse import OptionParser, OptionValueError
import ConfigParser

from xbmcjson import XBMC, PLAYER_VIDEO

class XbmcClient(object):
  def __init__(self, options):
    self.options=options
    self.config = ConfigParser.SafeConfigParser()
    self.initializeConfig()
    self.initializeXbmc()

  def initializeConfig(self):
    if self.options.config is not None:
      if os.path.exists(self.options.config):
        self.config.read(self.options.config)
      else:
        raise Exception("The file '%s' does not exists"%(self.options.config))
    else:
        self.config.read(self.getDefaultConfig())


  def getDefaultConfig(self):
    cfgfile=None
    try:
      import xdg.BaseDirectory as bd
      cfgfile= os.path.join(bd.xdg_config_home, "xbmc-client","config")
    except:
      home = os.path.expanduser("~")
      if home == "~":
        log.error("Could not get default configuration path location using XDG (freedesktop).")
        exit(2)
      cfgfile= os.path.join(home, ".config", "xbmc-client", "config")
    return cfgfile

  def initializeXbmc(self):
    host=self.getHost()
    user=self.getUser()
    password=self.getPassword()
    if host is None or host=="":
      raise Exception("No host found. Have you configured the default config file %s ?"%(self.getDefaultConfig()))
    if user is None or user=="":
      raise Exception("No user found. Have you configured the default config file %s ?"%(self.getDefaultConfig()))
    self.xbmc=XBMC(self.getJsonRpc(host), user, password)

  def getJsonRpc(self, host):
    jsonrpc="jsonrpc"
    if not host.endswith("/"):
      jsonrpc="/"+jsonrpc
    return host+jsonrpc

  def getHost(self):
    #Command line always override config
    if self.options.host is not None:
      return self.options.host
    return self.config.get("xbmc","host")
  def getUser(self):
    #Command line always override config
    if self.options.user is not None:
      return self.options.user
    return self.config.get("xbmc","user")
  def getPassword(self):
    if self.options.password is not None:
      return self.options.password
    return self.config.get("xbmc","password")

  def openWindow(self, windowname):
    return self.xbmc.GUI.ActivateWindow(window=windowname)

  def execute(self):
    res = None
    if self.options.ping:
      res = self.xbmc.JSONRPC.Ping()
    if self.options.playpause:
      res = self.xbmc.Player.PlayPause([PLAYER_VIDEO])
    if self.options.stop:
      res = self.xbmc.Player.Stop([PLAYER_VIDEO])
    if self.options.notify:
      _title="Notification title"
      _message="Notification message"
      if self.options.notify_title is not None:
        _title=self.options.notify_title
      if self.options.notify_message is not None:
        _message=self.options.notify_message
      res = self.xbmc.GUI.ShowNotification(title=_title, message=_message)
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
    if self.options.select:
      res = self.xbmc.Input.Select()
    if self.options.sendtext is not None:
      res= self.xbmc.Input.SendText(text = self.options.sendtext)
    if self.options.mute:
      res = self.xbmc.Application.SetMute(mute=True)
    if self.options.unmute:
      res = self.xbmc.Application.SetMute(mute=False)
    if self.options.window is not None:
      res = self.openWindow(self.options.window)
    if self.options.scan is not None:
      if self.options.scan == "video":
        res = self.xbmc.VideoLibrary.Scan()
      elif self.options.scan == "music":
        res = self.xbmc.AudioLibrary.Scan()
      else:
        print "Unsupported library type : '%s'"%(self.options.scan)
    if self.options.clean is not None:
      if self.options.clean == "video":
        res = self.xbmc.VideoLibrary.Clean()
      elif self.options.clean == "music":
        res = self.xbmc.AudioLibrary.Clean()
      else:
        print "Unsupported library type : '%s'"%(self.options.clean)
    if res is not None:
      success=False
      if res.has_key("result") and (res["result"]=="OK" or res["result"]==True):
        success=True
      elif res.has_key("result") and res["result"]=="pong":
        success=True
      elif res.has_key("result") and res["result"]==False and self.options.unmute:
        # unmute always send me a result == False, even when it"s ok...
        success=True
      elif res.has_key("error") and res["error"].has_key("message"):
        print res["error"]["message"]
      else:
        print "Unknown error : '%s'"%(res)
      if success:
        print "Success."
        exit(0)
    exit(-1)


def main():
  def customWindow(option, opt, value, parser):
    """Open custom window"""
    # define here the mapping between the parametre and the associated window
    WINWOWS={
        '--home' : 'home',
        '--weather' : 'weather',
        '--settings' : 'settings',
        '--videos' : 'videos',
        }
    if WINWOWS.has_key(opt):
      parser.values.window=WINWOWS[opt]


  parser = OptionParser("usage: %prog [options]")
  # Config options
  parser.add_option("-c","--config", action="store", type="string", dest="config", help="Configuration file. Default is located in ~/.config/xbmc-client/config")

  # XBMC instance options
  parser.add_option("--host", action="store", type="string", dest="host", help="XBMC http host")
  parser.add_option("--user", action="store", type="string", dest="user", help="XBMC http user")
  parser.add_option("--password", action="store", type="string", dest="password", help="XBMC http password")

  # JSONRPC options
  parser.add_option("--ping", action="store_true", dest="ping", help="Send a ping")
  
  # Playback options
  parser.add_option("-p","--playpause", action="store_true", dest="playpause", help="Plays or pauses playback")
  parser.add_option("-s","--stop", action="store_true", dest="stop", help="Stops playback")

  # Volume options
  parser.add_option("--mute", action="store_true", dest="mute", help="Mute")
  parser.add_option("--unmute", action="store_true", dest="unmute", help="Unmute")


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
  parser.add_option("--select", action="store_true", dest="select", help="Send 'Select' key")
  parser.add_option("--sendtext", action="store", type="string", dest="sendtext", help="Send a custom text input")

  # Window options
  parser.add_option("--window", action="store", type="string", dest="window", help="Open a custom window")
  # Specifics windows are managed by the callback
  parser.add_option("--home", action="callback", dest="home", help="Open the Home window", callback=customWindow)
  parser.add_option("--weather", action="callback", dest="weather", help="Open the Weather window", callback=customWindow)
  parser.add_option("--settings", action="callback", dest="settings", help="Open the Settings window", callback=customWindow)
  parser.add_option("--videos", action="callback", dest="videos", help="Open the Videos window", callback=customWindow)

  # Library options
  parser.add_option("--scan", action="store", type="string", dest="scan", help="Scan the video library by default. Set it to 'audio' or 'video'")
  parser.add_option("--clean", action="store", type="string", dest="clean", help="Clean the given library by default. Set it to 'audio' or 'video'")

  (options, args) = parser.parse_args()

  p = XbmcClient(options)
  p.execute()

if __name__=="__main__":
  main()
