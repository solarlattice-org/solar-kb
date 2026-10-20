---
id: method:polarity-measurement
type: DetectionMethod
name: String polarity measurement
aliases:
- Polarity check
- Polarity test
claims:
- claim_id: c1
  rel: produces
  target: meas:negative-polarity-reading
  note: With the meter's positive lead on the string's positive cable and negative lead on its negative
    cable, the meter's minus indicator shows the string is wired in reverse.
  quote: All digital meters have a negative ("-") indicator that indicates when a voltage is negative;
    in this case a string connected in reverse polarity.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: sec=5.4.1.1.1
    h: c4548edebd52
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c2
  rel: produces
  target: meas:low-voc
  note: A string open-circuit voltage well below the expected value can mean one or more modules in the
    string are connected with the wrong polarity. Shorted bypass diodes or insulation faults can cause
    the same reading.
  cite:
  - src: src:iec-62446-1
    loc: sec=6.4
    h: c2c39f38b7e7
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
A string polarity measurement uses a multimeter or voltmeter to confirm that the positive and negative conductors of each PV string are wired the right way round. Connect the meter's positive lead to the string's positive cable and its negative lead to the negative cable. A negative reading on the display means the string is connected in reverse polarity. Measure each string on its own, before it is connected to other strings or the inverter. Do the check before any other tests and before switches are closed or string fuses are inserted. When a CPS inverter reports a PVxReverse fault, turn the DC switch off and open the fuse holders to isolate the strings. Then use the meter to find the reversed string and correct its wiring. An open-circuit voltage well below the expected value can also point to modules wired with the wrong polarity inside a string. The inverter does not protect against a reversed string. It is very dangerous: under strong sunlight it can blow a fuse and start a fire. If you find a reversed string on a system that was already connected, check its modules and bypass diodes for damage. Record the result for each string on the test report sheet.

<!-- review notes
- sentence 6: support check: partial - Passage says reversed string is not protected by inverter, hazardous, blows fuse at high irradiation, and could result in fire, but 'strong sunlight' and fire are conditional (fuse may fail to operate), roughly matching though simplified.
- sentence 8: support check: partial - The report sheet has a polarity check row per string, implying recording, but no passage explicitly instructs recording results per string.
-->
