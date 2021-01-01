def on_pin_pressed_p0():
    basic.show_string("dongmuyang150@163.com")
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_gesture_tilt_left():
    for index in range(3):
        music.start_melody(music.built_in_melody(Melodies.JUMP_UP), MelodyOptions.ONCE)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_logo_long_pressed():
    radio.send_string(":-(")
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    basic.show_number(input.compass_heading())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_six_g():
    basic.show_number(randint(0, 1))
input.on_gesture(Gesture.SIX_G, on_gesture_six_g)

def on_gesture_shake():
    basic.show_number(randint(1, 12))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_logo_up():
    if input.light_level() > 60:
        basic.show_leds("""
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            """)
    else:
        basic.show_leds("""
            . # . . .
            . # # . .
            . # # . .
            . # # . .
            # # . . .
            """)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_logo_pressed():
    radio.send_string(":-)")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_pin_pressed_p2():
    basic.show_string("bye")
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    basic.show_number(input.magnetic_force(Dimension.X))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    basic.show_string("Hello!")
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_sound_loud():
    basic.show_string("dasheng")
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_gesture_tilt_right():
    for index2 in range(3):
        music.start_melody(music.built_in_melody(Melodies.BIRTHDAY), MelodyOptions.ONCE)
    basic.pause(200)
    for index3 in range(2):
        music.play_melody("D F D G F G A F ", 120)
        music.play_melody("D C5 D B F F A F ", 120)
        music.play_melody("C5 A B G A F G E ", 120)
        music.play_melody("G B A G C5 B A B ", 120)
        music.play_melody("C5 G B A F A C5 B ", 120)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

radio.set_group(123)
input.calibrate_compass()
basic.show_string("Hello!@dmy")