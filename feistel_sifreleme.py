import PySimpleGUI as sg
import feistel
import time




sg.theme("DarkTeal2")

layout = [
    [sg.T("")],
    [sg.Text("Choose a file: "),
     sg.Input(key="-IN-"),
     sg.FileBrowse()],
    [sg.Text("Password key: "),sg.Input(key="-KEY-")],
    [sg.Text("Outfile Name: "),sg.Input(key="-OUTFILE-")],
    [sg.Radio("ECB", "crypt-type", key='ecb', enable_events=True),
     sg.Radio("CBC", "crypt-type", key='cbc', enable_events=True)],
    [sg.Button("Encrypte"), sg.Button("Decrypte")],
    [sg.Text("Result: ", key="-OUT-")]


]


window = sg.Window('My File Browser', layout, resizable=True, finalize=True)

filename = ""
opt = {"e_or_d": "", "mode": "", "filename": "", "key": "", "outfilename": ""}
retrunValue = ""
while True:
    event, values = window.read()
    opt["filename"] = values['-IN-']
    opt["key"] = values['-KEY-']
    opt["outfilename"] = values['-OUTFILE-']
    if values["ecb"]:
        opt["mode"] = "ecb"
    if values["cbc"]:
        opt["mode"] = "cbc"
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    elif event == "Encrypte":
        opt["e_or_d"] = "-e"
        start_time = time.time()
        retrunValue = feistel.main(opt)
        retrunValue = retrunValue + "\n" + str(time.time() - start_time)
        print(time.time() - start_time)
    elif event == "Decrypte":
        opt["e_or_d"] = "-d"
        start_time = time.time()
        retrunValue = feistel.main(opt)
        retrunValue = retrunValue + "\n" + str(time.time() - start_time)
        print(time.time() - start_time)

    # print("returnvalue",retrunValue)
    window['-OUT-'].update(value=retrunValue)
    # input()

window.close()
