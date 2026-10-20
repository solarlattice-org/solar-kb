---
id: meas:low-vmp-voc-ratio
type: Measurement
name: Reduced Vmp/Voc ratio
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 10
    unit: unit:PERCENT
  conditions: Approximate relative module power decrease when cell cracking was induced in a stress test
    of 60-cell multicrystalline modules; series resistance rose only modestly in this case
  note: In the same source, the rise in series resistance accounts for only a small share of this loss;
    most of the loss comes from a lower Impp/Isc ratio.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.3
    h: b6c82133fe8c
  review: drafted
---
A reduced Vmp/Voc ratio means the maximum power point voltage drops relative to open-circuit voltage, which points to higher series resistance. On a light IV curve, higher series resistance shows as a flatter slope between the maximum power point and Voc. Series resistance is best measured by combining light and dark IV curves, or by tracing light IV curves at two light intensities. In cell cracking stress tests, the Impp/Isc ratio drops the most, while the Vmp/Voc ratio drops less but falls further as cell damage grows. Likely causes include damaged or undersized PV wiring, poor module or array interconnections, and high-resistance faults in cell interconnects or the junction box from degradation, corrosion or manufacturing error. Moisture entering through delamination can also raise series resistance and lower performance. Long cable runs add their own resistance and affect the curve shape, so either account for them in the model or repeat the test closer to the array. Module series resistance is a lumped value, so mismatch between cells can also raise it, and an IR scan can help find high-resistance faults.
