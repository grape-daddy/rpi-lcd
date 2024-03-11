#! /usr/bin/env python

import drivers
from time import sleep
from datetime import datetime
from dotenv import load_dotenv
from subprocess import check_output
display = drivers.Lcd()
load_dotenv()
IP = check_output(["hostname", "-I"], encoding="utf8").split()[0]
mqtt_broker = os.getenv('MQTT_BROKER')
try:
  print("Writing to display")
  def long_string(display, text='', num_line=1, num_cols=16):
    if len(text) > num_cols:
      display.lcd_display_string(text[:num_cols], num_line)
			sleep(1)
			for i in range(len(text) - num_cols + 1):
				text_to_print = text[i:i+num_cols]
				display.lcd_display_string(text_to_print, num_line)
				sleep(0.2)
			sleep(1)
		else:
			display.lcd_display_string(text, num_line)
      
  while True:
    # display.lcd_display_string(str(datetime.now().time()), 1)
    # display.lcd_display_string(str(IP), 2)
    display.lcd_display_string(str(IP), 1)
    display.lcd_display_string(str(mqtt_broker), 2)
    # Uncomment the following line to loop with 1 sec delay
    # sleep(1)
except KeyboardInterrupt:
  # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
  print("Cleaning up!")
  display.lcd_clear()
