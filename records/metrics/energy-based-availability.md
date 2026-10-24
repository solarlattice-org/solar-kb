---
id: metric:energy-based-availability
type: Metric
name: Energy-based availability
aliases:
- energy availability
category: Performance
claims:
- claim_id: c1
  rel: subclass_of
  target: metric:availability
  note: Described as an energy-weighted form of the time-based availability metric, because PV availability
    during darkness matters little.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h87
    h: ad241558dc90
  - src: src:trn-oandm-nrel-best-practices-for-om-of-photovoltaic-and-ess
    loc: sec=6.1.1
    h: 581ffc57a0ee
  review: drafted
- claim_id: c2
  rel: part_of
  target: std:iec-61724-3
  note: IEC 61724-3 defines energy availability and gives the method for determining it.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h87
    h: ad241558dc90
  - src: src:trn-oandm-nrel-best-practices-for-om-of-photovoltaic-and-ess
    loc: sec=6.1.1
    h: 581ffc57a0ee
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h31
    h: b42fec7c7f7c
  review: drafted
  review_note: 'support check: partial - Passages say IEC 61724-3 defines energy availability and provides
    a method to determine it, but the method itself isn''t given in the passages.'
---
Energy-based availability measures how much of a PV plant's energy throughput capability was actually available. It weights each hour by its energy, so an hour of high irradiance counts for more than an hour of low irradiance. Formula in words: divide the expected energy for the periods when the system was operating by the total expected energy for the whole period. The system counts as operating when its inverters are peak-power tracking and feeding energy into the grid. If only some inverters or strings are working, the operating expected energy is calculated for those inverters or strings only. To calculate it you need weather data as well as a record of when the inverters were operating. It can be reported as a percentage or as a fraction, either for the whole system or for individual blocks. IEC 61724-3 defines the metric and gives two alternative ways to calculate it. IECRE suggests also reporting it with external causes identified and events outside management control excluded. O&M contracts usually use energy-based availability in the availability guarantee, and the exclusion factors defined for contractual availability tend to apply to it as well. At component level, time-based availability may be more practical. Plant reports should include both time-based and energy-based availability.

<!-- review notes
- sentence 6: support check: partial - Passages say energy-based availability is generally used in the availability guarantee and exclusion factors tend to apply, but 'usually' is only 'generally' and fine; core is stated, though 'usually' vs 'generally' is close enough, so only minor qualifier differences.
-->
