import random

print("Добро пожаловать в игру \"угадайка число\"")
play = True
while play:
  print("Введите правую границу")
  right_range = int(input())
  num = random.randint(1, right_range)
  cnt = 0

  def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= right_range:
      return True
    print(f"А может быть все-таки введем целое число от 1 до {right_range}?")
    return False

  while True:
    print(f"Введите число от 1 до {right_range}")
    num2 = input()
    if is_valid(num2):
      cnt+=1
      num2 = int(num2)
      if num2 == num:
        print("Вы угадали, поздравляем!\nКоличество попыток:", cnt)
        break
      elif num2 > num:
        print("Ваше число больше загаданного, попробуйте еще разок")
      else:
        print("Ваше число меньше загаданного, попробуйте еще разок")
    else:
      print("Пожалуйста, введите правильные входные данные")

  print("Хотите сыграть еще раз? (Да, Нет)")
  ans = input().lower()
  if ans == "да":
    play = True
  else: play = False

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")