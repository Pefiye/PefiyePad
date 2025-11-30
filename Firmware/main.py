import kmk.setup
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC as K
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# [col 1 (GP29), col 2 (GP6), col 3 (GP7), col 4 (GP0)]
keyboard.col_pins = (
    board.GP29,  # col 1
    board.GP6,   # col 2
    board.GP7,   # col 3
    board.GP0,   # col 4
)

# [row 1 (GP26), row 2 (GP27), row 3 (GP28)]
keyboard.row_pins = (
    board.GP26,  # row 1
    board.GP27,  # row 2
    board.GP28,  # row 3
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Visual Key Map:
#      C1    C2    C3    C4
# R1: [F13, F14, F15, F16]
# R2: [F17, F18, F19, F20]
# R3: [F21, F22, F23, F24]

keyboard.keymap = [
    [
        # Row 1 (Keys F13, F14, F15, F16)
        K.F13, K.F14, K.F15, K.F16,
    ],
    [
        # Row 2 (Keys F17, F18, F19, F20)
        K.F17, K.F18, K.F19, K.F20,
    ],
    [
        # Row 3 (Keys F21, F22, F23, F24)
        K.F21, K.F22, K.F23, K.F24,
    ],
]

if __name__ == '__main__':
    keyboard.go()