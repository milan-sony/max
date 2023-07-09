from urllib.request import urlopen

connection = 0

try:
  urlopen("https://www.google.com/", timeout=1)
  connection = 1
except:
  connection = 0

if connection == 1:
  print("Connected")
else:
  print("not connected")