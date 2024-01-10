import PySimpleGUI as sg
import calendar

# Önceden kaydedilmiş görevler
saved_tasks = []
completed_tasks = []

# Takvim görüntüleme
calendar_str = calendar.month(2023, 3)

# Görev listesi penceresini oluştur
layout = [
    [sg.Text("To-Do List", font=("Helvetica", 20), justification="center")],
    [sg.InputText("", key="task"), sg.Button("Ekle", key="add_task")],
    [sg.Column([[sg.Listbox(saved_tasks, size=(40, 10), key="task_list")]], element_justification="center"),
     sg.Column([[sg.Multiline(default_text=calendar_str, size=(40, 10), key="calendar_display")]], element_justification="center")],
    [sg.Button("Tamamlandı", key="mark_done"), sg.Button("Sil", key="delete")],
]

window = sg.Window("To-Do List", layout)

# Ana döngü
while True:
    event, values = window.read()
    
    # Çıkış yap
    if event == sg.WINDOW_CLOSED:
        break
        
    # Görev ekle
    if event == "add_task":
        task = values["task"]
        if task:
            saved_tasks.append(task)
            window["task_list"].update(saved_tasks)
            window["task"].update("")
    
    # Görev tamamlandı olarak işaretle
    if event == "mark_done":
        selected_task = values["task_list"]
        if selected_task:
            for task in selected_task:
                completed_tasks.append(task)
                saved_tasks.remove(task)
            window["task_list"].update(saved_tasks)
    
    # Görevi silme
    if event == "delete":
        selected_task = values["task_list"]
        if selected_task:
            for task in selected_task:
                saved_tasks.remove(task)
            window["task_list"].update(saved_tasks)
    
window.close()
