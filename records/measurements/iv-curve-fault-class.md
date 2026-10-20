---
id: meas:iv-curve-fault-class
type: Measurement
name: IV curve classified as fault
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 38
    unit: unit:W
  conditions: One string whose IV curve an SVM classified as a fault, measured against a Gaussian Process
    Regression estimate of the fault-free curve in an in-situ IV tracing experiment
  note: The faulty string showed lower voltage output than both the GPR estimate and a healthy neighbouring
    string.
  quote: the string was producing about 38 W less than it should have if it were not in a fault condition
  cite:
  - src: src:iea-pvps-t13-07-2017
    loc: sec=5.3.2
    h: 5cd9bad228fd
  review: drafted
---
This signature is a binary label that a classifier puts on a measured IV curve: either normal or fault. In one setup, an in-situ tracer measured string IV curves at set times each day. A support vector machine then classified each curve using the normalized current and voltage points together with plane-of-array irradiance and module temperature. When a curve was labelled as a fault, a Gaussian Process Regression model estimated the fault-free curve for the same irradiance and temperature. The lost power was then taken as the difference between the actual and estimated curves. On previously unseen test data, this classifier found all 82 fault cases with no false positives, and it correctly marked 242 cases as normal. Other systems call a curve a fault when one of its parameters, such as the slope between Voc and the maximum power point, is too many standard deviations away from its expected value. A fault label should be checked against the conditions at the time of measurement. A signature that means a fault in full sun can be normal under cloud, so compare it with past performance under similar conditions. IV curve shape deviations behind such labels can come from damaged cells or modules, shorted bypass diodes, local shading, module mismatch, shunt paths and excessive series resistance.
