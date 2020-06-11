# Examination paper variants generator

--EN--
This programm is presented in two variations.
One has console interface representation and second one has graphical interface wich was made with Qt5.
First of all this programm was made to help teachers at distance learning to spread randomly exam papers betwen students.


--RU--
Эта программа представлена в двух вариациях.
Одна из них с консольным интерфейсом, другая с графическим интерфейсом, сделанным на Qt5.
Изначально программа создавалась, чтобы помочь учителям на дистанционном обучении случайным образом распределить экзаменационные билеты между студентами.
Чтобы скомпилировать вариант с графическим интерфейсом в один исполняемый файл нужно следующее:
- Установить python3
- Скачать и установить pip на windows, либо же ввести команду _sudo apt-get install python3-pip_ на Linux
- Установить pyinstaller командой _pip install pyinstaller_
- Запустить командную строку из дирректории с программой с графическим интерфейсом и набрать команду _pyinstaller -w -F Generator.py_
  - необязательным атрибутом будет флаг `<-i>` с указанием пути до кастомной иконки _"...\icon.ico"_
- Найти в папке dist исполняемый файл

©ElDios
