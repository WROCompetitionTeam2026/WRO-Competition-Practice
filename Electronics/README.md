# Electronics / power and sensing

## Recent software connections

![Hub connections](Diagrams/hub-connections.svg)

The diagram is based on the original September #6, #7 and #8 block sources. It represents the logical connections that these programs address, rather than a measured electrical circuit.

| Connection | Function referenced in the recent programs |
|---|---|
| A | Distance sensor; lateral-clearance checks |
| C | Distance sensor; event below 20 inches for a corner turn |
| D | Propulsion motor |
| E | Distance sensor; lateral-clearance checks |
| F | Steering motor and absolute-position feedback |
| Internal hub IMU | Yaw measurement |

The original #7 comment identifies A as the left-side sensor and E as the right-side sensor. Confirm that orientation on the selected physical build. The position and orientation of C are not independently established by the exported source. Port B is not referenced by these three snapshots.

## Power

The supplied photographs show a SPIKE hub and wired LEGO peripherals. The hub battery supplies the hub and its connected components. A measured power budget, current draw, runtime and battery-condition log were not provided, so this documentation does not assign numerical electrical specifications to the assembled vehicle.

The notebook records sensor replacements in August and reinforcement intended to reduce connection vibration on 1 October. These are the team's reported reliability changes. See [the journal](../Docs/Engineering-Journal.md) for the original sequence of events.

## Historical colour-sensor work

The April/May journal describes colour-sensor calibration, sensor repositioning and problems caused by a scratched sensor. The August Python prototype uses D for the colour sensor and C for distance, with motors on E/F. This is a different historical layout; see [the code guide](../Code/README.md).

Colour sensing is not read by the recent #6/#7/#8 programs. An electronic diagram for those snapshots should therefore not imply that their distance-reading branches classify red and green traffic signs.

## Assembly reference

Use the [top and bottom vehicle views](../Mechanics/Vehicle%20Photos/README.md) and [mechanism detail photographs](../Mechanics/README.md) to inspect cable routing. Before reproducing a selected build, record its sensor heights/angles, hub firmware, battery specification, measured current draw and final port assignments.

[Repository home](../README.md)
