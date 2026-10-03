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
flipperevents_whenDistance(COMPARATOR='<', UNIT='inches', PORT=flipperevents_distance-sensor-selector(field_flipperevents_distance-sensor-selector='C'), VALUE='20')
flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE='90')
control_wait_until(CONDITION=flipperoperator_isInBetween(VALUE=flippersensors_orientationAxis(AXIS='yaw'), LOW='86', HIGH='90'))
flippersensors_resetYaw()
procedures_call(procedure='Steering')
procedures_call(procedure='yaw')
```

### Stack 2

```text
flipperevents_whenProgramStarts()
flippersensors_resetYaw()
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), SPEED='200')
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'))
procedures_call(procedure='Steering')
control_forever()
  SUBSTACK:
    control_if(CONDITION=flippersensors_isDistance(COMPARATOR='<', UNIT='inches', PORT=flippersensors_distance-sensor-selector(field_flippersensors_distance-sensor-selector='A'), VALUE='4'))
      SUBSTACK:
        flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'), VALUE='25')
        control_wait_until(CONDITION=flippersensors_isDistance(COMPARATOR='>', UNIT='inches', PORT=flippersensors_distance-sensor-selector(field_flippersensors_distance-sensor-selector='A'), VALUE='4'))
        procedures_call(procedure='Steering')
        procedures_call(procedure='yaw')
    control_if(CONDITION=flippersensors_isDistance(COMPARATOR='<', UNIT='inches', PORT=flippersensors_distance-sensor-selector(field_flippersensors_distance-sensor-selector='E'), VALUE='4'))
      SUBSTACK:
        flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE='25')
        control_wait_until(CONDITION=flippersensors_isDistance(COMPARATOR='>', UNIT='inches', PORT=flippersensors_distance-sensor-selector(field_flippersensors_distance-sensor-selector='E'), VALUE='4'))
        procedures_call(procedure='Steering')
        procedures_call(procedure='yaw')
```

### Stack 3

```text
procedures_definition(custom_block=procedures_prototype(procedure='Steering'))
control_if(CONDITION=flipperoperator_isInBetween(VALUE=flippermotor_absolutePosition(PORT=flippermotor_single-motor-selector(field_flippermotor_single-motor-selector='F')), LOW='146', HIGH='359'))
  SUBSTACK:
    flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE=operator_subtract(NUM1='360', NUM2=flippermotor_absolutePosition(PORT=flippermotor_single-motor-selector(field_flippermotor_single-motor-selector='F'))))
control_if(CONDITION=flipperoperator_isInBetween(VALUE=flippermotor_absolutePosition(PORT=flippermotor_single-motor-selector(field_flippermotor_single-motor-selector='F')), LOW='1', HIGH='145'))
  SUBSTACK:
    flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE=operator_multiply(NUM1='-1', NUM2=flippermotor_absolutePosition(PORT=flippermotor_single-motor-selector(field_flippermotor_single-motor-selector='F'))))
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
    flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE='-15')
    procedures_call(procedure='Steering')
control_if(CONDITION=flipperoperator_isInBetween(VALUE=flippersensors_orientationAxis(AXIS='yaw'), LOW='-1', HIGH='1'))
  SUBSTACK:
    procedures_call(procedure='Steering')
    procedures_call(procedure='yaw')
```
