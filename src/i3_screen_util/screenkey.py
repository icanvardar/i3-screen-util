#!/usr/bin/env python3

import subprocess
from .process_manager import ProcessManager


class Screenkey:
    @staticmethod
    def show():
        subprocess.Popen(
            "screenkey",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

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
