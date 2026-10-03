# Original SPIKE block listing

Automatically extracted from the accompanying `.llsp3` project.
Blocks retain their original opcodes, values, units and procedure names.
Indentation shows nested control stacks; each event is a separate stack.
This is a review representation, not an executable program or a Python translation.

## rEP3XnmTDvlnJeH4ni63

### Variables

```text
Count = '1'
AJJHHJ = '-1'
```

### Stack 1

```text
procedures_definition(custom_block=procedures_prototype(procedure='PAOA'))
control_wait_until(CONDITION=flippersensors_isDistance(COMPARATOR='<', UNIT='inches', PORT=flippersensors_distance-sensor-selector(field_flippersensors_distance-sensor-selector='A'), VALUE='1'))
flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE='90')
control_wait_until(CONDITION=flipperoperator_isInBetween(VALUE=flippersensors_orientationAxis(AXIS='yaw'), LOW='86', HIGH='90'))
flippersensors_resetYaw()
procedures_call(procedure='Steering')
procedures_call(procedure='yaw')
```

### Stack 2

```text
flipperevents_whenDistance(COMPARATOR='<', UNIT='inches', PORT=flipperevents_distance-sensor-selector(field_flipperevents_distance-sensor-selector='C'), VALUE='20')
control_if(CONDITION=operator_equals(OPERAND1=variable('Count'), OPERAND2='0'))
  SUBSTACK:
    data_setvariableto(VARIABLE='Count', VALUE='1')
    procedures_call(procedure='Steering')
    flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'), VALUE='90')
    control_wait_until(CONDITION=flipperoperator_isInBetween(VALUE=flippersensors_orientationAxis(AXIS='yaw'), LOW='-90', HIGH='-86'))
    flippersensors_resetYaw()
    procedures_call(procedure='Steering')
    procedures_call(procedure='yaw')
    data_setvariableto(VARIABLE='Count', VALUE='0')
```

### Stack 3

```text
flipperevents_whenProgramStarts()
data_setvariableto(VARIABLE='Count', VALUE='0')
flippersensors_resetYaw()
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), SPEED='100')
flippermotor_motorSetSpeed(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), SPEED='90')
flippermotor_motorStartDirection(PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='D'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'))
procedures_call(procedure='Steering')
control_forever()
  SUBSTACK:
    control_if(CONDITION=operator_and(OPERAND1=operator_equals(OPERAND1=variable('Count'), OPERAND2='0'), OPERAND2=flippersensors_isDistance(COMPARATOR='<', UNIT='inches', PORT=flippersensors_distance-sensor-selector(field_flippersensors_distance-sensor-selector='A'), VALUE='6')))
      SUBSTACK:
        flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE='25')
        control_wait_until(CONDITION=operator_or(OPERAND1=flippersensors_isDistance(COMPARATOR='>', UNIT='inches', PORT=flippersensors_distance-sensor-selector(field_flippersensors_distance-sensor-selector='A'), VALUE='7'), OPERAND2=operator_gt(OPERAND1=variable('Count'), OPERAND2='0')))
        control_if(CONDITION=operator_equals(OPERAND1=variable('Count'), OPERAND2='0'))
          SUBSTACK:
            procedures_call(procedure='Steering')
            procedures_call(procedure='yaw')
    control_if(CONDITION=operator_and(OPERAND1=operator_equals(OPERAND1=variable('Count'), OPERAND2='0'), OPERAND2=flippersensors_isDistance(COMPARATOR='<', UNIT='inches', PORT=flippersensors_distance-sensor-selector(field_flippersensors_distance-sensor-selector='E'), VALUE='6')))
      SUBSTACK:
        flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'), VALUE='25')
        control_wait_until(CONDITION=operator_or(OPERAND1=flippersensors_isDistance(COMPARATOR='>', UNIT='inches', PORT=flippersensors_distance-sensor-selector(field_flippersensors_distance-sensor-selector='E'), VALUE='7'), OPERAND2=operator_gt(OPERAND1=variable('Count'), OPERAND2='0')))
        control_if(CONDITION=operator_equals(OPERAND1=variable('Count'), OPERAND2='0'))
          SUBSTACK:
            procedures_call(procedure='Steering')
            procedures_call(procedure='yaw')
    procedures_call(procedure='yaw')
    control_wait(DURATION='0.02')
```

