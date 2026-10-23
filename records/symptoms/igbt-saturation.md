---
id: symptom:igbt-saturation
type: Symptom
name: Power switch saturation
aliases:
- IGBT Sat
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: FIMER/ABB inverters show error code E007 with the message 'IGBT Sat' when one of the inverter's
    active devices is in saturation.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r5
    h: 3b5ad120cf21
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:inverter-fault-indicator
  note: The E007 IGBT Sat alarm is shown with the yellow LED on the inverter.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=46.r5
    h: 3b5ad120cf21
  review: drafted
---
On FIMER/ABB string inverters, power switch saturation is reported as error E007 'IGBT Sat' and the yellow LED lights. The alarm means that one of the inverter's active switching devices (the IGBTs) went into saturation. After the error appears, the inverter tries to go back to normal operation by itself. If the code shows up only now and then, the likely cause is a sudden change in grid voltage or input voltage, and the inverter itself is not faulty. If the code keeps coming back, suspect an internal fault in the inverter and contact the manufacturer's customer assistance.
