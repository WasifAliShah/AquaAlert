# WaterReminder

WaterReminder is a Python script that helps you stay hydrated by reminding you to drink water at regular intervals throughout the day. It uses the Windows Task Scheduler to ensure notifications are shown even if you are logged out or your computer is running on battery power.

## Features

- Sends a notification to remind you to drink water.
- Configurable intervals between reminders (default is 3 hours).
- Runs every day of the week.
- Uses the Windows Task Scheduler to ensure reliability.

## Prerequisites

- Python 3.x
- `winotify` library
- `pywin32` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/WaterReminder.git
    cd WaterReminder
    ```

2. Install the required Python libraries:

    ```bash
    pip install winotify pywin32
    ```

3. Ensure you have an image for the notification icon. You can use the provided `images.jpg` or your own image. Place it in the appropriate directory.

## Usage

1. Open the `Drink_water_proj.py` file and adjust the settings if necessary:
    - Change the interval between reminders.
    - Modify the start time for reminders.

2. Run the script to set up the reminders:

    ```bash
    python Drink_water_proj.py
    ```

3. The script will create a scheduled task that sends notifications at the specified intervals.

## Customization

### Change Reminder Intervals

To change the intervals between reminders, modify the `interval_hours` parameter in the `create_triggers` function in the script:

'''python
create_triggers(task_def, start_time, interval_hours=3, trigger_count=7)'''

### Change Start Time

To change the start time for the reminders, modify the `start_time` variable:

'''python
start_time = datetime.datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)'''





