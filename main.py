# -*- coding: utf-8 -*-
from tkinter import *
import json
import requests
from searcher import boolSearch
from vector_module_search import vectorSearch

def win1():
    strochka = search_input()

    window = Tk()
    window.geometry("800x400+600+100")
    window["bg"] = "red"
    window.title("VECTOR SEARCH:")
    res = vectorSearch(strochka)
    i = 0
    for row in res:
        # lbl = Label(window, text=row[0] + "  " + str(round(row[1], 5)), font=("Arial Bold", 11), bg="red",
        lbl = Label(window, text=row, font=("Arial Bold", 11), bg="red",
                    fg="black")  # bq - цвет фона текса. fq - цвет текста
        lbl.grid(column=0, row=i)
        # i = i + 1
    window.mainloop()


def win2():
    strochka = search_input()

    window = Tk()
    window.geometry("800x400+600+500")
    window["bg"] = "red"
    window.title("BOOLEAN SEARCH:")
    res = boolSearch(strochka)
    i = 0
    for row in res:
        lbl = Label(window, text=row, font=("Arial Bold", 11), bg="red",
                    fg="black")  # bq - цвет фона текса. fq - цвет текста
        lbl.grid(column=0, row=i)
        i = i + 1
    window.mainloop()


def search_input():
    # search = input()
    search = txt.get()

    search_set = set(search.strip().split(" "))
    tesaurus_search_set = set()

    for word in search_set:
        tesaurus_search_set.add(word.lower())

    for word in search_set:
        tesaurus_text = requests.get('http://www.serelex.org/find/ru-patternsim-ruwac-wiki/' + word).text
        if tesaurus_text.find('relations') != -1:
            json_buffer = json.loads(tesaurus_text)
            value_buff = 0.0
            for json_word in json_buffer['relations']:
                value_buff += json_word['value']
            value = value_buff / len(json_buffer['relations'])
            for json_word in json_buffer['relations']:
                if value <= json_word['value']:
                    tesaurus_search_set.add(json_word['word'].lower())
    return list(tesaurus_search_set)


if __name__ == '__main__':
    window = Tk()
    window.geometry("500x300+100+100")
    window["bg"] = "red"
    window.title("Ну что будем искать?")
    lbl = Label(window, text="Введите запрос: ", font=("Arial Bold", 15), bg="red",
                fg="black")  # bq - цвет фона текса. fq - цвет текста
    lbl.grid(column=0, row=0)
    txt = Entry(window, width=60)
    txt.grid(column=0, row=1)
    btn = Button(window, text="Векторный метод", bg="grey", fg="white", command=win1)
    btn.grid(column=0, row=2)
    btn = Button(window, text="Булевый метод", bg="grey", fg="white", command=win2)
    btn.grid(column=0, row=3)
    window.mainloop()

    # strochka = search_input()
    # print("Input please your request:")
    # print("VECTOR SEARCH:")
    # vectorSearch(strochka)
    # print("\nBOOLEAN SEARCH:")
    # boolSearch(strochka)
