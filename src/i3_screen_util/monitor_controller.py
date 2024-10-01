#!/usr/bin/env python3

import json
import os
import re
import subprocess
import sys

BACKUP_FILE_PATH = "/var/tmp/i3-screen-util.data.bin"

# reference: https://www.thinkwiki.org/wiki/Xorg_RandR_1.2#Output_port_names
XRANDR_DISPLAY_TYPES = [
    "VGA",
    "LVDS",
    "DP1",
    "TV",
    "TMDS-1",
    "TMDS-2",
    "LVDS1",
    "VGA1",
    "DVI1",
    "VGA-0",
    "LVDS",
    "S-video",
    "DVI-0",
    "HDMI",
    "DVI",
    "DP",
]


class Backup:
    @staticmethod
    def get_backup_data(options):
        with open(BACKUP_FILE_PATH, "r") as backup_file:
            backup_data = backup_file.read()

            if len(backup_data) == 0:
                data = {}
                for option in options:
                    data[str(option)] = True
                with open(BACKUP_FILE_PATH, "w") as backup_file:
                    tmp = json.dumps(data)
                    backup_file.write(
                        " ".join(format(ord(letter), "b") for letter in tmp)
                    )
                    backup_file.close()
                return data
            else:
                data_raw = "".join(chr(int(x, 2)) for x in backup_data.split())
                return json.loads(data_raw)

    @staticmethod
    def save_backup_data(new_backup_data):
        with open(BACKUP_FILE_PATH, "w") as backup_file:
            tmp = json.dumps(new_backup_data)
            backup_file.write(" ".join(format(ord(letter), "b") for letter in tmp))
            backup_file.close()


class MonitorController:
    @staticmethod
    def turn_off_monitor(monitor_name, backup_data):
        subprocess.run(f"xrandr --output {monitor_name} --off", shell=True)

        backup_data[monitor_name] = False
        Backup.save_backup_data(backup_data)

    @staticmethod
    def turn_on_monitor(monitor_name, to, side_monitor_name, backup_data):
        subprocess.run(
            f"xrandr --output {monitor_name} --auto --{to}-of {side_monitor_name}",
            shell=True,
        )

        backup_data[monitor_name] = True
        Backup.save_backup_data(backup_data)

    @staticmethod
    def get_monitor_options():
        monitors_raw = subprocess.run(
            "xrandr", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )

        # wow i can do regex search UwU
        pattern = r"([A-Za-z]+-\d+) connected"
        displays = re.findall(pattern, monitors_raw.stdout.decode())
        return [
            display
            for display in displays
            if any(display.startswith(dt) for dt in XRANDR_DISPLAY_TYPES)
        ]

    @classmethod
    def toggle_monitor(cls, monitor_number, locate_to, locate_of):
        if os.path.exists(BACKUP_FILE_PATH) is False:
            with open(BACKUP_FILE_PATH, "w") as backup_file:
                backup_file.close()
                pass

        options = MonitorController.get_monitor_options()

        try:
            monitor_name = options[monitor_number]
            side_monitor_name = None
            if locate_of is not None:
                side_monitor_name = options[locate_of]

            backup_data = Backup.get_backup_data(options)

            is_turned_on = backup_data[monitor_name]

            if is_turned_on is True:
                cls.turn_off_monitor(monitor_name, backup_data)
            else:
                if locate_to is None or side_monitor_name is None:
                    raise Exception(
                        "'locate_to' or 'location_of' arguments cannot be None."
                    )

                cls.turn_on_monitor(
                    monitor_name, locate_to, side_monitor_name, backup_data
                )
        except IndexError:
            raise Exception("Invalid monitor number.")
        except Exception:
            sys.exit(0)
