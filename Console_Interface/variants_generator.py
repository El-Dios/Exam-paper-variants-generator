import random
from colorama import init, Fore, Back, Style
from os import system


def generate_unique_variants(students_count, exam_papers_count):
  """
  Случайным образом генерирует и выводит на экран
  номера билетов для каждого студента
  """
  # check if exam papers number more than students amount
  if exam_papers_count < students_count:
    for val in range(students_count):
      print(f'{val+1:2}й студент - вариант № {random.randrange(exam_papers_count)+1}')
    
    return None

  # define list of exam papers numbers
  number_list = []

  # fulfill list by numbers
  for i in range(1, exam_papers_count+1):
    number_list.append(i)

  # randomly shuffle fulfilled list
  random.shuffle(number_list)
  
  # formatting print exam papers number in order of students number
  for val in range(students_count):
    print(f'{val+1:2}й студент - вариант № {number_list[val]}')
  
  return None


init()

flag = True

# console interface in while cycle
while(flag):
  system('cls')
  print(Back.GREEN, Style.BRIGHT, Fore.WHITE + "Здравствуйте! Добро пожаловать в генератор билетов!")

  # Input values for function
  print(Back.CYAN)
  count_stud = int(input('Введите количество студентов: '))
  count_exam_papers = int(input('Введите количество билетов: '))
  
  # Execute function
  print(Back.RESET, Fore.GREEN)
  generate_unique_variants(count_stud, count_exam_papers)
  decision = input("\nПовторить?[Да/Нет]")
  if (decision.lower() != 'да'):
    flag = False

