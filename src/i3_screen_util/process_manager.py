#!/usr/bin/env python3

import subprocess


class ProcessManager:
    @staticmethod
    def find_and_kill(process_name):
        command = (
            f"ps -aux | grep {process_name}"
            + " | grep -v grep | awk '{ print $2 }' | xargs kill -9"
        )

        subprocess.Popen(command, shell=True)

    @staticmethod
    def find_process(process_name):
        result = subprocess.run(
            f"ps cax | grep {process_name} | grep -o '^[ ]*[0-9]*'",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        ).stdout.decode()

        if len(result):
            return result.split()

        return None
