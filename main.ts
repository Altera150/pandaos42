input.onGesture(Gesture.TiltLeft, function () {
    xuanszhuan()
})
input.onGesture(Gesture.EightG, function () {
    xuanszhuan()
})
function xuanszhuan () {
    basic.showNumber(input.rotation(Rotation.Roll))
}
input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    radio.sendString(":(")
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.compassHeading())
})
input.onGesture(Gesture.SixG, function () {
    basic.showNumber(randint(0, 1))
})
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(randint(1, 12))
})
input.onGesture(Gesture.LogoUp, function () {
    if (input.lightLevel() > 5) {
        basic.showLeds(`
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            `)
    } else {
        basic.showLeds(`
            . # . . .
            . # # . .
            . # # . .
            . # # . .
            # # . . .
            `)
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    radio.sendString(":/")
})
input.onPinPressed(TouchPin.P2, function () {
    radio.sendString("bye")
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(input.magneticForce(Dimension.X))
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onGesture(Gesture.FreeFall, function () {
    xuanszhuan()
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(input.temperature())
})
input.onPinPressed(TouchPin.P1, function () {
    radio.sendString("Hello")
})
input.onSound(DetectedSound.Loud, function () {
    basic.showString("dasheng")
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    radio.sendString(":)")
})
input.onGesture(Gesture.TiltRight, function () {
    music.startMelody(music.builtInMelody(Melodies.Blues), MelodyOptions.Once)
    music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Once)
})
let music2 = 0
radio.setGroup(123)
input.calibrateCompass()
basic.showString("Hello!@dmy")
basic.forever(function () {
    music2 = randint(0, 2)
})
