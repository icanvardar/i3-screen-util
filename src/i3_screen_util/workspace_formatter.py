#!/usr/bin/env python3

import os
import subprocess


class WorkspaceFormatter:
    @staticmethod
    def format_workspace(lines):
        if "splith" in lines[2]:
            lines = lines[2:]
            lines[0] = "{\n"
        else:
            lines = lines[1:]

        return "".join(str(line) for line in lines)

    @classmethod
    def format_and_overwrite(cls, workspaces):
        for i in range(0, 10):
            path = f"{workspaces}/workspace_{i}.json"
            with open(path) as file:
                try:
                    lines = file.readlines()

                    if len(lines) <= 1:
                        continue

                    result = cls.format_workspace(lines).replace("//", "")
                except FileNotFoundError:
                    raise Exception(f"Workspace {i}'s config not found!")
            with open(path, "w") as file:
                file.write(result)

                file.close()

    @staticmethod
    def load_workspaces(workspaces):
        dirname = os.path.dirname(__file__)
        sc_path = os.path.join(dirname, "./bin/load-workspaces.sh")
        subprocess.run(
            f"{sc_path} {workspaces}",
            shell=True,
        )

    @classmethod
    def save_workspaces(cls, workspaces):
        dirname = os.path.dirname(__file__)
        sc_path = os.path.join(dirname, "./bin/save-workspaces.sh")
        subprocess.run(f"{sc_path} {workspaces}", shell=True)

        cls.format_and_overwrite(workspaces)
