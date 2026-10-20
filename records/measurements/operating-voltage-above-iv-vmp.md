---
id: meas:operating-voltage-above-iv-vmp
type: Measurement
name: Operating voltage above Vmp
signals:
- point: model_103.DCV
  unit: unit:V
  pattern: stays at or near the inverter minimum DC voltage and above the IV-derived Vmp
- point: model_103.DCW
  unit: unit:W
  pattern: below the IV-derived Pmp during the same intervals
- point: model_160.DCV
  unit: unit:V
  pattern: above the expected Vmp at the module temperature
- point: model_303.TmpBOM
  unit: unit:DEG_C
  pattern: high module temperature that lowers Vmp
- point: model_160.DCW
  unit: unit:W
  pattern: MPPT input power below the IV-derived Pmp at the same timestamps
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average energy loss from inverter voltage flooring in summer 2025 at a 100 MW PV plant in
    California
  note: Field poster from Leeward Renewable Energy and OTT HydroMet. Voltage or setting changes were estimated
    to recover a large share of this loss.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
---
In this signature, the inverter's measured DC operating voltage sits above the array maximum power point voltage (Vmp) taken from an IV curve, and the operating power is below the Pmp from the IV curve. It points to inverter voltage floor losses: array Vmp has dropped below the inverter's minimum DC input voltage, so the inverter has to run above the true maximum power point. The inverter stays online and irradiance can look normal, but some of the available DC power is not harvested. Look for it during hot periods, because module voltage drops as cell temperature rises. Degraded modules, a tight string design margin or reactive power operation can also push Vmp under the floor. Check AC voltage and reactive power dispatch at the same timestamps, along with DC voltage limits, module temperature and SCADA operating points. Before blaming voltage flooring, rule out outages, curtailment, clipping, soiling and sensor faults. In production data alone, this loss can look like clipping or general underperformance.
