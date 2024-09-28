#!/usr/bin/env python3

import subprocess


class Lockscreen:
    @staticmethod
    def control_lockscreen():
        subprocess.run("./bin/control-lockscreen.sh")
