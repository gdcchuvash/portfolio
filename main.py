from datetime import datetime
from playsound import playsound

def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return "Не тот формат, пожалуйста повторите"
    else:
        if int(alarm_time[0:2]) > 23:
            return "Не тот формат, пожалуйста повторите"
        elif int(alarm_time[3:5]) > 59:
            return "Не тот формат, пожалуйста повторите"
        elif int(alarm_time[6:8]) > 59:
            return "Не тот формат, пожалуйста повторите"
        else:
            return "ок"

while True:
    alarm_time = input("Введите время в формате 'HH:MM:SS':")

    validate = validate_time(alarm_time.lower())
    if validate != 'ок':
        print(validate)
    else:
        print(f"Установка будильника для {alarm_time}")
        break

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]

while True:
    now = datetime.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")

    if alarm_hour == current_hour:
        if alarm_min == current_min:
            if alarm_sec == current_sec:
                print("ВСТАВАЙ УЕБИЩЕ")
                playsound('C:\\Users\\danii\\PycharmProjects\\Будильник\\rafael_krux-hit_n_smash.mp3')
                break
