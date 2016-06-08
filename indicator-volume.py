#!/usr/bin/python

import os
import signal
import json
import names

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify


def main():
    cwd=os.path.dirname(__file__)+'/volume.png'
    print(cwd)
    indicator = appindicator.Indicator.new("Indicator Volume", os.path.abspath(cwd), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()

def build_menu():
    menu = gtk.Menu()
    item_110 = gtk.MenuItem('110%')
    item_110.connect('activate', volume_110)
    menu.append(item_110)

    item_120 = gtk.MenuItem('120%')
    item_120.connect('activate', volume_120)
    menu.append(item_120)

    item_130 = gtk.MenuItem('130%')
    item_130.connect('activate', volume_130)
    menu.append(item_130)

    item_140 = gtk.MenuItem('140%')
    item_140.connect('activate', volume_140)
    menu.append(item_140)

    item_150 = gtk.MenuItem('150%')
    item_150.connect('activate', volume_150)
    menu.append(item_150)

    item_hdmi = gtk.MenuItem('HDMI Output')
    item_hdmi.connect('activate', hdmi)
    menu.append(item_hdmi)

    item_pc = gtk.MenuItem('PC Output')
    item_pc.connect('activate', pc)
    menu.append(item_pc)

    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def volume_110(_):
    os.system("pactl set-sink-volume 0 110%")
    notify.init("Volume set to 110%")


def volume_120(_):
    os.system("pactl set-sink-volume 0 120%")
    notify.init("Volume set to 120%")


def volume_130(_):
    os.system("pactl set-sink-volume 0 130%")
    notify.init("Volume set to 130%")


def volume_140(_):
    os.system("pactl set-sink-volume 0 140%")
    notify.init("Volume set to 140%")


def volume_150(_):
    os.system("pactl set-sink-volume 0 150%")
    notify.init("Volume set to 150%")

def hdmi(_):
    os.system("pactl set-card-profile 0 output:"+names.hdmi_audio)
    os.system("xrandr --output "+names.pc_monitor+" --auto")
    os.system("xrandr --output "+names.hdmi_monitor+" --auto")
    os.system("xrandr --output "+names.pc_monitor+" --off")
    

def pc(_):
    os.system("pactl set-card-profile 0 output:"+names.pc_audio)
    os.system("xrandr --output "+names.hdmi_monitor+" --auto")
    os.system("xrandr --output "+names.pc_monitor+" --auto")
    os.system("xrandr --output "+names.hdmi_monitor+" --off")

def quit(_):
    notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
