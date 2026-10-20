---
id: method:independent-test-validation
type: DetectionMethod
name: Independent test data validation
aliases:
- independent lab measurements
- independent testing
claims:
- claim_id: c1
  rel: produces
  target: meas:module-parameter-deviation
  note: Independent test data or lab measurements show material differences from the PAN file parameters
    used in the energy model; the forecast should then be updated.
  cite:
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=front
    h: ab4eee130cc0
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h2
    h: 10747fe38d64
  - src: src:pv-root-cause-flawed-pan-file-losses
    loc: sec=h6
    h: d98419e6bd80
  review: drafted
---
Independent test data validation checks the module parameters in an energy model file, such as a PAN file, against test data that does not come from the module maker. First find the exact PAN file used for the energy estimate, including its source, its version and any manual edits. Run sensitivity cases to see whether PAN parameters can plausibly explain a lasting gap between expected and measured output. This is the main check for flawed PAN file yield losses. A PAN problem is a modeling loss, not a fault in the field. Keep it apart from real operating losses so nobody tries to repair a defect that does not exist. Independent third-party testing of module samples at the factory gate or when they arrive on site is an optional way to get independent data. Treat the source of the PAN file as a controlled input, and update forecasts if independent testing shows material differences in the parameters.

<!-- review notes
- sentence 1: support check: partial - Passages mention validating parameters against independent test data and independent lab measurements, but don't explicitly define it as data not from the module maker.
- sentence 3: support check: partial - Sensitivity cases to see if PAN parameters explain the production gap are stated, but not that it is the 'main check', and 'lasting' gap is only loosely supported by 'persistent'.
-->
