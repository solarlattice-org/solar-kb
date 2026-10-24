---
id: metric:expected-energy-ratio
type: Metric
name: Expected energy ratio
aliases:
- EER
- estimated energy ratio
category: Performance
---
The expected energy ratio compares the AC energy a site actually measured with the AC energy it was expected to produce. It is simply measured energy divided by expected energy. Expected energy is the long-term expectation based on a typical meteorological year (TMY). Users upload it as monthly values under the site's Energy Expectations tab, and every month the site is expected to operate needs a value. EER is not adjusted for weather. The weather-adjusted ratios, GEER and IEER, take EER and correct it by the ratio of measured to expected insolation. GEER uses satellite-based virtual irradiance divided by TMY3 expected insolation. IEER uses on-site insolation and user-uploaded expected insolation instead. EER is different from the performance index, which divides measured energy by modeled energy from a PV model configured for the site. In the monitoring platform, EER can be added to data extracts and graphical reports. Monthly granularity is suggested for a site performance yield report. The Salesforce connector's monthly site performance snapshot reports an average EER for each month. It sorts sites into performance groups: below 0.5, 0.5 to 0.8, 0.8 to 1.2, and above 1.2.

<!-- review notes
- sentence 3: support check: partial - The passages say GEER/IEER take EER and adjust by measured/expected insolation, but they never explicitly state that EER is not weather-adjusted (only implied).
- sentence 4: support check: partial - GEER uses VI insolation over TMY3 expected insolation and IEER uses on-site insolation with user-uploaded expected insolation, but the passage doesn't say GEER's measured insolation is 'satellite-based' as a requirement beyond VI using satellite imagery (fine) and describes GEER as an EER adjustment rather than simple division; the 'divided by' phrasing is loosely right, so only minor imprecision.
-->
