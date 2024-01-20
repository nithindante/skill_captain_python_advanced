import threading


def roll():
    print("Rolling")

def eat():
  print("eating")

def jump():
  print("jumping")

#Creating threads

roll_thread = threading.Thread(target=roll)
eat_thread = threading.Thread(target=eat)
jump_thread = threading.Thread(target=jump)

#starting the threads

roll_thread.start()
eat_thread.start()
jump_thread.start()

#waiting for the thread to finish

roll_thread.join()
eat_thread.join()
jump_thread.join()

#Both threads are finished

print("done with hobbies")