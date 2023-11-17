from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QListWidget, QLineEdit
import json

app = QApplication([])
windows = QWidget()

countries = {
    'Казахстан': 'Крутой мега такой',
    'Россия': 'ОмегаКрутой',
    'Франция': 'Багет',
}

with open ('countries.json', 'w', encoding='utf=8') as file:
    json.dump(countries, file)

main_layout = QHBoxLayout()
rof_left = QVBoxLayout()
rof_right = QVBoxLayout()
list_countries = QListWidget()
name_Countries = QLineEdit()
text_Countries = QTextEdit()

add_count_button = QPushButton('Добавить страну')
del_count_button = QPushButton('Удалить страну')
edit_count_button = QPushButton('Изменить страну')
line_Countries = QHBoxLayout()
line_Countries.addWidget(add_count_button)
line_Countries.addWidget(del_count_button)
line_Countries.addWidget(edit_count_button)
rof_left.addWidget(list_countries)
rof_right.addWidget(name_Countries)
rof_right.addWidget(text_Countries)
rof_right.addLayout(line_Countries)




main_layout.addLayout(rof_left, 2)
main_layout.addLayout(rof_right, 8)
windows.setLayout(main_layout)
windows.setStyleSheet("background-color: blue; color: blue")
text_Countries.setStyleSheet("background-color: white")
list_countries.setStyleSheet("background-color: white")
name_Countries.setStyleSheet("background-color: white")
add_count_button.setStyleSheet("background-color: white")
del_count_button.setStyleSheet("background-color: white")
edit_count_button.setStyleSheet("background-color: white")

with open ('countries.json', 'r',  encoding='utf=8') as file:
    countries = json.load(file)
    for country in countries:
        list_countries.addItem(country)


def add_country():
    country = name_Countries.text()
    print(country)
    with open ('countries.json', 'r',  encoding='utf=8') as file:    
       countries = json.load(file)

    countries[country] = ''
    with open ('countries.json', 'w', encoding='utf=8') as file:
        json.dump(countries, file)
    list_countries.clear()

    for country in countries:
        print(type(country))
        list_countries.addItem(country) 

def del_country():
    country = list_countries.selectedItems()[0].text()
    if country:
        with open ('countries.json', 'r',  encoding='utf=8') as file:    
            countries = json.load(file)
        del countries[country]
        with open ('countries.json', 'w', encoding='utf=8') as file:
            json.dump(countries, file)
        list_countries.clear()
        with open ('countries.json', 'r',  encoding='utf=8') as file:    
            countries=json.load(file)
            for country in countries:
                list_countries.addItem(country)
def edit_country():
    country = list_countries.selectedItems()[0].text()
    if country:
        with open ('countries.json', 'r', encoding='utf=8') as file:
            countries = json.load(file)
        text = text_Countries.toPlainText()
        countries[country] = text
        with open ('countries.json', 'w', encoding='utf=8') as file:
            json.dump(countries, file)


def info_country():
    country = list_countries.selectedItems()[0].text()
    with open('countries.json', 'r', encoding='utf=8') as file:
        countries = json.load(file)
    text_Countries.setText(countries[country])


add_count_button.clicked.connect(add_country)
del_count_button.clicked.connect(del_country)
edit_count_button.clicked.connect(edit_country)
list_countries.itemClicked.connect(info_country)        

windows.show()
app.exec_()
