firstnumber = [x for x in input().strip().split(' ')]
if firstnumber[1] == '+':
  print(int(firstnumber[0]) + int(firstnumber[2]))
elif firstnumber[1] == '-':
  print(int(firstnumber[0]) - int(firstnumber[2]))
elif firstnumber[1] == '*':
  print(int(firstnumber[0]) * int(firstnumber[2]))
elif firstnumber[1] == '/':
  print(int(firstnumber[0]) / int(firstnumber[2]))
