#!/usr/bin/env python3

import argparse


class Args:
    def __init__(self):
        parser = argparse.ArgumentParser(prog="PROG")
        subparsers = parser.add_subparsers(dest="method")

        # organize
        parser_workspace = subparsers.add_parser(
            "organize",
            help="Apply backed up i3wm workspaces or backup i3wm workspaces.",
        )
        parser_workspace.add_argument("-a", "--action", choices=["load", "save"])
        parser_workspace.add_argument("-w", "--workspaces", type=str)

        # lockscreen
        subparsers.add_parser("lockscreen", help="Prevents lockscreen execution.")

        # toggle
        parser_toggle = subparsers.add_parser("toggle", help="Toggles monitor.")
        parser_toggle.add_argument("-mn", "--monitor-number", type=int)
        parser_toggle.add_argument("-lt", "--locate-to", choices=["left", "right"])
        parser_toggle.add_argument("-lo", "--locate-of", type=int)

        args = parser.parse_args()
        method = args.method

        self.method = method

        match method:
            case "organize":
                self.action = args.action
                self.workspaces = args.workspaces
            case "lockscreen":
                return
            case "toggle":
                self.monitor_number = args.monitor_number
                self.locate_to = args.locate_to
                self.locate_of = args.locate_of
            case _:
                parser.error("Please provide valid operation method.")
