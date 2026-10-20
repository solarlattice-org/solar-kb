---
id: meas:stm-no-signal-at-ribbon
type: Measurement
name: No test signal at ribbon
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 35
    unit: unit:PERCENT
  conditions: One PV module with a single cell interconnect ribbon locally disconnected (failure stage
    1); I-V curve measured at standard test conditions
  note: The disconnected position was also located with the signal transmission device.
  quote: only this one disconnection among many interconnection results in 35% power loss
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.6
    h: 31f745f3dabf
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
---
This signature appears during a signal transmission check. The receiver picks up the test signal along healthy ribbons, but the signal disappears at the point where a cell interconnect ribbon is disconnected. To run the check, first stop the PV system. Then connect the transmitter to the target module string at the combiner box and move the receiver along the interconnect ribbons on the front or back of each module. The transmitter sends a small alternating test current into the string, and the receiver senses the magnetic flux that this current creates. Losing the signal at only one ribbon points to a local break in a single cell interconnect ribbon. If no signal can be found anywhere on a submodule, all ribbons of a cell or a string interconnect are broken, and the signal is going through the bypass diode instead. Ribbon breaks are often caused by poor soldering, ribbon kinks that were bent too hard, physical stress during transport, thermal cycling, or hot spots from partial shading. In one field module, results from the signal method matched an EL image showing ribbons disconnected on two cells. The method is cheap and can be used in the field without removing modules. Even one disconnected ribbon caused a large power loss in an STC I-V measurement. The failure can get worse until a bypass diode fails, which can lead to burn marks and broken glass.
