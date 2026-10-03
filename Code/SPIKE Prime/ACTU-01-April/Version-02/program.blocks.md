# Original SPIKE block listing

Automatically extracted from the accompanying `.llsp3` project.
Blocks retain their original opcodes, values, units and procedure names.
Indentation shows nested control stacks; each event is a separate stack.
This is a review representation, not an executable program or a Python translation.

## 0gtGZsDe6VvlxEpFSUrY

### Stack 1

```text
flipperevents_whenProgramStarts()
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'), SPEED='50')
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), SPEED='50')
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'))
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'))
flipperlight_lightDisplayImageOn(MATRIX=flipperlight_matrix-5x5-brightness-image(field_flipperlight_matrix-5x5-brightness-image='0000000009000909090009000'))
flipperlight_lightDisplaySetBrightness(BRIGHTNESS='100')
```

### Stack 2

```text
flipperevents_whenColor(PORT=flipperevents_color-sensor-selector(field_flipperevents_color-sensor-selector='D'), OPTION=flipperevents_color-selector(field_flipperevents_color-selector='9'))
flippermotor_motorStop(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'))
flippermotor_motorStop(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'))
flipperlight_lightDisplayImageOn(MATRIX=flipperlight_matrix-5x5-brightness-image(field_flipperlight_matrix-5x5-brightness-image='0000000000999990000000000'))
control_wait(DURATION='1')
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'))
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'), SPEED='35')
control_wait(DURATION='0.5')
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'), SPEED='35')
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), SPEED='35')
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'))
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'))
```

### Stack 3

```text
flipperevents_whenColor(PORT=flipperevents_color-sensor-selector(field_flipperevents_color-sensor-selector='D'), OPTION=flipperevents_color-selector(field_flipperevents_color-selector='6'))
flippermotor_motorStop(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'))
flippermotor_motorStop(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'))
flipperlight_lightDisplayImageOn(MATRIX=flipperlight_matrix-5x5-brightness-image(field_flipperlight_matrix-5x5-brightness-image='0090000900999990090000900'))
control_wait(DURATION='1')
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'))
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'), SPEED='35')
control_wait(DURATION='0.5')
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'), SPEED='35')
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), SPEED='35')
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'))
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'))
```

### Stack 4

```text
flipperevents_whenDistance(COMPARATOR='<', UNIT='%', PORT=flipperevents_distance-sensor-selector(field_flipperevents_distance-sensor-selector='D'), VALUE='4')
flippermotor_motorStop(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'))
flippermotor_motorStop(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'))
flipperlight_lightDisplayImageOn(MATRIX=flipperlight_matrix-5x5-brightness-image(field_flipperlight_matrix-5x5-brightness-image='0999099009909099009909990'))
control_wait(DURATION='1')
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'))
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'), SPEED='35')
control_wait(DURATION='0.5')
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'), SPEED='35')
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), SPEED='35')
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='E'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'))
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'))
```

### Original comments

Detector

Detector

Detector
