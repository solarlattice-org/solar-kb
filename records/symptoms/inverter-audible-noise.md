---
id: symptom:inverter-audible-noise
type: Symptom
name: Inverter audible noise
aliases:
- humming
- whistling
- buzzing contactor
- rattling noise
- clicking noise
- pulsating noise
- buzzing noise
- loud humming noise
- noise emission
claims:
- claim_id: c1
  rel: observed_as
  target: meas:fan-abnormal-noise
  note: Rattling or snarling noise that continues with backup mode disabled can come from a cable touching
    the internal fan; the source says the inverter must then be replaced.
  cite:
  - src: src:sma-kb-noises-of-the-backup-relais-with-sunny-tripower-smart-energy
    loc: sec=h1
    h: dd39c63b2d2f
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:contactor-buzzing
  note: Buzzing from the backup contactor after the backup function is activated, loud enough to be heard
    elsewhere in the house.
  cite:
  - src: src:sma-kb-noises-of-the-backup-relais-with-sunny-tripower-smart-energy
    loc: sec=h1
    h: dd39c63b2d2f
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:grid-impedance-pulse-noise
  note: Clicking or cyclic pulsing noise while the inverter measures grid impedance. This is normal behaviour,
    and the volume depends on the power fed in and on hardware such as chokes.
  cite:
  - src: src:sma-kb-noise-emission-of-sma-inverters
    loc: sec=h1
    h: ba0e0c7ab062
  review: drafted
  review_note: 'support check: partial - Clicking and cyclic pulsing during grid impedance measurement,
    with volume depending on power fed in and hardware like chokes, are stated, but only clicking is called
    normal; the pulse is described as audible, not explicitly normal.'
- claim_id: c4
  rel: observed_as
  target: meas:power-correlated-noise-level
  note: 'Fan and audible level rise and fall with power throughput and internal temperature: louder at
    midday, quieter in the morning, evening or on cold days. This is normal unless an error is shown.'
  cite:
  - src: src:doe-femp-om-small-pv
    loc: sec=h3
    h: 82129b1df69b
  review: drafted
---
Some noise from an operating inverter is normal, because turning DC into AC always makes some sound, and datasheets give a typical noise level for each model. Fan noise goes up and down with power and internal heat, so the inverter is louder at midday and quieter in the morning or in cold weather. If the status lights are green and no error is shown, this is normal. Clicking or pulsing sounds during grid impedance measurement are also normal. Mounting the inverter on a solid wall rather than plasterboard or wood keeps the volume down. Buzzing from the backup contactor after backup is switched on can sometimes be cleared by switching the AC fuse off and on again so the contactor re-seats. If the customer does not use backup, you can turn the function off instead. Rattling or snarling that continues with backup turned off may be a cable touching the internal fan, and the source says the inverter must then be replaced. Buzzing from the power stage has been fixed by firmware updates on some models, so check the inverter's firmware version and the release notes. Noise heard on radio receivers is radio frequency interference, which is a separate issue. Measure the noise at different distances from the inverter and its cables to find the source.

<!-- review notes
- sentence 2: support check: partial - The seminar supports the variation with power and heat and normal with no errors, but mentions lights being on and green only as a general indication, and does not say status lights green applies to every inverter; mostly supported though fan 'cold weather' is stated.
- sentence 6: support check: partial - The release notes say a buzzing noise from the power stage set was fixed in a bugfix, but nothing about checking firmware version, some models, or the advice to check release notes.
- sentence 7: support check: partial - Distance testing at the inverter and cables is stated, but the passages don't say radio noise is a separate issue from audible inverter noise, and note interference alone doesn't confirm the inverter as source.
-->
