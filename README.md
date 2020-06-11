# Examination paper variants generator

--EN--
This programm is presented in two variations.
One has console interface representation and second one has graphical interface wich was made with Qt5.
First of all this programm was made to help teachers at distance learning to spread randomly exam papers betwen students.
To compile a version with GUI into a single executable file, you need to do the following:
- Install _python3_
- Download and install _pip_ at **windows**, or type the comand to terminal `sudo apt-get install python3-pip` at **Linux**
- Install _pyinstaller_ with command `pip install pyinstaller`
- Run the Run the command line from the directory with the program and type the command `pyinstaller -w -F Generator.py`
  - optional attribute will be flag `-i` writing the path to the custom icon `"...\icon.ico"`
- Find exe file at _dist_ directory and use it

--RU--
Эта программа представлена в двух вариациях.
Одна из них с консольным интерфейсом, другая с графическим интерфейсом, сделанным на Qt5.
Изначально программа создавалась, чтобы помочь учителям на дистанционном обучении случайным образом распределить экзаменационные билеты между студентами.
Чтобы скомпилировать вариант с графическим интерфейсом в один исполняемый файл нужно следующее:
- Установить _python3_
- Скачать и установить _pip_ на **windows**, либо же ввести команду `sudo apt-get install python3-pip` на **Linux**
- Установить _pyinstaller_ командой `pip install pyinstaller`
- Запустить командную строку из директории с программой с графическим интерфейсом и набрать команду `pyinstaller -w -F Generator.py`
  - необязательным атрибутом будет флаг `-i` с указанием пути до кастомной иконки `"...\icon.ico"`
- Найти в папке _dist_ исполняемый файл и использовать

©ElDios
