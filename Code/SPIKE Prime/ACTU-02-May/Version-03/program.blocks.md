# Original SPIKE block listing

Automatically extracted from the accompanying `.llsp3` project.
Blocks retain their original opcodes, values, units and procedure names.
Indentation shows nested control stacks; each event is a separate stack.
This is a review representation, not an executable program or a Python translation.

## rEP3XnmTDvlnJeH4ni63

### Variables

```text
Count = 0
```

### Stack 1

```text
procedures_call(procedure='Steering')
control_wait(DURATION='2')
```

### Stack 2

```text
procedures_call(procedure='Steering')
```

### Stack 3

```text
procedures_definition(custom_block=procedures_prototype(procedure='Steering But more stupid'))
```

### Stack 4

```text
procedures_definition(custom_block=procedures_prototype(procedure='Steering'))
flippermotor_motorStop(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'))
control_if(CONDITION=flipperoperator_isInBetween(VALUE=flippermotor_absolutePosition(PORT=flippermotor_single-motor-selector(field_flippermotor_single-motor-selector='F')), LOW='146', HIGH='359'))
  SUBSTACK:
    flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE=operator_subtract(NUM1='360', NUM2=flippermotor_absolutePosition(PORT=flippermotor_single-motor-selector(field_flippermotor_single-motor-selector='F'))))
control_if(CONDITION=flipperoperator_isInBetween(VALUE=flippermotor_absolutePosition(PORT=flippermotor_single-motor-selector(field_flippermotor_single-motor-selector='F')), LOW='1', HIGH='145'))
  SUBSTACK:
    flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE=operator_multiply(NUM1='-1', NUM2=flippermotor_absolutePosition(PORT=flippermotor_single-motor-selector(field_flippermotor_single-motor-selector='F'))))
```

### Stack 5

```text
flipperevents_whenProgramStarts()
flippersensors_resetYaw()
procedures_call(procedure='Steering')
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), SPEED='65')
flippermotor_motorTurnForDirection(UNIT='seconds', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'), VALUE='0.5')
control_wait(DURATION='0.5')
flippermotor_motorTurnForDirection(UNIT='seconds', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'), VALUE='0.3')
flippermotor_motorTurnForDirection(UNIT='seconds', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'), VALUE='1.5')
control_wait(DURATION='1')
flippersensors_resetYaw()
flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE='60')
control_wait(DURATION='0.6')
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'))
flipperlight_lightDisplayImageOn(MATRIX=flipperlight_matrix-5x5-brightness-image(field_flipperlight_matrix-5x5-brightness-image='9909999099000009000909990'))
control_forever()
  SUBSTACK:
    control_if(CONDITION=flippersensors_isDistance(COMPARATOR='<', UNIT='inches', PORT=flippersensors_distance-sensor-selector(field_flippersensors_distance-sensor-selector='C'), VALUE='2'))
      SUBSTACK:
        flippermotor_motorStop(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'))
        control_wait(DURATION='1')
        flippermotor_motorTurnForDirection(UNIT='seconds', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE='0.3')
        control_wait(DURATION='1')
        flippermotor_motorTurnForDirection(UNIT='seconds', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'), VALUE='0.3')
        control_wait(DURATION='2')
        flippermotor_motorTurnForDirection(UNIT='seconds', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE='2')
        control_wait(DURATION='1')
        flippermotor_motorStop(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'))
        flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE='60')
        control_wait(DURATION='1')
        flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'))
    control_if(CONDITION=flippersensors_isDistance(COMPARATOR='<', UNIT='inches', PORT=flippersensors_distance-sensor-selector(field_flippersensors_distance-sensor-selector='A'), VALUE='6'))
      SUBSTACK:
        flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'), VALUE='25')
        control_wait_until(CONDITION=flippersensors_isDistance(COMPARATOR='>', UNIT='inches', PORT=flippersensors_distance-sensor-selector(field_flippersensors_distance-sensor-selector='A'), VALUE='6'))
        procedures_call(procedure='Steering')
    control_if(CONDITION=flippersensors_isDistance(COMPARATOR='<', UNIT='inches', PORT=flippersensors_distance-sensor-selector(field_flippersensors_distance-sensor-selector='E'), VALUE='6'))
      SUBSTACK:
        flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE='25')
        control_wait_until(CONDITION=flippersensors_isDistance(COMPARATOR='>', UNIT='inches', PORT=flippersensors_distance-sensor-selector(field_flippersensors_distance-sensor-selector='E'), VALUE='6'))
        procedures_call(procedure='Steering')
        procedures_call(procedure='yaw')
    control_if(CONDITION=flippersensors_isColor(PORT=flippersensors_color-sensor-selector(field_flippersensors_color-sensor-selector='B'), VALUE=flippersensors_color-selector(field_flippersensors_color-selector='9')))
      SUBSTACK:
        flippermotor_motorStop(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'))
        control_wait(DURATION='1')
        flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'), VALUE='75')
        flippermotor_motorTurnForDirection(UNIT='seconds', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE='1')
        control_wait(DURATION='1')
        procedures_call(procedure='Steering')
        flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'))
```

### Stack 6

```text
flipperevents_whenProgramStarts()
control_forever()
  SUBSTACK:
    flipperlight_centerButtonLight(COLOR=flipperlight_color-selector-vertical(field_flipperlight_color-selector-vertical='9'))
    control_wait(DURATION='2')
    flipperlight_centerButtonLight(COLOR=flipperlight_color-selector-vertical(field_flipperlight_color-selector-vertical='5'))
    control_wait(DURATION='2')
    flipperlight_centerButtonLight(COLOR=flipperlight_color-selector-vertical(field_flipperlight_color-selector-vertical='3'))
    control_wait(DURATION='2')
```

### Stack 7

```text
procedures_definition(custom_block=procedures_prototype(procedure='yaw'))
control_if(CONDITION=operator_lt(OPERAND1=flippersensors_orientationAxis(AXIS='yaw'), OPERAND2='1'))
  SUBSTACK:
    flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'), VALUE='-15')
    procedures_call(procedure='Steering')
control_if(CONDITION=operator_gt(OPERAND1=flippersensors_orientationAxis(AXIS='yaw'), OPERAND2='1'))
  SUBSTACK:
    flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE='15')
    procedures_call(procedure='Steering')
control_if(CONDITION=flipperoperator_isInBetween(VALUE=flippersensors_orientationAxis(AXIS='yaw'), LOW='-1', HIGH='1'))
  SUBSTACK:
    procedures_call(procedure='Steering')
```
