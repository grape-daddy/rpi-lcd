#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Example: Scrolling text on display if the string length is major than columns in display.
# Created by Dídac García.

import os
from dotenv import load_dotenv
from subprocess import check_output

# Import necessary libraries for communication and display use
import drivers
from time import sleep

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()
load_dotenv()

ipv4 = check_output(["hostname", "-I"], encoding="utf-8").split()[0]
mqtt_broker = os.getenv('MQTT_BROKER')
	
def mqtt_broker_string(display, text='', num_line=1, num_cols=16):
	if (len(text) + 8) > num_cols:
		display.lcd_display_string(text[:num_cols], num_line)
		sleep(1)
		for i in range((len(text) + 8) - num_cols + 1):
			text_to_print = "BROKER: " + text[i:i+num_cols]
			display.lcd_display_string(text_to_print, num_line)
			sleep(0.2)
		sleep(1)
	else:
		display.lcd_display_string(text, num_line)
			
def long_string(display, text='', num_line=1, num_cols=16):
	""" 
	Parameters: (driver, string to print, number of line to print, number of columns of your display)
	Return: This function send to display your scrolling string.
	"""
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
			
# Main body of code
try:
	print("Press CTRL + C to stop this script!")

	# Example of short string
	long_string(display, str(ipv4), 1)
	sleep(1)

	# Example of long string
	mqtt_broker_string(display, str(mqtt_broker), 2)
	display.lcd_clear()
	sleep(1)

	while True:
		long_string(display, str(ipv4), 1)
		# An example of infinite scrolling text
		mqtt_broker_string(display, str(mqtt_broker), 2)
except KeyboardInterrupt:
	# If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
	display.lcd_clear()
	print("Cleaning up!")
