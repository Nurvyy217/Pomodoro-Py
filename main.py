import time
import plyer

def send_notification(title, message):
    plyer.notification.notify(
        title=title,
        message=message,
        timeout=10
    )

def pomodoro_timer(study_time=25, break_time=5):
    while True:
        send_notification("Watunya belajar", "Fokus selama 25 menit!")
        time.sleep(study_time*60)

        send_notification("Waktunya istirahat", "Istirahat selama 5 menit!")
        time.sleep(break_time*60)

if __name__ == "__main__":
    pomodoro_timer()