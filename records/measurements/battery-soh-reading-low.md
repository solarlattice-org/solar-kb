---
id: meas:battery-soh-reading-low
type: Measurement
name: Low battery SOH reading
aliases:
- SOH
- State of health
- Usable battery capacity
- 320.01 Soh
---
The battery state of health (SOH) is the usable battery capacity shown as a percentage of the nominal capacity. 100% means the full nominal capacity is usable and 50% means only half of it is. SMA battery inverters raise a battery fault or warning when the current SOH falls below 70%. The corrective step is to check that the message is plausible and to replace the battery if needed. SOH is not measured directly. It is estimated from measurable values, algorithms and parameter settings, so a wrong installation or wrong parameters can make the reading inaccurate. The inverter starts SOH at 100% after commissioning. It then learns the real value over several charge cycles, and only if the lead-acid battery is cycled and has recurring idle phases under low load. A loss of a few percent per year or per 100 cycles is normal battery aging. A drop of several ten percent in the first months after commissioning points to a possible error. Battery aging and frequent insufficient charging lower the usable capacity, either for good or only for a while. A battery whose real capacity is below the manufacturer's rating also gives a low reading, and a capacity test will confirm this. Below the rated temperature, the reported capacity is automatically adjusted downward. Read low SOH values in cold conditions with this in mind. The estimate is accurate to within ±15 %, so an exact value needs an on-site capacity test by qualified staff. If the cause is removed before permanent damage occurs, SOH can recover over several weeks.

<!-- review notes
- sentence 6: support check: partial - Aging and insufficient charging lowering capacity (permanent or temporary) is in u7, and u12 says the battery may have lower capacity than specified with a capacity test as the measure, but 'a capacity test will confirm this' is stronger than the passages.
- sentence 8: support check: partial - The ±15% accuracy, the need for measurement by qualified on-site staff for a more accurate value, and recovery over several weeks if no irreversible damage occurred are all stated, but the 'accurate to within ±15%' and 'exact value' framing is slightly stronger than 'more accurate'.
-->
