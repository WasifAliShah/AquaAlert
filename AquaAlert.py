import datetime
import win32com.client
from winotify import Notification, audio

def create_notification():
    toast = Notification(app_id="Water Assistant",
                         title="Time to drink Water",
                         msg="2 hours have passed since your last water break.",
                         duration="short",
                         icon="C:\\Python_harry_tut\\images.jpg")
    toast.set_audio(audio.Default, loop=False)
    toast.show()

def create_triggers(task_def, start_time, interval_hours, trigger_count):
    TASK_TRIGGER_DAILY = 2
    for i in range(trigger_count):
        trigger = task_def.Triggers.Create(TASK_TRIGGER_DAILY)
        trigger.StartBoundary = (start_time + datetime.timedelta(hours=i * interval_hours)).isoformat()
        trigger.DaysInterval = 1  # Repeat every day

def create_action(task_def):
    TASK_ACTION_EXEC = 0
    action = task_def.Actions.Create(TASK_ACTION_EXEC)
    action.ID = 'Water Reminder'
    action.Path = 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    action.Arguments = 'C:\\Python_harry_tut\\Drink_water_proj.py'

def configure_task(task_def):
    task_def.RegistrationInfo.Description = 'Water Reminder Task'
    task_def.Settings.Enabled = True
    task_def.Settings.StopIfGoingOnBatteries = False
    task_def.Settings.DisallowStartIfOnBatteries = False  # Allow task to start on battery

def register_task(task_def):
    TASK_CREATE_OR_UPDATE = 6
    TASK_LOGON_NONE = 0
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')
    root_folder.RegisterTaskDefinition(
        'Water Reminder Task',  # Task name
        task_def,
        TASK_CREATE_OR_UPDATE,
        '',  # No user
        '',  # No password
        TASK_LOGON_NONE  # Run whether user is logged in or not
    )

def main():
    try:
        create_notification()

        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        root_folder = scheduler.GetFolder('\\')
        task_def = scheduler.NewTask(0)

        start_time = datetime.datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
        create_triggers(task_def, start_time, interval_hours=2, trigger_count=7)
        create_action(task_def)
        configure_task(task_def)
        register_task(task_def)

        print("Task successfully registered.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
