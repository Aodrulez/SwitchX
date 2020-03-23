import xbox
import argparse
import asyncio
import logging
import os
from contextlib import contextmanager
import random
import time

from joycontrol import logging_default as log
from joycontrol.controller_state import ControllerState, button_push, StickState
from joycontrol.protocol import controller_protocol_factory, Controller
from joycontrol.server import create_hid_server

j=xbox.Joystick()
currentButton=""
controller = Controller.PRO_CONTROLLER
if not os.geteuid() == 0:
	raise PermissionError(' [-] Script must be run as root!')


async def _main(controller, capture_file=None, spi_flash=None):
	factory = controller_protocol_factory(controller, spi_flash=spi_flash)
	transport, protocol = await create_hid_server(factory, 17, 19, capture_file=capture_file)
	await letItRain(protocol.get_controller_state())
	await transport.close()

async def letItRain(controller_state: ControllerState):
	try:
		enabled=True
		calibration = None
		lstick = controller_state.l_stick_state
		rstick = controller_state.r_stick_state
		button_state = controller_state.button_state

		# Button status
		upStatus=False
		downStatus=False
		leftStatus=False
		rightStatus=False
		homeStatus=False
		minusStatus=False
		plusStatus=False
		l_stickStatus=False
		r_stickStatus=False
		aStatus=False
		bStatus=False
		xStatus=False
		yStatus=False
		lStatus=False
		rStatus=False
		zlStatus=False
		zrStatus=False
		waitTime=0

		await controller_state.connect()
		print(" [+] Connected to Switch!")
		while enabled:
			if j.connected():

				# Analog sticks are our priority
				(leftX,leftY) = j.leftStick()
				(rightX,rightY) = j.rightStick()
				rstick.set_h(int(rightX))
				rstick.set_v(int(rightY))
				lstick.set_h(int(leftX))
				lstick.set_v(int(leftY))
				await asyncio.sleep(0)

				if j.dpadUp():
					upStatus=True
					button_state.set_button('up')
					await controller_state.send()
				elif(upStatus):
					upStatus=False
					button_state.set_button('up', pushed=False)
					await controller_state.send()

				if j.dpadDown():
					downStatus=True
					button_state.set_button('down')
					await controller_state.send()
				elif(downStatus):
					downStatus=False
					button_state.set_button('down', pushed=False)
					await controller_state.send()

				if j.dpadLeft():
					leftStatus=True
					button_state.set_button('left')
					await controller_state.send()
				elif(leftStatus):
					leftStatus=False
					button_state.set_button('left', pushed=False)
					await controller_state.send()

				if j.dpadRight():
					rightStatus=True
					button_state.set_button('right')
					await controller_state.send()
				elif(rightStatus):
					rightStatus=False
					button_state.set_button('right', pushed=False)
					await controller_state.send()

				if j.Guide():
					waitTime = waitTime+1
					homeStatus=True
					button_state.set_button('home')
					await controller_state.send()
				elif(homeStatus):
					homeStatus=False
					waitStatus=waitTime
					waitTime=0
					button_state.set_button('home', pushed=False)
					await controller_state.send()
					if(waitStatus > 20):
						await button_push(controller_state,'b')
						await button_push(controller_state,'capture')

				if j.Back():
					minusStatus=True
					button_state.set_button('minus')
					await controller_state.send()
				elif(minusStatus):
					minusStatus=False
					button_state.set_button('minus', pushed=False)
					await controller_state.send()

				if j.Start():
					plusStatus=True
					button_state.set_button('plus')
					await controller_state.send()
				elif(plusStatus):
					plusStatus=False
					button_state.set_button('plus', pushed=False)
					await controller_state.send()

				if j.leftThumbstick():
					l_stickStatus=True
					button_state.set_button('l_stick')
					await controller_state.send()
				elif(l_stickStatus):
					l_stickStatus=False
					button_state.set_button('l_stick', pushed=False)
					await controller_state.send()

				if j.rightThumbstick():
					r_stickStatus=True
					button_state.set_button('r_stick')
					await controller_state.send()
				elif(r_stickStatus):
					r_stickStatus=False
					button_state.set_button('r_stick', pushed=False)
					await controller_state.send()

				if j.A():
					bStatus=True
					button_state.set_button('b')
					await controller_state.send()
				elif(bStatus):
					bStatus=False
					button_state.set_button('b', pushed=False)
					await controller_state.send()

				if j.B():
					aStatus=True
					button_state.set_button('a')
					await controller_state.send()
				elif(aStatus):
					aStatus=False
					button_state.set_button('a', pushed=False)
					await controller_state.send()

				if j.X():
					yStatus=True
					button_state.set_button('y')
					await controller_state.send()
				elif(yStatus):
					yStatus=False
					button_state.set_button('y', pushed=False)
					await controller_state.send()

				if j.Y():
					xStatus=True
					button_state.set_button('x')
					await controller_state.send()
				elif(xStatus):
					xStatus=False
					button_state.set_button('x', pushed=False)
					await controller_state.send()

				if j.leftBumper():
					lStatus=True
					button_state.set_button('l')
					await controller_state.send()
				elif(lStatus):
					lStatus=False
					button_state.set_button('l', pushed=False)
					await controller_state.send()

				if j.rightBumper():
					rStatus=True
					button_state.set_button('r')
					await controller_state.send()
				elif(rStatus):
					rStatus=False
					button_state.set_button('r', pushed=False)
					await controller_state.send()

				if j.leftTrigger():
					zlStatus=True
					button_state.set_button('zl')
					await controller_state.send()
				elif(zlStatus):
					zlStatus=False
					button_state.set_button('zl', pushed=False)
					await controller_state.send()

				if j.rightTrigger():
					zrStatus=True
					button_state.set_button('zr')
					await controller_state.send()
				elif(zrStatus):
					zrStatus=False
					button_state.set_button('zr', pushed=False)
					await controller_state.send()


	finally:
		j.close()

print("\t\t    +------------------+")
print("\t\t    |   SwitchX v1.0   |")
print("\t\t    +------------------+")
print("\t\t    (c) Aodrulez\n")
print("( Adds support for XBOX360 controllers to Nintendo Switch )\n")
with open("controller.bin", 'rb') as spi_flash_file:
		spi_flash = spi_flash_file.read()
loop = asyncio.get_event_loop()
loop.run_until_complete(_main(controller,spi_flash=spi_flash))


