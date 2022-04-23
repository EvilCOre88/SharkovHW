strin = 'Система'
car_speed = 140
is_town = True
is_camera = False
town_speed = 60
country_speed = 90
over_speed = 0
fine_for_20_to_40 = 500
fine_for_40_to_60 = 1000
fine_for_60_to_80 = 2000
fine_over_80 = 5000
if is_town == True:
  over_speed = car_speed - town_speed
else:
  over_speed = car_speed - country_speed
if over_speed < 20:
  print ("Вы не превысили скорость или превысили незначительно")
elif over_speed >= 20 and over_speed < 40:
  print ("Вы превысили скорость на " + str(over_speed) + " км/час")
  print ("Ваш штраф составит " + str(fine_for_20_to_40) + " рублей")
elif over_speed >= 40 and over_speed < 60: 
  print ("Вы превысили скорость на " + str(over_speed) + " км/час")
  print ("Ваш штраф составит " + str(fine_for_40_to_60) + " рублей")
elif over_speed >= 60 and over_speed < 80 and is_camera == True:
  print ("Вы превысили скорость на " + str(over_speed) + " км/час")
  print ("Ваш штраф составит " + str(fine_for_60_to_80) + " рублей")
  print ("Вы лишились водительских прав")
elif over_speed >= 80 and is_camera == True:
  print ("Вы превысили скорость на " + str(over_speed) + " км/час")
  print ("Ваш штраф составит " + str(fine_over_80) + " рублей")
  print ("Вы лишились водительских прав")
elif over_speed >= 60 and over_speed < 80:
  print ("Вы превысили скорость на " + str(over_speed) + " км/час")
  print ("Ваш штраф составит " + str(fine_for_60_to_80) + " рублей")
elif over_speed >= 80:
  print ("Вы превысили скорость на " + str(over_speed) + " км/час")
  print ("Ваш штраф составит " + str(fine_over_80) + " рублей")

  # проеврка ГИТА