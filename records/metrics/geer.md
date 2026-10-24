---
id: metric:geer
type: Metric
name: GEER (virtual-irradiance expected energy ratio)
aliases:
- GEER
category: Performance
claims:
- claim_id: c1
  rel: subclass_of
  target: metric:insolation-adjusted-expected-energy-ratio
  note: 'GEER uses the same basic formula as IEER but with fixed inputs: Virtual Irradiance for measured
    insolation and TMY3 for expected insolation.'
  cite:
  - src: src:alsoenergy-kb-ieer
    loc: sec=h6
    h: 42bbee5d89bf
  - src: src:alsoenergy-kb-rescheduling-a-legacy-site-performance-yield-report-in-locusnoc
    loc: sec=front
    h: 003faad8cb7c
  review: drafted
---
GEER is a weather-adjusted expected energy ratio in the LocusNOC monitoring platform. It compares how much energy a site actually produced with how much it was expected to produce, corrected for how sunny the period really was. It starts from EER, which is measured AC energy divided by expected AC energy. GEER then adjusts EER by dividing it by the ratio of measured insolation to expected insolation. Measured insolation comes from Locus Energy Virtual Irradiance, a satellite-based estimate of global horizontal sunlight. Expected insolation comes from TMY3 global horizontal data. For GEER to show, the site needs a valid address, uploaded energy expectations and working Virtual Irradiance data. You can check in the charting tool that Virtual Irradiance is available for the site. GEER suits sites with no on-site weather station. IEER uses the same basic formula but lets the user choose the inputs, such as on-site insolation and uploaded expected insolation, which makes GEER the less flexible version. GEER shows on the Overview page as last-month and this-month values, and is also available in the charting tool, in reports and in the External API. If IEER is enabled for a site, the Overview shows IEER instead of GEER and labels which metric is displayed. For monthly reporting, add GEER as a performance ratio in a Data Extract or a Graphical Report and set the granularity to monthly.

<!-- review notes
- sentence 2: support check: partial - EER = measured/expected energy is stated, but GEER is said to adjust EER by the insolation ratio (VI/TMY3) without stating it divides EER by that ratio; the direction is unspecified.
- sentence 3: support check: partial - VI as measured and TMY3 as expected insolation are stated, and VI is satellite-based, but the passages show GEER uses VI Insolation Global Horizontal and TMY3 GHI only loosely; 'global horizontal' for VI is supported by the field name, so the detail is mostly there, though stated as a fixed pairing only partly.
-->
