#!/usr/bin/env python3

import os
import subprocess
from .process_manager import ProcessManager


class Lockscreen:
    @staticmethod
    def control_lockscreen():
        process = ProcessManager.find_process("control-lockscreen")
        if process is not None:
            ProcessManager.find_and_kill("control-lockscreen")

        dirname = os.path.dirname(__file__)
        sc_path = os.path.join(dirname, "./bin/control-lockscreen.sh")
        subprocess.Popen(sc_path, shell=True)