### Stack 4

```text
procedures_definition(custom_block=procedures_prototype(procedure='Steering'))
control_if(CONDITION=flipperoperator_isInBetween(VALUE=flippermotor_absolutePosition(PORT=flippermotor_single-motor-selector(field_flippermotor_single-motor-selector='F')), LOW='146', HIGH='359'))
  SUBSTACK:
    flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE=operator_subtract(NUM1='360', NUM2=flippermotor_absolutePosition(PORT=flippermotor_single-motor-selector(field_flippermotor_single-motor-selector='F'))))
control_if(CONDITION=flipperoperator_isInBetween(VALUE=flippermotor_absolutePosition(PORT=flippermotor_single-motor-selector(field_flippermotor_single-motor-selector='F')), LOW='1', HIGH='145'))
  SUBSTACK:
    flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE=operator_multiply(NUM1='-1', NUM2=flippermotor_absolutePosition(PORT=flippermotor_single-motor-selector(field_flippermotor_single-motor-selector='F'))))
```

### Stack 5

```text
procedures_definition(custom_block=procedures_prototype(procedure='yaw'))
control_if(CONDITION=operator_equals(OPERAND1=variable('Count'), OPERAND2='0'))
  SUBSTACK:
    data_setvariableto(VARIABLE='AJJHHJ', VALUE='0')
    control_if(CONDITION=operator_lt(OPERAND1=flippersensors_orientationAxis(AXIS='yaw'), OPERAND2='-2'))
      SUBSTACK:
        data_setvariableto(VARIABLE='AJJHHJ', VALUE='15')
    control_if(CONDITION=operator_gt(OPERAND1=flippersensors_orientationAxis(AXIS='yaw'), OPERAND2='2'))
      SUBSTACK:
        data_setvariableto(VARIABLE='AJJHHJ', VALUE='-15')
    data_setvariableto(VARIABLE='AJJHHJ', VALUE=operator_subtract(NUM1=operator_mod(NUM1=operator_add(NUM1=operator_subtract(NUM1=variable('AJJHHJ'), NUM2=flippermotor_absolutePosition(PORT=flippermotor_single-motor-selector(field_flippermotor_single-motor-selector='F'))), NUM2='180'), NUM2='360'), NUM2='180'))
    control_if(CONDITION=operator_gt(OPERAND1=variable('AJJHHJ'), OPERAND2='1'))
      SUBSTACK:
        flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='clockwise'), VALUE=variable('AJJHHJ'))
    control_if(CONDITION=operator_lt(OPERAND1=variable('AJJHHJ'), OPERAND2='-1'))
      SUBSTACK:
        flippermotor_motorTurnForDirection(UNIT='degrees', PORT=flippermotor_multiple-port-selector(field_flippermotor_multiple-port-selector='F'), DIRECTION=flippermotor_custom-icon-direction(field_flippermotor_custom-icon-direction='counterclockwise'), VALUE=operator_multiply(NUM1='-1', NUM2=variable('AJJHHJ')))
```

### Original comments

AJUSTE MINIMO de la referencia original de 99 bloques. D sigue CCW; D=100 es el mismo maximo que SPIKE aplicaba al 200 original. F=90 agiliza la direccion. Se conservan C<20 pulgadas, el giro CCW de 90 grados, ventana yaw -90..-86 y Steering original. yaw sin recursion, correccion ±15 absoluta en recta; A izquierda aleja a derecha y E derecha aleja a izquierda. Margen lateral 6/7 pulgadas. Count ya existente: 0 recta, 1 giro, evita que se pisen. AJJHHJ ya existente: calculo temporal de F. SIN deteccion de sentido ni control nuevo de vueltas.
