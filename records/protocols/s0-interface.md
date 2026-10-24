---
id: proto:s0-interface
type: Protocol
name: S0 pulse interface
aliases:
- S0
- S0 meter interface
- pulse output
- S0 interface
- S0 counter
- S0 meter
category: Communication
protocol_kind: transport
---
The S0 interface is a simple electrical pulse link. An energy meter sends a set number of pulses for each kWh, and the receiving device counts them. On the SMA device described in these units, you set the meter input type to S0 in the drop-down list. You then type the meter's pulse rate into the S0 pulses/kWh field, using the value from the energy meter manual. A Fronius Symo inverter can take an S0 counter wired straight to the inverter to record self-consumption. The counter can sit at the feed-in point or in the consumption branch. With a Fronius S0 meter fitted, you can set dynamic power reduction in the DSO Editor menu on the Fronius Datamanager website. The inverter may need a firmware update before it accepts an S0 meter. Fronius lists the S0 meter requirements as: compliance with IEC 62053-31 Class B, at most 15 V DC, between 2 mA and 15 mA when ON, and no more than 0.15 mA when OFF. The Fronius wiring diagram marks the S0 terminals as S0 + and S0 -. If the SMA energy balance diagrams show unrealistic feed-in or purchase values, check that the S0 meter outputs values netted across the line conductors. If it does not, contact the meter manufacturer.

<!-- review notes
- sentence 1: support check: partial - Passages mention S0 meters with a pulses/kWh rate and IEC 62053-31 requirements, but never describe S0 as a simple electrical pulse link or say the receiver counts pulses.
- sentence 4: support check: partial - Passages state dynamic power reduction under DSO Editor and possible firmware update, but do not say it is a 'Fronius S0 meter' or that the reduction is tied to having one fitted; mostly supported though.
- sentence 6: support check: partial - The diagram text lists S0 + and S0 - labels, but the passage does not explicitly say they mark the terminals in a wiring diagram.
- sentence 1: review: partial - The S0 pulses/kWh field implies a set pulse rate per kWh, but the passages never call S0 a simple electrical pulse link or say the receiving device counts the pulses.
-->
