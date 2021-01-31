import pynput.keyboard as keyboard
import pynput.mouse as mouse
import time as time

board = keyboard.Controller()
rat = mouse.Controller()
print(rat.position)

#steps
starting_position = (-1106, 310)
writing_position = (-749, 954)
send_position = (-410, 948)
matches_position = (-1234, 201)
message1 = "Siemka, jeżeli mi nie odpiszesz to spowodujesz lokalne zakłócenie projekcji astralnej  co w efekcie wytworzy dysonans na styku dwóch płaszczyzn rzeczywistości"
message2 = "A tego raczej byś nie chciała"

def send_message(text):
    rat.position = writing_position
    board.type(text)
    time.sleep(1)
    rat.position = send_position
    rat.click(mouse.Button.left, 1)


def bot(text1, text2):
    rat.position = starting_position
    rat.click(mouse.Button.left, 1)
    time.sleep(0.5)
    send_message(text1)
    time.sleep(0.5)
    send_message(text2)
    rat.position = matches_position
    rat.click(mouse.Button.left, 1)



for i in range(1):
    bot(message1, message2)
