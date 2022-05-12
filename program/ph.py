def ph_cycle(None):
  blank = None # don't think this is needed
  if ph_balance > 6.3:
      print("ph high")
      GPIO.output(3, GPIO.LOW)
      sleep(5)
      GPIO.output(3, GPIO.HIGH)
      sleep(5)
  elif ph_balance < 5.3:
      print("ph low")
      GPIO.output(4, GPIO.LOW)
      sleep(5)
      GPIO.output(4, GPIO.HIGH)
      sleep(5)
