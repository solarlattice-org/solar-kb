---
id: metric:degradation-rate
type: Metric
name: Degradation rate
aliases:
- annual degradation
- Rd
- module degradation rate
- total degradation rate
category: Performance
---
Degradation rate measures how fast a PV module's power falls away from its initial maximum output power over time. It is usually treated as a linear rate and reported as percent power loss per year (%/yr or %/a), for single modules or for a whole PV system. Monitoring platforms apply it by multiplying estimated energy by one minus the rate times the number of whole years since a configured degradation start date. Climate-based models estimate the rate from module temperature, temperature cycling, UV dose and relative humidity, and can combine separate rates for hydrolysis, photodegradation and thermomechanical wear into one total rate. Long-term module rates of about 0.3% to 1% per year are typical, and banks often assume a flat 0.5% per year for crystalline modules when no module-specific test data exists; the rate is usually higher in the first year of light exposure before it settles. Published annual rates also depend on technology, for example 0.40 %/year for CdTe, 0.87 for amorphous silicon, 0.96 for CIGS and 1.00 for concentrator modules. A system can degrade faster than its modules because modules that age at different rates create mismatch, so some engineers add about 0.1% per year as a modeling allowance; field data should be used to check this. IEC TS 61724-4 covers the evaluation method for PV system degradation rate.
