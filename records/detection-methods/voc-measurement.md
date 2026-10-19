---
id: method:voc-measurement
type: DetectionMethod
name: Open-circuit voltage measurement
aliases:
- Voc
- V oc
- open circuit voltage test
- direct Voc measurement
claims:
- claim_id: c1
  rel: produces
  target: meas:low-voc
  note: A string Voc well below the expected value can point to modules with reversed polarity, shorted
    bypass diodes, poor insulation, damage, or water in conduits or junction boxes (u1). A short-circuited
    bypass diode gives a module Voc lower than expected (u10).
  cite:
  - src: src:iec-62446-1
    loc: sec=6.4
    h: c2c39f38b7e7
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h7
    h: 0a38406de906
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-19
- claim_id: c2
  rel: produces
  target: meas:high-voc
  note: A string Voc above the expected value usually comes from a wiring error, such as the wrong number
    of modules in series.
  cite:
  - src: src:iec-62446-1
    loc: sec=6.4
    h: c2c39f38b7e7
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
Open-circuit voltage measurement checks the voltage of each PV string while no current flows. It confirms that strings are wired correctly and that the expected number of modules are connected in series. Measure each string with suitable equipment before any switches are closed or string overcurrent protective devices are installed. Compare each reading with the value expected from the datasheet or a PV model that accounts for the module type, module count and cell temperature. You can also scale up from a single measured module, or compare identical strings, using a reference string if irradiance is unstable. A low reading can mean reversed module polarity, shorted bypass diodes, poor insulation, damage, or water in conduits or junction boxes. A high reading usually means a wiring error. The check helps detect short-circuited bypass diodes in Bypass Diode Failure, short circuits in Junction Box Failure, and voltage loss from Potential Induced Degradation (PID). Its limits: it is less accurate than electroluminescence for PID, and an open-circuit bypass diode is hard to detect unless the module is strongly mismatched. An IV curve trace can give Voc in place of a separate test. Any test device must be rated for the circuit's voltage and current.

<!-- review notes
- sentence 1: support check: partial - Per-string measurement and checking wiring and series module count are stated, but 'while no current flows' is not explicitly stated (only implied by open circuit).
- sentence 5: support check: partial - Short-circuited diodes (u10), junction box short circuits (u4) and PID detection via Voc (u20) are supported, though PID 'voltage loss' is only loosely stated and Voc for PID is called less accurate.
-->
