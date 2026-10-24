---
id: symptom:radio-frequency-interference
type: Symptom
name: Radio frequency interference
aliases:
- RFI
- EMC interference
- broadband noise on radio bands
- electromagnetic emissions
- EMC-related issues
- radio interference
- Electromagnetic Interference
- EMI
claims:
- claim_id: c1
  rel: observed_as
  target: meas:power-correlated-noise-level
  note: Radio noise that appears when the inverter starts, changes with output power and stops when PV
    production stops points to the PV system. Noise that stays while the inverter is off points to another
    source.
  cite:
  - src: src:kb-solis-44002862909-radio-frequency-interference-rfi-in-solar-pv-installations
    loc: sec=h3
    h: f913937ec32b
  - src: src:kb-solis-44002862909-radio-frequency-interference-rfi-in-solar-pv-installations
    loc: sec=h12
    h: cd4b6af4f76a
  - src: src:kb-solis-44002862909-radio-frequency-interference-rfi-in-solar-pv-installations
    loc: sec=h4
    h: 73d6fb1b1427
  review: drafted
  review_note: 'support check: partial - Passages say noise changes with PV start/stop, output power and
    disappears when production stops, but don''t state it follows AC power or vanishes at zero output
    as a measured quantity, nor the ''noise stays while inverter off points elsewhere'' conclusion explicitly
    (only listed as an observation).'
- claim_id: c2
  rel: observed_as
  target: meas:rf-spectrum-broadband-noise
  note: Wideband SDR or spectrum analyzer captures taken before and after inverter startup show which
    frequencies are affected and what the noise pattern looks like (broadband, periodic pulses, tones).
  cite:
  - src: src:kb-solis-44002862909-radio-frequency-interference-rfi-in-solar-pv-installations
    loc: sec=h3
    h: f913937ec32b
  - src: src:kb-solis-44002862909-radio-frequency-interference-rfi-in-solar-pv-installations
    loc: sec=h11
    h: f086a443d9c4
  - src: src:kb-solis-44002862909-radio-frequency-interference-rfi-in-solar-pv-installations
    loc: sec=h4
    h: 73d6fb1b1427
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c3
  rel: observed_as
  target: meas:rf-noise-distance-gradient
  note: Noise is measured at several distances from the inverter, AC cabling, DC cabling and communication
    cables. A large change in signal strength helps locate the emission source.
  cite:
  - src: src:kb-solis-44002862909-radio-frequency-interference-rfi-in-solar-pv-installations
    loc: sec=h13
    h: a780eb01bd2f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
Radio users, often amateur radio operators, report broadband noise on one or more bands, audible noise on receivers, or poorer reception. The noise may show up on several antennas. Interference alone does not prove the inverter is the source. Cabling, grounding, antenna systems, connectors or other electronics nearby can also cause it. First check which bands are affected and whether the noise happens by day, at night or both. Also check whether it follows inverter operation or PV production. If the noise starts at inverter power-up, changes with output power and stops when production stops, the PV system is likely involved. If it stays while the inverter is inactive, look for another source. Take wideband SDR or spectrum analyzer captures before and after inverter startup to see the affected frequencies and the noise pattern. Measure the noise at different distances from the inverter, the AC and DC cabling and the communication cables to find the emitter. Moving the antenna for a short time shows whether local coupling is the cause. Typical fixes are ferrite cores on AC, DC and communication cables, mains EMC filters, moving the antenna and putting more distance between the device and the receiver. If these give no measurable improvement, investigate further. Look at the whole system, including antennas, cable routing, grounding, connectors and communication wiring, rather than one component.

<!-- review notes
- sentence 1: support check: partial - Symptoms are listed and amateur radio operators are mentioned, but 'often' amateur operators isn't stated (passage says amateur or other radio users).
- sentence 4: support check: partial - The observation list is given, but the interpretation (PV system likely involved vs. look for another source) is not explicitly stated.
- sentence 7: support check: partial - Ferrites, mains filters, repositioning antenna and increasing distance appear, but ferrites/filters were customer-tried tests, not stated as recommended fixes, and 'investigate further' is supported only loosely.
- sentence 1: review: partial - The symptoms and the multiple antennas are stated, but the passage says 'amateur radio operators or other radio users', not that the reports are often from amateur operators.
- sentence 4: review: partial - The passage lists the time-correlation observations, but does not state the conclusions (PV system likely involved, or look for another source).
-->
