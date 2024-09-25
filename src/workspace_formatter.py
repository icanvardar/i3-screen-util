#!/usr/bin/env python3

import os


class WorkspaceFormatter:
    # deletes slashes
    @staticmethod
    def format_workspace(lines):
        if "splith" in lines[2]:
            lines = lines[2:]
            lines[0] = "{\n"
        else:
            lines = lines[1:]

        return "".join(str(line) for line in lines)

    @classmethod
    def format_and_overwrite(cls):
        for i in range(0, 10):
            path = os.path.expanduser(
                f"~/.dotfiles/i3/.config/i3/workspaces/workspace_{i}.json"
            )
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
    def try_me():
        print("try me")
