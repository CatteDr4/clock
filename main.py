import datetime
import asyncio
import os
import colored
import ctypes


# imports


if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleTitleW("Clock - CattoDragunov")
else:
    pass


async def clock():
    while True:
        """This is a clock"""
        time = datetime.datetime.now()
        print(fr"""{colored.fg(20)}
      ____________
     /\  ________ \
    /  \ \______/\ \
   / /\ \ \  / /\ \ \
  / / /\ \ \/ / /\ \ \
 / / /__\ \ \/_/__\_\ \__________
/ /_/____\ \__________  ________ \
\ \ \____/ / ________/\ \______/\ \
 \ \ \  / / /\ \  / /\ \ \  / /\ \ \
  \ \ \/ / /\ \ \/ / /\ \ \/ / /\ \ \
   \ \/ / /__\_\/ / /__\ \ \/_/__\_\ \
    \  /_/__{colored.fg(228)}{time.strftime("%I:%M:%S %p")}{colored.fg(20)}_\ \___________\
    /  \ \___{colored.fg(228)}{time.strftime("%d %b %Y")}{colored.fg(20)}_/ / _______  /
   / /\ \ \  / /\ \ \  / / /\ \  / / /
  / / /\ \ \/ / /\ \ \/ / /\ \ \/ / /
 / / /__\ \ \/_/__\_\/ / /__\_\/ / /
/ /_/____\ \_________\/ /______\/ /
\ \ \____/ / ________  __________/
 \ \ \  / / /\ \  / / /
  \ \ \/ / /\ \ \/ / /
   \ \/ / /__\_\/ / /
    \  / /______\/ /
     \/___________/BvG{colored.attr("reset")}""")
        await asyncio.sleep(1)
        if os.name == "nt": os.system("cls")
        else: os.system("clear")


loop = asyncio.get_event_loop()
loop.run_until_complete(clock())

# literally a clock
# Credits for the box thingy: https://asciiart.eu
