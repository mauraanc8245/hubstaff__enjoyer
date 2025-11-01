# Hubstaff Activity Simulator

Python script for simulating mouse activity to test Hubstaff activity tracker monitoring.

## Description

This script simulates random mouse movements with configurable intervals, maintaining activity level between 70-90%. The script runs for a specified duration (default: 10 minutes) and displays statistics for each 10-minute period.

## Requirements

- Python 3.7 or newer
- PyAutoGUI for mouse control

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Run

```bash
python hubstaff_activity_simulator.py
```

Runs simulation with default parameters:
- Minimum delay: 5 seconds
- Maximum delay: 15 seconds
- Duration: 10 minutes

### Custom Parameters

```bash
python hubstaff_activity_simulator.py --delay-min 3 --delay-max 12 --duration 20
```

**Parameters:**
- `--delay-min` - minimum delay between activities (seconds, default: 5)
- `--delay-max` - maximum delay between activities (seconds, default: 15)
- `--duration` - simulation duration (minutes, default: 10)

## How It Works

1. **Initialization**: The script detects screen size and sets a random activity level between 70-90%.

2. **Mouse Movements**: The script performs three types of movements:
   - **Smooth movements** - gradual movement between two points
   - **Direct movements** - fast movement to target position
   - **Chaotic movements** - movement through multiple intermediate points

3. **Activity Control**: The script calculates active time and idle time to maintain the target activity level (70-90%).

4. **Statistics**: Every 10 minutes, period statistics are displayed:
   - Period duration
   - Number of activities
   - Activity rate for the period

5. **Safety**: To stop the script, move the mouse to the corner of the screen (failsafe) or press `Ctrl+C`.

## Example Output

```
Starting activity simulation for 10 minutes
Activity rate: 78.5%
Delay range: 5-15 seconds
Press Ctrl+C to stop

Starting in 3 seconds...

Period 1 completed:
  Duration: 10.00 minutes
  Activities: 45
  Activity rate: 82.3%

Session completed:
Total duration: 10.00 minutes
Periods completed: 1
```

## Future Features

The script is designed with scalability in mind. Future versions plan to include:
- Keyboard shortcut simulation
- Configurable activity level
- Additional activity types

## Notes

- Make sure Hubstaff tracker is running before starting the simulation
- The script works in the current desktop environment
- Use failsafe (move mouse to corner) or Ctrl+C to stop
