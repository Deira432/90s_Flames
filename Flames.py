#Flames

# name_1 = 'Dee'
# name_2 = 'Code'
def flames (name_1,name_2):
  key = ['f','l','a','m','e','s']
  list_name_1 = list(name_1.upper())
  list_name_2 = list(name_2.upper())
  count = 0

  for items in list_name_1:
    for letters in list_name_2:
      if items == letters :
        count += 1

  total_letter_count = (len(list_name_1) + len(list_name_2)) - count 

  for i in range(0,5):
    while total_letter_count > len(key):
      #print('WHILE LOOP')
      total_letter_count -= len(key)
      if total_letter_count < len(key):
        key.pop(total_letter_count-1)
    else:
      if len(key) == 1 :
        break
      else:
        #print('ELSE BLOCK')
        key.pop(total_letter_count-1)

  #print(key)

  if key[0] == 'f':
    print(f"\nI smell a friend bond...between {name_1} and {name_2}")
  elif key[0] == 'l':
    print(f"\nI smell a lover bond between {name_1} and {name_2}")
  elif key[0] == 'a':
    print(f"\nThere is an affection between {name_1} and {name_2}")
  elif key[0] == 'm':
    print(f"\nI smell a marriage bond between {name_1} and {name_2}")
  elif key[0] == 'e':
    print(f"\nI smell a Enemy bond between {name_1} and {name_2}")
  elif key[0] == 's':
    print(f"\nI smell a Sister bond between {name_1} and {name_2}")

  print("\nThanking for choosing our service.....\n")
  print("           *Laughs Sarcastically*       ")


input_name_1 = input("Enter the first person : ")
input_name_2 = input("Enter the second person : ")

flames(input_name_1,input_name_2)