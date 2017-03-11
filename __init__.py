# coding=utf-8
from __future__ import absolute_import, division, print_function

__author__ = "Ryan Gimmy <ry.gimmy@gmail.com>"
__license__ = 'GNU Affero General Public License http://www.gnu.org/licenses/agpl.html'
__copyright__ = "Copyright (C) 2017 rgimmy.com - Released under terms of the AGPLv3 License"

import octoprint.plugin

import RPi.GPIO as GPIO
import flask


class RelayPlugin(octoprint.plugin.AssetPlugin,
				  octoprint.plugin.SettingsPlugin,
				  octoprint.plugin.BlueprintPlugin,
				  octoprint.plugin.StartupPlugin,
				  octoprint.plugin.TemplatePlugin):
	relay_state = 0
	gpio_pin = 3

	def __init__(self):
		print("initting relay monitor")
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.gpio_pin, GPIO.OUT, initial=GPIO.LOW)

	@octoprint.plugin.BlueprintPlugin.route("/toggleRelay", methods=["POST"])
	def toggleRelay(self):
		if self.relay_state == 0:
			# turn on
			self.relay_state = 1
			print("turning on relay")
			GPIO.output(self.gpio_pin, GPIO.HIGH)
			return "1"
		else:
			# turn off
			self.relay_state = 0
			print("turning off relay")
			GPIO.output(self.gpio_pin, GPIO.LOW)
			return "0"

	def get_assets(self):
		return dict(js=["js/relay.js"])

	def get_template_vars(self):
		return dict(
			homepage=__plugin_url__
		)

	def get_template_configs(self):
		return [
			dict(type="navbar", template="relay_navbar.jinja2"),
		]

__plugin_name__ = "Relay Plugin"
__plugin_url__ = "pluginurl"
__plugin_implementation__ = RelayPlugin()
