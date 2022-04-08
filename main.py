def on_microbit_id_button_b_evt_click():
    music.play_tone(494, music.beat(BeatFraction.BREVE))
    basic.clear_screen()
    basic.show_leds("""
        # # # . .
                # . . # .
                # # # . .
                # . . # .
                # # # . .
    """)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_B,
    EventBusValue.MICROBIT_BUTTON_EVT_CLICK,
    on_microbit_id_button_b_evt_click)

def on_microbit_id_button_a_evt_click():
    music.play_tone(440, music.beat(BeatFraction.BREVE))
    basic.clear_screen()
    basic.show_leds("""
        . . # . .
                . # . # .
                # . . . #
                # # # # #
                # . . . #
    """)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_A,
    EventBusValue.MICROBIT_BUTTON_EVT_CLICK,
    on_microbit_id_button_a_evt_click)

def on_microbit_id_button_ab_evt_click():
    for index in range(3):
        music.play_melody("C5 B A G F E D C ", 120)
        basic.show_icon(IconNames.HAPPY)
        basic.pause(500)
        basic.show_icon(IconNames.SMALL_HEART)
        basic.show_icon(IconNames.HEART)
        music.play_melody("C5 B A G - G A B ", 120)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_AB,
    EventBusValue.MICROBIT_BUTTON_EVT_CLICK,
    on_microbit_id_button_ab_evt_click)

basic.show_leds("""
    . # . # .
        # . # . #
        # . . . #
        . # . # .
        . . # . .
""")
music.play_melody("C5 B B A G F C F ", 200)