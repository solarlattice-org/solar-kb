---
id: metric:capacity-test-ratio
type: Metric
name: Capacity test ratio
aliases:
- measured-to-expected capacity
- ASTM E2848 capacity ratio
- reported capacity ratio
category: Performance
claims:
- claim_id: c1
  rel: part_of
  target: std:astm-e2939
  note: ASTM E2939 sets out how to find the expected capacity and the reporting conditions. That expected
    capacity is meant to be compared with the capacity measured under Test Method E2848. The edition cited
    is E2939-13, approved September 2013.
  cite:
  - src: src:std-standards-standards-testing-performance-testing-astm-e2939
    loc: sec=1
    h: 972a451a50ba
  - src: src:std-standards-standards-testing-performance-testing-astm-e2939
    loc: sec=5
    h: 5517c31c2dbe
  - src: src:std-standards-standards-testing-performance-testing-astm-e2939
    loc: sec=2.2
    h: 5fc2a05466b9
  review: drafted
---
The capacity test checks how much power the system can generate. It can be run with the ASTM regression method or with the PKs method. To get measured capacity, output power is fitted by multiple linear regression against plane-of-array irradiance, ambient air temperature and wind speed. The data come from a short collection period, typically 3 to 30 days. The reporting conditions are then put into the regression equation, which gives a capacity in watts. Expected capacity is found the same way, but using simulated power from a performance model of the system. That model is driven by meteorological data covering at least 5 contiguous days. The comparison only means something if both capacities use the same reporting conditions and the simulation period matches the data collection period. The comparison between expected and measured capacity can be used as a criterion for accepting the plant.
