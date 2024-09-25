#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from workspace_formatter import WorkspaceFormatter
from monitor_controller import MonitorController


def main():
    WorkspaceFormatter.try_me()
    MonitorController.test()


if __name__ == "__main__":
    main()
