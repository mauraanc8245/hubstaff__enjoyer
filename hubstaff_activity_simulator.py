#!/usr/bin/env python3

import pyautogui
import random
import time
import sys
import argparse
from typing import Tuple
from datetime import datetime, timedelta

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0


class ActivitySimulator:
    def __init__(self, delay_min: int, delay_max: int, target_min: int = 10):
        self.delay_min = delay_min
        self.delay_max = delay_max
        self.target_minutes = target_min
        self.screen_width, self.screen_height = pyautogui.size()
        self.activity_rate = random.uniform(0.70, 0.90)
        
    def get_random_position(self) -> Tuple[int, int]:
        margin = 50
        x = random.randint(margin, self.screen_width - margin)
        y = random.randint(margin, self.screen_height - margin)
        return (x, y)
    
    def smooth_movement(self, start_pos: Tuple[int, int], end_pos: Tuple[int, int], steps: int = 10):
        for i in range(steps):
            t = i / steps
            x = int(start_pos[0] + (end_pos[0] - start_pos[0]) * t)
            y = int(start_pos[1] + (end_pos[1] - start_pos[1]) * t)
            pyautogui.moveTo(x, y, duration=0.05)
    
    def perform_activity(self):
        current_pos = pyautogui.position()
        target_pos = self.get_random_position()
        
        movement_type = random.choice(['smooth', 'direct', 'chaotic'])
        
        if movement_type == 'smooth':
            self.smooth_movement(current_pos, target_pos)
        elif movement_type == 'direct':
            pyautogui.moveTo(target_pos[0], target_pos[1], duration=random.uniform(0.1, 0.3))
        else:
            intermediate_steps = random.randint(2, 5)
            prev_pos = current_pos
            for _ in range(intermediate_steps):
                intermediate_pos = self.get_random_position()
                self.smooth_movement(prev_pos, intermediate_pos, steps=5)
                prev_pos = intermediate_pos
                time.sleep(random.uniform(0.01, 0.05))
            self.smooth_movement(prev_pos, target_pos, steps=5)
    
    def calculate_active_time(self) -> float:
        base_interval = (self.delay_min + self.delay_max) / 2
        active_time = base_interval * self.activity_rate
        return active_time
    
    def calculate_idle_time(self) -> float:
        active_time = self.calculate_active_time()
        base_interval = (self.delay_min + self.delay_max) / 2
        idle_time = base_interval * (1 - self.activity_rate)
        return idle_time
    
    def run_cycle(self, start_time: datetime, session_end: datetime):
        if datetime.now() >= session_end:
            return False
        
        remaining = (session_end - datetime.now()).total_seconds()
        if remaining <= 0:
            return False
        
        self.perform_activity()
        
        active_duration = self.calculate_active_time()
        idle_duration = self.calculate_idle_time()
        
        time.sleep(idle_duration)
        
        return True
    
    def run(self):
        print(f"Starting activity simulation for {self.target_minutes} minutes")
        print(f"Activity rate: {self.activity_rate:.1%}")
        print(f"Delay range: {self.delay_min}-{self.delay_max} seconds")
        print(f"Press Ctrl+C to stop")
        print("\nStarting in 3 seconds...")
        time.sleep(3)
        
        session_start = datetime.now()
        session_end = session_start + timedelta(minutes=self.target_minutes)
        
        period_start = session_start
        period_count = 0
        activity_count = 0
        
        try:
            while datetime.now() < session_end:
                remaining_total = (session_end - datetime.now()).total_seconds()
                
                if self.run_cycle(session_start, session_end):
                    activity_count += 1
                    remaining_period = (period_start + timedelta(minutes=10) - datetime.now()).total_seconds()
                    
                    if remaining_period <= 0 or datetime.now() >= period_start + timedelta(minutes=10):
                        period_duration = (datetime.now() - period_start).total_seconds()
                        if period_duration > 0:
                            period_activity_rate = min(activity_count * (self.delay_min + self.delay_max) / 2 / period_duration, 1.0)
                            print(f"\nPeriod {period_count + 1} completed:")
                            print(f"  Duration: {period_duration/60:.2f} minutes")
                            print(f"  Activities: {activity_count}")
                            print(f"  Activity rate: {period_activity_rate:.1%}")
                        
                        period_start = datetime.now()
                        period_count += 1
                        activity_count = 0
                else:
                    break
                    
                if remaining_total <= 0:
                    break
                    
        except KeyboardInterrupt:
            print("\n\nSimulation stopped by user")
        
        total_duration = (datetime.now() - session_start).total_seconds()
        print(f"\n\nSession completed:")
        print(f"Total duration: {total_duration/60:.2f} minutes")
        print(f"Periods completed: {period_count}")


def main():
    parser = argparse.ArgumentParser(
        description='Hubstaff Activity Simulator - Simulates mouse activity for testing Hubstaff tracking'
    )
    parser.add_argument(
        '--delay-min',
        type=int,
        default=5,
        help='Minimum delay between activities in seconds (default: 5)'
    )
    parser.add_argument(
        '--delay-max',
        type=int,
        default=15,
        help='Maximum delay between activities in seconds (default: 15)'
    )
    parser.add_argument(
        '--duration',
        type=int,
        default=10,
        help='Simulation duration in minutes (default: 10)'
    )
    
    args = parser.parse_args()
    
    if args.delay_min < 1 or args.delay_max < 1:
        print("Error: Delays must be at least 1 second")
        sys.exit(1)
    
    if args.delay_min > args.delay_max:
        print("Error: Minimum delay cannot be greater than maximum delay")
        sys.exit(1)
    
    if args.duration < 1:
        print("Error: Duration must be at least 1 minute")
        sys.exit(1)
    
    simulator = ActivitySimulator(
        delay_min=args.delay_min,
        delay_max=args.delay_max,
        target_min=args.duration
    )
    
    simulator.run()


if __name__ == '__main__':
    main()

