# Code / SPIKE Prime

Original control software for ERA, grouped by the team's four update periods.

| Update | Contents |
|---|---|
| [ACTU 01 · April](SPIKE%20Prime/ACTU-01-April/README.md) | Two initial Word Blocks versions |
| [ACTU 02 · May](SPIKE%20Prime/ACTU-02-May/README.md) | Three projects, including clockwise and parking-named experiments |
| [ACTU 03 · August](SPIKE%20Prime/ACTU-03-August/README.md) | One Python prototype and three Word Blocks projects |
| [ACTU 04 · September](SPIKE%20Prime/ACTU-04-September/README.md) | Eight numbered versions and three additional variants inside Version 03 |

There are **20 supplied `.llsp3` projects**. The original filenames and locations are recorded in [the import manifest](../Docs/import-manifest.json). The project metadata is recorded in [the version inventory](../Docs/software-versions.json). Folder months are source labels, not inferred commit dates.

## Recent snapshots: #6, #7 and #8

All three are presented together at the team's request. Open the original project to upload it, or read the text export and screenshot to review it:

| Snapshot | Editable project | Readable blocks | Screenshot |
|---|---|---|---|
| #6 | [program.llsp3](SPIKE%20Prime/ACTU-04-September/Version-06/program.llsp3) | [Source listing](SPIKE%20Prime/ACTU-04-September/Version-06/program.blocks.md) | [View](SPIKE%20Prime/ACTU-04-September/Version-06/code-01.png) |
| #7 | [program.llsp3](SPIKE%20Prime/ACTU-04-September/Version-07/program.llsp3) | [Source listing](SPIKE%20Prime/ACTU-04-September/Version-07/program.blocks.md) | [View](SPIKE%20Prime/ACTU-04-September/Version-07/code-01.png) |
| #8 | [program.llsp3](SPIKE%20Prime/ACTU-04-September/Version-08/program.llsp3) | [Source listing](SPIKE%20Prime/ACTU-04-September/Version-08/program.blocks.md) | [View](SPIKE%20Prime/ACTU-04-September/Version-08/code-01.png) |

### What the source implements

These snapshots use a main program-start stack, a C-distance event and three named procedures. They reference motor D for propulsion, motor F for steering, distance sensors A/C/E and the hub's yaw sensor.

| Element | Original behaviour |
|---|---|
| Program-start stack | Initializes the version's variables/yaw, starts D and calls `Steering`; then enters a continuous main loop |
| Main loop | Checks A and E and makes short steering reactions when the distance threshold is crossed |
| C-distance event | Initiates the supplied corner-turn sequence at a reading below 20 inches |
| `Steering` | Centres F using absolute-position intervals 146–359° and 1–145° |
| `yaw` | Uses heading feedback to issue a correction to F; implementation differs between versions |
| `PAOA` | Defined alternative routine using A below 1 inch and a positive yaw window; not called by the main/C-event stacks in these snapshots |

Distance thresholds are explicitly in **inches** in the block source. Four inches equals 101.6 mm; six inches equals 152.4 mm; seven inches equals 177.8 mm; twenty inches equals 508 mm. These conversions explain the source values and are not new calibrated thresholds.

### Version comparison

- **#6:** D's original speed block stores `200`. A/E reactions use 4-inch thresholds and 25° steering-motor commands. The C event turns F counterclockwise for 90°, waits for yaw between −90° and −86°, resets yaw and recentres steering. The speed value is preserved as supplied; it is not a measured vehicle speed or a claim that the application accepts 200%.
- **#7:** D is set to `100`, F to `90`. `Count = 0` represents straight-driving work; `Count = 1` marks a turn in progress. A/E use a 6-inch trigger and a 7-inch clearance threshold. The main loop calls `yaw` and waits 0.02 seconds. The original source comment describes coordination to prevent the stacks from interfering with each other.
- **#8:** `AJJHHJ` becomes a heading target. The corner event updates it as `((target - 90 + 180) mod 360) - 180`. Heading error is `((yaw - target + 180) mod 360) - 180`. D is stopped while `Steering` centres F, then restarted. The supplied wait condition checks signed error `< 0.5`; it is not an absolute-error check. The original comment asks for track testing, because gyro and braking affect physical precision.

The three sources do not show a completed automatic direction-selection routine, colour-specific red/green pillar obedience, a three-lap counter with autonomous finish, or a complete parallel-parking sequence. The journal describes those development goals and experiments. A project named for parking is evidence of an experiment, not proof that every recent snapshot performs parking.

## Historical Python project

[ACTU 03 / Version 01](SPIKE%20Prime/ACTU-03-August/Version-01/WRO-Revamp-2026.llsp3) contains genuine Python source:

- [Original extracted Python](SPIKE%20Prime/ACTU-03-August/Version-01/WRO-Revamp-2026.py)
- [Project metadata](SPIKE%20Prime/ACTU-03-August/Version-01/WRO-Revamp-2026.metadata.json)

It imports SPIKE modules such as `color_sensor`, `distance_sensor`, `motor`, `runloop` and `hub`. Those modules run on the hub, not in desktop CPython. Its historical port assignments are E/F for the two motor channels, D for colour and C for distance. Those assignments must not be used to wire the recent D-propulsion/F-steering programs.

The Python prototype includes colour/reflection guards, timed motor arcs, yaw helpers and distance averaging. Some obstacle-related constants and helpers are defined but not invoked by `main()`. The presence of those definitions alone does not demonstrate an active obstacle routine. It is preserved as a historical prototype.

## Opening and uploading

1. Install the [official SPIKE app](https://education.lego.com/en-us/downloads/spike-app/software/).
2. Open a chosen original `.llsp3` file.
3. Compare all port assignments and mechanical motor directions with the selected vehicle.
4. Use USB to download to the hub. For an international event, verify the actual **slot one** requirement and the waiting-state/start-button procedure in rule 9.11.
5. Test during permitted practice time and record the chosen version. Exact tested app/firmware versions and final run evidence are not included in the supplied files.

## Export format

| File | Purpose |
|---|---|
| `.llsp3` | Original LEGO project; authoritative editable source |
| `.blocks.json` | Full original Scratch-style project graph extracted from the container |
| `.blocks.md` | Review listing preserving event stacks, nesting, opcodes, units and procedure names |
| `.py` | Python extracted only when the original container actually stores Python |
| `.metadata.json` | Original format, project name, creation/save timestamps and slot index |
| `code-*.png` | Supplied program screenshots |

Regenerate an export with Python 3, without third-party packages:

```powershell
python tools/export_spike.py "Code/SPIKE Prime/ACTU-04-September/Version-08/program.llsp3"
```

This tool exports source for inspection; it does not alter the control program.

[Repository home](../README.md)
