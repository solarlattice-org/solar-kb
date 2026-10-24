---
id: metric:soiling-ratio
type: Metric
name: Soiling ratio
aliases:
- soiling loss
- SR
category: Performance
---
The soiling ratio shows how much of a PV array's output is still available under soiled conditions. It divides the power of the array when soiled by the power of the same array when clean. A value of one means there is no soiling loss. The ratio falls as dirt builds up and reaches zero when soiling blocks all light from the cells, so it is really a measure of cleanliness. The soiling loss, which IEC 61724 also calls the soiling level, is one minus the soiling ratio. Using power from a soiled device and a clean device is the preferred method. Many setups use the temperature-corrected short-circuit current of a soiled and a clean reference device instead, especially when noisy voltage readings make the power data unreliable. The short-circuit current method can understate the loss when soiling is uneven, for example dirt collected along the bottom row of cells. That is because a bypassed substring cuts power but does not change the module's short-circuit current. IEC 61724 recommends measuring within two hours of solar noon for fixed arrays, or at an angle of incidence below about 35 degrees for trackers. Results may be given as daily, seasonal or annual values, either as simple averages or weighted by irradiance. The soiling rate is a related metric: the daily change in soiling ratio between cleaning events, given in percent per day and usually reported as a negative number. To get a soiling-corrected performance ratio, divide the performance ratio by the soiling ratio.

<!-- review notes
- sentence 4: support check: partial - Power ratio as preferred and SC current as alternative when voltage jitter affects power are stated, and SC current is temperature-corrected, but 'many setups' is roughly supported by 'in most cases' while the clean 'reference' device wording and the link are fine; however the passage doesn't say it's 'especially' due to noisy voltage beyond jitter example, minor.
- sentence 6: support check: partial - The IEC recommendations on timing are stated and daily/seasonal/annual and irradiance-weighted averages are mentioned, but the passages do not attribute those reporting options to IEC 61724.
-->
