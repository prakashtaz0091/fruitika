# tasks.py
from background_task import background
from time import sleep

@background(schedule=3)  # Schedule to run 10 seconds later
def demo_task():
    # Simulate a time-consuming task
    print("Task started... this may take a few seconds...")
    sleep(3)
    print(f'Task completed with arguments:')