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
flipperevents_whenProgramStarts()
flippersensors_resetYaw()
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), SPEED='65')
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'))
flipperlight_lightDisplayImageOn(MATRIX=flipperlight_matrix-5x5-brightness-image(field_flipperlight_matrix-5x5-brightness-image='9909999099000009000909990'))
procedures_call(procedure='Steering')
control_forever()
  SUBSTACK:
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
```

### Stack 2

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

### Stack 3

```text
flipperevents_whenDistance(COMPARATOR='<', UNIT='inches', PORT=flipperevents_distance-sensor-selector(field_flipperevents_distance-sensor-selector='C'), VALUE='22')
flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE='90')
control_wait_until(CONDITION=flipperoperator_isInBetween(VALUE=flippersensors_orientationAxis(AXIS='yaw'), LOW='85', HIGH='99'))
flippersensors_resetYaw()
procedures_call(procedure='Steering')
```

### Stack 4

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

### Stack 5

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
