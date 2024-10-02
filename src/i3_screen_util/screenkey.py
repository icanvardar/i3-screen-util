#!/usr/bin/env python3

import subprocess
from .process_manager import ProcessManager


class Screenkey:
    @staticmethod
    def show():
        # double check if there is any screenkey ran before, manually
        ProcessManager.find_and_kill("screenkey")

        subprocess.Popen("screenkey")

    @staticmethod
    def hide():
        ProcessManager.find_and_kill("screenkey")

    @classmethod
    def toggle(cls):
        process = ProcessManager.find_process("screenkey")

        if process is not None:
            cls.hide()
        else:
            cls.show()
