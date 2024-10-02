#!/usr/bin/env python3

from .args import Args
from .lockscreen import Lockscreen
from .monitor_controller import MonitorController
from .workspace_formatter import WorkspaceFormatter
from .screenkey import Screenkey


def run_app():
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
            MonitorController.toggle_monitor(
                args.monitor_number, args.locate_to, args.locate_of
            )
        case "screenkey":
            Screenkey.toggle()
