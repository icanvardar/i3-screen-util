## i3-screen-util

I originally started building a custom i3 screen management configuration for personal use, but as it grew, I decided to turn it into a project for others to use.

Just for you! <3

### Installation

You can install `i3-screen-util` with pip:

```bash
pip install i3-screen-util
```

### Features

- **Organize Workspaces**: Backup and load i3wm workspaces based on their current layout and position.
- **Prevent Lockscreen**: Automatically disable the lock screen while watching videos, regardless of fullscreen status.
- **Toggle Monitor**: Quickly enable/disable monitors by specifying their monitor number and location.

### Dependencies

Before using `i3-screen-util`, ensure the following tools and packages are installed on your system:

- **playerctl**
- **xautolock**
- **i3-save-tree**
- **i3-msg**
- **xrandr**
- **screenkey**

### API Reference

#### Organize Workspaces

Back up or restore i3wm workspaces.

```bash
i3-screen-util organize --action [load|save] --workspaces <path_to_file>
```

- **--action**: `load` or `save`. Determines whether to restore or backup workspaces.
- **--workspaces**: Path to the file where workspaces will be saved or from where they will be loaded.

#### Prevent Lockscreen

Temporarily disable the lock screen to prevent interruptions while watching videos.

```bash
i3-screen-util lockscreen
```

#### Toggle Monitor

Enable or disable a monitor by specifying its number and optional location positioning.

```bash
i3-screen-util toggle --monitor-number <num> [--locate-to <left|right>] [--locate-of <monitor_number>]
```

- **--monitor-number**: The monitor number to toggle (starting from 1).
- **--locate-to**: Optional. Position the monitor to the left or right of another monitor.
- **--locate-of**: Optional. The monitor number to position relative to.

### License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/icanvardar/i3-screen-util/blob/main/LICENSE) file for details.
