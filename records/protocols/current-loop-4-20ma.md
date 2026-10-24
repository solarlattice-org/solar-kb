---
id: proto:current-loop-4-20ma
type: Protocol
name: 4-20 mA current loop
aliases:
- 4-20 mA
- analog current input
- Current Loop
- 4-20 mA Output
category: Communication
protocol_kind: transport
---
The 4-20 mA current loop is an analog signal link. A measured value or setpoint is carried as a current between 4 mA and 20 mA. The Ideematec SensorBox lists a 4 to 20 mA current loop as one of its interfaces. The SMA WAGO I/O system has a 4-channel analog input terminal for 4 mA to 20 mA. It reads each signal at 12-bit resolution and keeps the input galvanically isolated from the system. On that terminal, each sensor is wired to a CAGE CLAMP input (AI 1 to AI 4) and ground. All four channels share one 0 V ground, and a red LED on a channel shows a wire break or an out-of-range value. The Beckwith M-7679 analog output module has two channels. Each one is set to 4-20 mA or 0-20 mA in IPScom S-7600, and the loop common must not be tied to chassis or earth ground. The SMA Cluster Controller can also take active power limit and reactive power setpoints as analog current signals from 0 mA to 20 mA.

<!-- review notes
- sentence 1: support check: partial - Passages show a current loop interface of 4–20 mA and a 4–20 mA input terminal, but don't explicitly say it's an analog link carrying measured values or setpoints.
- sentence 2: support check: partial - Passages list Interface: Current Loop 4–20 mA, but the device name (Ideematec SensorBox) isn't stated in the passages shown.
-->
