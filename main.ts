control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_B, EventBusValue.MICROBIT_BUTTON_EVT_CLICK, function () {
    music.playTone(494, music.beat(BeatFraction.Breve))
    basic.clearScreen()
    basic.showLeds(`
        # # # . .
        # . . # .
        # # # . .
        # . . # .
        # # # . .
        `)
})
control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_A, EventBusValue.MICROBIT_BUTTON_EVT_CLICK, function () {
    music.playTone(440, music.beat(BeatFraction.Breve))
    basic.clearScreen()
    basic.showLeds(`
        . . # . .
        . # . # .
        # . . . #
        # # # # #
        # . . . #
        `)
})
control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_AB, EventBusValue.MICROBIT_BUTTON_EVT_CLICK, function () {
    for (let index = 0; index < 3; index++) {
        music.playMelody("C5 B A G F E D C ", 120)
        basic.showIcon(IconNames.Happy)
        basic.pause(500)
        basic.showIcon(IconNames.SmallHeart)
        basic.pause(500)
        basic.showIcon(IconNames.Heart)
        music.playMelody("C5 B A G - G A B ", 120)
    }
})
basic.showLeds(`
    . # . # .
    # . # . #
    # . . . #
    . # . # .
    . . # . .
    `)
music.playMelody("C5 B B A G F C F ", 200)
