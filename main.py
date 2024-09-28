#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src/i3_screen_util"))

from workspace_formatter import WorkspaceFormatter
from lockscreen import Lockscreen
from monitor_controller import MonitorController
from args import Args


def main():
    args = Args()

    match args.method:
        case "organize":
            if args.action == "load":
                WorkspaceFormatter.load_workspaces(args.workspaces)
            elif args.action == "save":
                WorkspaceFormatter.save_workspaces(args.workspaces)
        case "lockscreen":
            Lockscreen.control_lockscreen()
        case "toggle":
            MonitorController.toggle(
                args.monitor_number, args.locate_to, args.locate_of
            )


if __name__ == "__main__":
    main()
