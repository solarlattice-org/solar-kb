---
id: metric:mtbf
type: Metric
name: Mean time between failures
aliases:
- MTBF
category: Reliability
---
Mean time between failures is the average exposure time between one failure of a component and its next failure. It is calculated by dividing the total period over which data was collected by the total number of failures recorded in that period, and it is expressed in hours. The total period is the calendar time of data collection in hours, and total failures is the count of failures during that period. MTBF is the inverse of the failure rate, and together with mean time to repair it gives inherent availability as MTBF divided by the sum of MTBF and MTTR. IEEE 493-2007 (the Gold Book) defines the term and its formula in its reliability definitions. O&M guidelines list MTBF as an equipment KPI that plant operators track, and one microinverter vendor gives 10 to 15 years as typical for traditional central or string inverters.

<!-- review notes
- sentence 4: support check: partial - The Ai = MTBF/(MTBF+MTTR) formula is stated, but the passages never say MTBF is the inverse of the failure rate (though λ=Tf/Tp and MTBF=Tp/Tf imply it).
- sentence 6: support check: partial - The passages list MTBF as an equipment KPI and tracked metric, and give 10-15 years for traditional inverters, but they don't show the figure is from a microinverter vendor or that it is typical.
-->
