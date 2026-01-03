from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.rgb import RGB
from kmk.extensions.oled import OLED
from kmk.extensions.oled import OledDisplayMode
import board

keyboard = KMKKeyboard()

# -------------------------
# MATRIX CONFIG (4 ROW x 3 COL = 12 KEYS)
# -------------------------
keyboard.row_pins = (
    board.D0,
    board.D1,
    board.D2,
    board.D3,
)

keyboard.col_pins = (
    board.D4,
    board.D5,
    board.D6,
)

keyboard.diode_orientation = keyboard.DIODE_ROW2COL

# -------------------------
# RGB (16 LEDs)
# -------------------------
rgb = RGB(
    pixel_pin=board.D10,   # change if needed
    num_pixels=16,
    val_limit=100,
)

keyboard.extensions.append(rgb)

# -------------------------
# OLED (SSD1306 I2C)
# -------------------------
oled = OLED(
    sda=board.SDA,
    scl=board.SCL,
    width=128,
    height=64,
    display_mode=OledDisplayMode.TXT,
)

keyboard.extensions.append(oled)

# -------------------------
# KEYMAP (4x3)
# -------------------------
keyboard.keymap = [
    [
        KC.Q,   KC.W,   KC.E,
        KC.A,   KC.S,   KC.D,
        KC.Z,   KC.X,   KC.C,
        KC.LCTL, KC.SPACE, KC.ENTER,
    ]
]

# -------------------------
# OLED TEXT
# -------------------------
oled.text = [
    "XIAO RP2040",
    "4x3 MACROPAD",
    "",
    "12 Keys",
    "16 RGB",
]

# -------------------------
# RGB MODE
# -------------------------
rgb.enable()
rgb.mode = rgb.RAINBOW

if __name__ == "__main__":
    keyboard.go()
