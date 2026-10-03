import color_sensor
import distance_sensor
import motor
import runloop
import time
from hub import light_matrix, port, motion_sensor

# ─────────────────────────────────────────────
# PORTS
# ─────────────────────────────────────────────
PORT_L    = port.E
PORT_R    = port.F
PORT_COL= port.D
PORT_DIST = port.C

# ─────────────────────────────────────────────
# SPIN
# ─────────────────────────────────────────────
SPIN_SPEED = 300

# ─────────────────────────────────────────────
# WHITE REFLECTION GUARD
# ─────────────────────────────────────────────
WHITE_MIN        = 55
NUDGE_FAST_SPEED = 420
NUDGE_SLOW_SPEED = 150
NUDGE_MS        = 180

# ─────────────────────────────────────────────
# BLUE TURNS
# ─────────────────────────────────────────────
BLUE_FAST_SPEED= 500
BLUE_SLOW_SPEED= 120
BLUE_MS        = 360
BLUE_COOLDOWN_MS = 500
BLUE_REF_MIN    = 20
BLUE_REF_MAX    = 34

# ─────────────────────────────────────────────
# BLUE CORRECTION
# ─────────────────────────────────────────────
CORRECT_FASTER_SIDE = 'L'

# ─────────────────────────────────────────────
# GREEN / YELLOW / ORANGE EARLY WARNING
# ─────────────────────────────────────────────
GREEN= 6
YELLOW = 7

EARLY_FAST_SPEED = 475
EARLY_SLOW_SPEED = 145
EARLY_MS        = 325

# Safer orange reflection fallback
ORANGE_REF_MIN = 40
ORANGE_REF_MAX = 55

# ─────────────────────────────────────────────
# YAW
# ─────────────────────────────────────────────
YAW_TURN_SPEED = 230
YAW_TOLERANCE= 3

# ─────────────────────────────────────────────
# OBSTACLE
# ─────────────────────────────────────────────
OBSTACLE_MM        = 130
OBSTACLE_PREWARN_MM= 200
OBSTACLE_COOLDOWN_MS = 3000
DIST_SAMPLES        = 3

# ─────────────────────────────────────────────
# COLORS
# ─────────────────────────────────────────────
BLUE = 3

# ─────────────────────────────────────────────
# STATES
# ─────────────────────────────────────────────
STATE_SPIN= 0
STATE_NUDGE = 1
STATE_EARLY = 2
STATE_BLUE= 3
STATE_DODGE = 4

state = STATE_SPIN

# ─────────────────────────────────────────────
# FIXED ORANGE DETECTION
# ─────────────────────────────────────────────
async def detect_yellow_orange():
    color_hits = 0
    refl_hits = 0

    for _ in range(5):
        c = color_sensor.color(PORT_COL)
        r = color_sensor.reflection(PORT_COL)

        if c == GREEN or c == YELLOW:
            color_hits += 1

        if ORANGE_REF_MIN <= r <= ORANGE_REF_MAX:
            refl_hits += 1

        await runloop.sleep_ms(5)

    if color_hits >= 2:
        return True

    if refl_hits >= 3:
        return True

    return False

# ─────────────────────────────────────────────
# LEDs
# ─────────────────────────────────────────────
def led_clear():
    light_matrix.clear()

def led_startup():
    light_matrix.clear()
    for i in range(5):
        light_matrix.set_pixel(2, i, 100)
        light_matrix.set_pixel(i, 2, 100)

def led_blue():
    light_matrix.clear()
    for px in [(2, 2), (1, 2), (3, 2), (2, 1), (2, 3)]:
        light_matrix.set_pixel(px[0], px[1], 100)

def led_early():
    light_matrix.clear()
    light_matrix.set_pixel(2, 2, 50)
    light_matrix.set_pixel(1, 2, 30)
    light_matrix.set_pixel(3, 2, 30)

def led_nudge():
    light_matrix.clear()
    light_matrix.set_pixel(2, 2, 50)

def led_dodge():
    light_matrix.clear()
    for i in range(5):
        light_matrix.set_pixel(i, i, 100)

