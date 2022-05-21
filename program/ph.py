def ph_cycle(None):
  blank = None # don't think this is needed
  if ph_balance > 7:
      print("ph high")
      GPIO.output(BASE, GPIO.LOW)
      sleep(5)
      GPIO.output(BASE, GPIO.HIGH)
      sleep(600)
  elif ph_balance < 5:
      print("ph low")
      GPIO.output(ACID, GPIO.LOW)
      sleep(5)
      GPIO.output(ACID, GPIO.HIGH)
      sleep(600)
