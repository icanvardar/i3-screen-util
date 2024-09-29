from src.i3_screen_util.args import Args
from src.i3_screen_util.monitor_controller import BACKUP_FILE_PATH
from src.i3_screen_util import run_app

import sys
import subprocess
from pathlib import Path


def test_organize_method():
    tmp = sys.argv
    try:
        sys.argv = [
            tmp[0],
            "organize",
            "--action",
            "save",
            "--workspaces",
            "./tmp",
        ]

        args = Args()
        run_app()

        assert args.action == "save"

        for i in range(10):
            workspace_path = Path(f"{args.workspaces}/workspace_{i}.json")
            assert workspace_path.exists() is True

        subprocess.run(f"rm -rf {args.workspaces}", shell=True)

        # TODO: add load workspace test suite as well
    finally:
        sys.argv = tmp


def test_lockscreen_method():
    tmp = sys.argv
    try:
        sys.argv = [
            tmp[0],
            "lockscreen",
        ]

        run_app()

        running_process = subprocess.run(
            "ps -aux | grep control-lockscreen | grep -v grep | awk '{ print $2 }'",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        running_process = running_process.stdout.decode()

        assert len(running_process) > 0

        subprocess.run(
            "ps -aux | grep control-lockscreen | grep -v grep | awk '{ print $2 }' | xargs kill -9",
            shell=True,
        )
    finally:
        sys.argv = tmp


def test_toggle_method():
    tmp = sys.argv
    try:
        sys.argv = [
            tmp[0],
            "toggle",
            "--monitor-number",
            "2",
            "--locate-to",
            "left",
            "--locate-of",
            "1",
        ]

        run_app()
        args = Args()

        assert args.monitor_number == 1
        assert args.locate_to == "left"
        assert args.locate_of == 0

        backup_file_path = Path(BACKUP_FILE_PATH)

        assert backup_file_path.exists() is True
    finally:
        sys.argv = tmp