def led_spin():
    light_matrix.clear()
    for px in [(2, 0), (4, 2), (2, 4), (0, 2)]:
        light_matrix.set_pixel(px[0], px[1], 100)

def led_prewarn():
    light_matrix.clear()
    light_matrix.set_pixel(2, 0, 60)
    light_matrix.set_pixel(2, 2, 40)

# ─────────────────────────────────────────────
# GYRO
# ─────────────────────────────────────────────
def get_yaw():
    return motion_sensor.tilt_angles()[0] / 10.0

def yaw_error(current, target):
    e = target - current
    while e > 180:
        e -= 360
    while e < -180:
        e += 360
    return e

# ─────────────────────────────────────────────
# DISTANCE
# ─────────────────────────────────────────────
async def read_distance_avg():
    total = 0
    count = 0
    for _ in range(DIST_SAMPLES):
        d = distance_sensor.distance(PORT_DIST)
        if d != -1:
            total += d
            count += 1
        await runloop.sleep_ms(5)
    return (total // count) if count > 0 else -1

# ─────────────────────────────────────────────
# MOTORS
# ─────────────────────────────────────────────
def spin():
    motor.run(PORT_L, -SPIN_SPEED)
    motor.run(PORT_R, SPIN_SPEED)

def stop_all():
    motor.stop(PORT_L)
    motor.stop(PORT_R)

async def do_arc(fast_spd, slow_spd, duration_ms):
    if CORRECT_FASTER_SIDE == 'L':
        motor.run(PORT_L, -fast_spd)
        motor.run(PORT_R, slow_spd)
    else:
        motor.run(PORT_L, -slow_spd)
        motor.run(PORT_R, fast_spd)
    await runloop.sleep_ms(duration_ms)

async def do_nudge():
    global state
    state = STATE_NUDGE
    led_nudge()

    await do_arc(NUDGE_FAST_SPEED, NUDGE_SLOW_SPEED, NUDGE_MS)
    stop_all()
    await runloop.sleep_ms(25)

    state = STATE_SPIN
    led_spin()
    spin()

# ─────────────────────────────────────────────
# ACTIONS
# ─────────────────────────────────────────────
async def do_early():
    global state
    state = STATE_EARLY
    led_early()

    await do_arc(EARLY_FAST_SPEED, EARLY_SLOW_SPEED, EARLY_MS)
    stop_all()
    await runloop.sleep_ms(25)

    state = STATE_SPIN
    led_spin()
    spin()

async def do_blue():
    global state
    state = STATE_BLUE
    led_blue()

    await do_arc(BLUE_FAST_SPEED, BLUE_SLOW_SPEED, BLUE_MS)
    stop_all()
    await runloop.sleep_ms(25)

    state = STATE_SPIN
    led_spin()
    spin()

# ─────────────────────────────────────────────
# MAIN LOOP
# ─────────────────────────────────────────────
async def main():
    global state

    motion_sensor.reset_yaw(0)
    await runloop.sleep_ms(200)

    led_startup()
    await runloop.sleep_ms(600)
    led_clear()

    last_blue_time = time.ticks_ms()

    state = STATE_SPIN
    led_spin()
    spin()

    while True:
        now = time.ticks_ms()

        if state != STATE_SPIN:
            await runloop.sleep_ms(10)
            continue

        reflection = color_sensor.reflection(PORT_COL)
        c = color_sensor.color(PORT_COL)

        # BLUE FIRST so white guard doesn't steal it
        if c == BLUE and BLUE_REF_MIN <= reflection <= BLUE_REF_MAX:
            if time.ticks_diff(now, last_blue_time) > BLUE_COOLDOWN_MS:
                await do_blue()
                last_blue_time = time.ticks_ms()
            continue

        # orange / yellow / green detection
        if await detect_yellow_orange():
            await do_early()
            continue

        # white / line guard
        if reflection < WHITE_MIN:
            await do_nudge()
            continue

        await runloop.sleep_ms(20)

runloop.run(main())