---
id: mit:fuse-replacement
type: Mitigation
name: DC fuse replacement
aliases:
- String fuse replacement
- Replacing DC Branch Fuse
---
DC fuse replacement means taking out a blown or damaged fuse on the DC input side of an inverter or DC combiner and putting in a new one. Sungrow string inverters list it as one check for PV abnormal alarms (codes 078-081, 220-227, 548-563 and 580-595), after you confirm the string is connected, the module is not shaded and the wiring is not loose. On Sungrow central and MV inverters, a DC fuse fault alarm means you check whether the fuse has blown, and if it has, Sungrow carries out the replacement. Only a qualified person should do this work. First switch the DC and AC disconnects and the AC branch breaker off, confirm there is no voltage, check with a DC clamp meter that no current flows through the fuse, and cover the array with dark opaque sheets. Pull the old fuse out with a fuse extractor, holding only the plastic tab and never touching the metal end caps or clips. Fit a new fuse with the same specifications as the old one. Base the fuse rating on string sizing: at least 1000 VDC, and generally 1.56 times the module Isc. The CPS wire box holders accept 15A, 20A, 25A or 30A fuses. For an arc fault, also check for loose fuses or terminals with poor contact, then tighten them or replace any burnt parts. If the alarm continues after the fuse is replaced and the other causes have been ruled out, contact the manufacturer's service team.

<!-- review notes
- sentence 1: support check: partial - Passages cover installing/replacing fuses in a DC combiner and replacing damaged/blown DC fuses, but no definition stating it is on the DC input side of an inverter or combiner explicitly; broadly consistent yet definitional.
- sentence 2: support check: partial - Fuse check appears in the PV abnormal codes listed, but the preconditions differ: for 548-595 the order puts shading and loose wiring checks before fuse, and 'module not shaded' isn't a precondition for codes 078-081/220-227; also fuse check isn't gated on all three.
- sentence 3: support check: partial - Central/MV rows say check if fuse is blown and contact Sungrow to replace, but the u28 row only refers to other measures, and the 'central and MV' scope is only implied.
-->
