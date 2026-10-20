---
id: symptom:fill-factor-reduction
type: Symptom
name: Reduced fill factor
aliases:
- FF
claims:
- claim_id: c1
  rel: observed_as
  target: meas:fill-factor-reduction
  note: Seen on IV traces. Corrosion lowers FF through higher series resistance along with lower Isc.
    LID lowers FF along with Isc and Voc. Cell cracking lowers FF through a modest rise in series resistance.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h7
    h: 7c7e8aa5f488
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h6
    h: 0189f40b9ccf
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.3
    h: b6c82133fe8c
  review: drafted
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 10
    unit: unit:PERCENT
  conditions: Relative module power decrease when cell cracking was induced in stress testing. The source
    pairs this loss with a series resistance increase of 0.5 Ohm cm2 and a 2% absolute drop in fill factor.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.3
    h: b6c82133fe8c
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
  review_note: 'support check: partial - The 10% relative module power loss, 0.5 Ohm cm2 and 2% absolute
    FF drop are stated, but the 10% is power loss for the module, not a loss attributed to fill factor
    itself, and it is only an approximate figure from one test.'
---
A reduced fill factor shows up when you trace a module or string IV curve. The curve gives lower power than its Isc and Voc would suggest. For reference, typical fill factors at STC are 0.75 to 0.80 for polycrystalline cells and 0.80 to 0.85 for monocrystalline cells. In severe metallization corrosion, the fill factor drops because series resistance rises, and short-circuit current also falls. The corrosion is usually visible by eye, and EL imaging can confirm it. In light induced degradation, Isc, fill factor and Voc all fall together. Check early-life flash-test and IV results against the nameplate rating. Cell cracks raise series resistance only modestly. In one stress test, a module that lost about a tenth of its power showed a fill factor drop of 2% absolute. Potential induced degradation and cell interconnection failure can also change the IV curve. Use EL, IR thermography and Voc checks to tell them apart from cracks or diode faults. Check first: look for corrosion and encapsulant damage, then use EL and thermography to find the affected cells.

<!-- review notes
- sentence 1: support check: partial - IV tracing shows FF decrease in corrosion and LID, but the passages never say the curve gives lower power than Isc and Voc suggest, and they do not specifically describe module or string traces.
- sentence 6: support check: partial - The passages give EL, thermography and Voc checks for PID and EL/IR for separating interconnection failures from cracks or diode failures, and a PID IV signature figure, but they do not state that interconnection failure changes the IV curve or that the same combination applies to both.
- sentence 7: support check: partial - Visual inspection then electrical confirmation (EL, thermography) is stated for corrosion, but encapsulant damage is not tied to EL and thermography locating affected cells, and the 'check first' framing is an extrapolation.
-->
