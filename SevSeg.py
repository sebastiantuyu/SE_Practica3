from machine import Pin

#############################
#                           #
#    Runner an API for      #
#    display on 7 segment   #
#    displays               #
#                           #
#############################
class RunnerV8:
    def __init__(self):
      self.digits = [
        [0, 0, 0, 0, 0, 0, 1, 1], # 0
        [1, 0, 0, 1, 1, 1, 1, 1], # 1
        [0, 0, 1, 0, 0, 1, 0, 1], # 2
        [0, 0, 0, 0, 1, 1, 0, 1], # 3
        [1, 0, 0, 1, 1, 0, 0, 1], # 4
        [0, 1, 0, 0, 1, 0, 0, 1], # 5
        [0, 1, 0, 0, 0, 0, 0, 1], # 6
        [0, 0, 0, 1, 1, 1, 1, 1], # 7
        [0, 0, 0, 0, 0, 0, 0, 1], # 8
        [0, 0, 0, 1, 1, 0, 0, 1] # 9
      ]
      self.pins = [
        Pin(12, Pin.OUT), # A 12
        Pin(13, Pin.OUT), # B 13
        Pin(14, Pin.OUT), # C 14
        Pin(27, Pin.OUT), # D 27
        Pin(26, Pin.OUT), # E 26
        Pin(5, Pin.OUT), # F 5
        Pin(25, Pin.OUT), # G 25
        Pin(4, Pin.OUT) # DP
      ]
      self.delay = 0.15
      self.mux = [Pin(18, Pin.OUT), Pin(2, Pin.OUT)]
      self.STATE = 0

    def mux_position(self, mux):
        if mux == 0:
          self.mux[0].on()
          self.mux[1].off()
        else:
          self.mux[0].off()
          self.mux[1].on()

    def int_to_display(self, position, mux):
      self.mux_position(mux)
      for x in range(len(self.pins) - 1):
        self.pins[x].value(self.digits[position][x])

    def send_data(self, data):
      if data > 9:
        self.int_to_display(int(str(data)[0]), 0)
        self.int_to_display(int(str(data)[1]), 1)
      else:
        self.int_to_display(0, 0)
        self.int_to_display(data, 1)

