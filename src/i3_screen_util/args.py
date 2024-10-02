#!/usr/bin/env python3

import argparse
import os

__version__ = "0.2.3"


class Args:
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog="PROG")
        self.parser.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"{__version__}",
            help="Shows version",
        )
        subparsers = self.parser.add_subparsers(dest="method")

        # organize
        parser_workspace = subparsers.add_parser(
            "organize",
            help="Apply backed up i3wm workspaces or backup i3wm workspaces.",
        )
        parser_workspace.add_argument(
            "-a", "--action", choices=["load", "save"], required=True
        )
        parser_workspace.add_argument("-w", "--workspaces", type=str, required=True)

        # lockscreen
        subparsers.add_parser("lockscreen", help="Prevents lockscreen execution.")

        # toggle
        parser_toggle = subparsers.add_parser("toggle", help="Toggles monitor.")
        parser_toggle.add_argument("-mn", "--monitor-number", type=int, required=True)
        parser_toggle.add_argument("-lt", "--locate-to", choices=["left", "right"])
        parser_toggle.add_argument("-lo", "--locate-of", type=int)

        # screenkey
        subparsers.add_parser("screenkey", help="Toggles screenkey, automatically.")

        args = self.parser.parse_args()
        method = args.method

        self.method = method

        match method:
            case "organize":
                self.action = args.action
                self.workspaces = os.path.abspath(args.workspaces)
            case "lockscreen":
                return
            case "toggle":
                self.monitor_number = args.monitor_number - 1
                self.locate_to = args.locate_to
                self.locate_of = args.locate_of - 1
            case "screenkey":
                return
            case _:
                self.parser.error("Please provide valid operation method.")
