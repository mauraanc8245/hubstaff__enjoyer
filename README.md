# Hubstaff Activity Simulator

Python script for simulating realistic human activity (mouse, keyboard, scrolling, app switching) to test Hubstaff activity tracker monitoring.

## Description

This script simulates realistic human computer activity including mouse movements, keyboard typing, scrolling, application switching, and window management. It maintains activity level between 70-90% and runs continuously until manually stopped. The script displays statistics for each 10-minute period.

## Requirements

- Python 3.7 or newer
- PyAutoGUI for mouse control

## Installation

1. Install dependencies:

```bash
pip3 install -r requirements.txt
```

**Note**: On macOS, use `python3` and `pip3` instead of `python` and `pip`.

## Usage

### Basic Run

```bash
python3 hubstaff_activity_simulator.py
```

Runs simulation continuously until stopped (Ctrl+C or fail-safe):
- Minimum delay: 5 seconds
- Maximum delay: 15 seconds
- Duration: unlimited (runs until manually stopped)

### Custom Parameters

```bash
python3 hubstaff_activity_simulator.py --delay-min 3 --delay-max 12 --duration 20
```

**Parameters:**
- `--delay-min` - minimum delay between activities (seconds, default: 5)
- `--delay-max` - maximum delay between activities (seconds, default: 15)
- `--duration` - simulation duration in minutes (default: unlimited, runs until stopped)

## How It Works

1. **Initialization**: The script detects screen size and sets a random activity level between 70-90%.

2. **Activity Types**: The script performs various realistic activities:
   - **Mouse movements** - smooth, direct, and chaotic movements across the screen
   - **Keyboard typing** - simulates typing random text with occasional backspaces
   - **Keyboard shortcuts** - common shortcuts like copy, paste, save, undo, etc.
   - **Mouse scrolling** - vertical scrolling in both directions
   - **Application switching** - switches between applications using Command+Tab (macOS)
   - **Window management** - opens/closes windows, tabs, and file dialogs

3. **Natural Activity Sequence**: Activities are organized in a realistic pattern:
   - Application switching occurs periodically (every 8th cycle)
   - Window switching within apps (every 12th cycle)
   - File operations and new windows/tabs (every 15th cycle)
   - Window/tab closing (every 20th cycle)
   - Mixed mouse, keyboard, and scrolling actions with natural timing

4. **Activity Control**: The script calculates active time and idle time to maintain the target activity level (70-90%).

5. **Statistics**: Every 10 minutes, period statistics are displayed:
   - Period duration
   - Number of activities
   - Activity rate for the period

6. **Safety**: To stop the script, move the mouse to the corner of the screen (failsafe) or press `Ctrl+C`.

## Example Output

```
Starting continuous activity simulation (run until stopped)
Activity rate: 78.5%
Delay range: 5-15 seconds
Press Ctrl+C to stop, or move mouse to screen corner for fail-safe

Starting in 3 seconds...

Period 1 completed:
  Duration: 10.00 minutes
  Activities: 45
  Activity rate: 82.3%

Session completed:
Total duration: 10.00 minutes
Periods completed: 1
```

## Features

- **Realistic Mouse Activity**: Smooth, direct, and chaotic mouse movements
- **Keyboard Simulation**: Text typing with realistic intervals and shortcuts
- **Application Switching**: Automatic switching between applications
- **Window Management**: Opening/closing windows, tabs, and file dialogs
- **Scrolling**: Natural mouse wheel scrolling
- **Natural Timing**: Human-like delays and activity patterns
- **Fail-Safe Protection**: Stop by moving mouse to screen corner

## Notes

- Make sure Hubstaff tracker is running before starting the simulation
- The script works in the current desktop environment
- Use failsafe (move mouse to corner) or Ctrl+C to stop
