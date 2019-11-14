#!/usr/bin/python
from phue import Bridge

class Hue:
  def __init__(self):
    self.ip = 'Philips-hue.local'
    self.bridge = Bridge(self.ip)

  def pink(self) :
    self.bridge.set_light('Strip', { 'hue' : 3000, 'bri' : 220 })

  def on(self) :
    self.bridge.set_light('Strip', 'on', True)

  def off(self) :
    self.bridge.set_light('Strip', 'on', False)

  def toggle(self) :
    if self.bridge.get_light('Strip', 'on') :
      self.off()
    else :
      self.on()