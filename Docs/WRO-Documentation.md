# WRO Future Engineers / documentation requirements

**Basis:** international 2026 General & Game Rules, chapter 7 and appendix C; the separate Documentation Rubric; official Q&A reviewed on 3 October 2026. National events may apply their organiser's adaptations.

## Official references

- [2026 season documents](https://wro-association.org/competition/2026-season/)
- [Future Engineers General & Game Rules](https://wro-association.org/wp-content/uploads/WRO-2026-Future-Engineers-Self-Driving-Cars-General-Rules.pdf)
- [Documentation Rubric](https://wro-association.org/wp-content/uploads/WRO-2026-Future-Engineers-Documentation-Rubric.pdf)
- [Official Q&A](https://wro-association.org/competition/questions-answers/)
- [Official repository template](https://github.com/World-Robot-Olympiad-Association/wro2022-fe-template)

## Template cross-reference

The official template's folder names are an example organisation. This repository uses the team's requested presentation while exposing the corresponding material:

| Template section | Repository location |
|---|---|
| `src` | [Code](../Code/README.md) |
| `schemes` | [Electronics / Diagrams](../Electronics/README.md) |
| `v-photos` | [Mechanics / Vehicle Photos](../Mechanics/Vehicle%20Photos/README.md) |
| `t-photos` | [General Photos / Team](../General%20Photos/README.md) |
| `video` | [video / video.md](../video/video.md) |
| `models` | [Mechanics / 3D Models](../Mechanics/3D%20Models/README.md) |
| `other` | [Docs](README.md) and [archive](../archive/README.md) |

## Submission requirements and available evidence

| Requirement | Evidence / remaining action |
|---|---|
| Public GitHub repository | Existing public repository; retain public visibility after submission |
| English README of at least 5,000 characters explaining the solution and upload process | [Root README](../README.md); length checked by the repository verification tool |
| Mobility, power/sensing and obstacle-management explanation | Source-based explanations in README, Code, Electronics, Mechanics and the English journal |
| Code for every programmed component | Original SPIKE projects and readable Python/block-source exports; team must identify the program actually used at the event |
| Vehicle photographs from all six sides | [Six supplied views](../Mechanics/Vehicle%20Photos/README.md); confirm they show the post-modification competition build |
| Team photograph | Supplied event photographs; confirm/add a portrait showing all three students |
| YouTube demonstration for each challenge, public or unlisted, with at least 30 seconds of autonomous driving | Original MP4 practice clips imported; **two qualifying YouTube URLs still required** |
| Engineering journal and hardcopy at the international final | [English PDF](Engineering-Journal.pdf) and corrected Spanish source available; bring an English hardcopy with readable code/screenshots |
| CAD/manufacturing files when applicable | No such source files supplied; applicability statement in the models section |
| Reproducible electromechanical documentation | Source-derived logical diagram supplied; final physical connections, measurements, gear ratio, parts list and power-budget details require team input |

This organisation does not establish complete competition compliance by itself. Missing measurements, videos and final-program evidence are identified rather than invented.

## Commit and visibility deadlines

Chapter 7 requires:

1. A first commit no later than **two months before the competition**, containing at least **one fifth of the final code amount**.
2. A second commit no later than **one month before the competition**.
3. A third commit no later than **two weeks before the competition**. This is the main evaluation snapshot; later changes may not count towards documentation scoring.
4. Submission of the repository URL no later than **three weeks before the competition**, according to the organiser's exact date/time.
5. Public repository access from submission through at least **twelve months after the competition**.

The original repository has ten commits dated 26–30 April 2026 before this refresh. Their history is retained. The event date and submitted evaluation snapshot were not supplied, so the deadline and one-fifth-of-code conditions cannot be marked as verified. Importing old files today does not create evidence of an earlier GitHub publication. Do not backdate or manufacture commits to simulate those milestones.

## Rubric navigation

Each criterion is scored 0, 2, 4 or 6; the documentation maximum is **30 points**.

| Criterion | Evidence location |
|---|---|
| Mobility and mechanical design | [Mechanics](../Mechanics/README.md), six views and notebook entries |
| Power and sensor architecture | [Electronics](../Electronics/README.md), logical diagram and sensor history |
| Software architecture and obstacle strategy | [Code](../Code/README.md), original source listings and control-flow diagram |
| Systems thinking and engineering decisions | [Journal](Engineering-Journal.md): sensor limitations, prototype changes, event feedback and reinforcement motivations |
| Reproducibility and GitHub quality | README, original source files, inventories, meaningful history and verification tool |

The rubric evaluates evidence, engineering reasoning, testing and reproducibility. A polished layout cannot substitute for absent performance data. The journal reports the team's original decisions and observations without introducing torque, current, speed or success-rate measurements that were never supplied.

## Program/build details to reconcile with the rules

These points follow directly from the supplied source and the official rules:

- Rules 11.3–11.5 require four wheels, a connected drive arrangement and a steering actuator; the three-wheel historical prototype is not the international vehicle configuration.
- Rule 9.11 requires the prescribed waiting-state/start-button procedure and slot one for SPIKE. The recent supplied programs start propulsion on their program-start event; a separate waiting state is not shown.
- Recent #6/#7/#8 snapshots use distance sensing and yaw. They do not show complete red/right and green/left traffic-sign obedience, three-lap completion/finish logic or a full parking sequence.
- Exact vehicle size and mass, final gear arrangement and measured performance require confirmation on the selected robot.

The official Q&A additionally clarifies parking measurement near the mat, unchanged vehicle size while leaving/entering the parking area, permission to park in the opposite orientation and assessment of unequal wheel track widths. Read the linked live Q&A before the event.

[Repository home](../README.md)
