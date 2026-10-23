---
id: meas:battery-temperature-status-high
type: Measurement
name: Battery temperature status high
aliases:
- High battery temperature warning
- BatTmpHiWarn
- W212
---
This status means the battery temperature has entered a critical range, and the battery may not work as well as it should. It is the middle step of a three-level indication: normal means the temperature is inside the permitted range, and too high means the maximum has been exceeded and the battery has been shut down. On Sunny Island systems, battery management shows a warning when the measured battery temperature comes within 5°C of the maximum permissible value. If the maximum is exceeded, the unit switches off and starts again once the battery has cooled down. The temperature is read continuously from the supplied battery temperature sensor. That sensor should sit at the warmest point of the battery bank, and a wrong reading can lead to the wrong charging voltage. Some battery monitoring systems also report the maximum cell temperature across the battery modules as a data point that refreshes every 10 seconds. The usual cause is a battery that is simply too hot. Let it cool down and protect it from temperatures above 25°C, which helps prevent early aging. If the reading looks implausible, check the temperature sensor: its resistance should be about 2000 ohms at room temperature, and you should replace it if the value is far off. When the upper temperature limit set by the battery manufacturer is exceeded, a battery error is reported, so check that the battery's surroundings meet the manufacturer's ambient conditions.

<!-- review notes
- sentence 3: support check: partial - The warning at 5°C below the max and the switch-off are stated, but restarting once the battery has cooled is only in u9, and the passages do not say the warning is shown for the measured temperature on all Sunny Island systems; this is mostly stated, but the 'starts again' is supported by u9 only.
- sentence 7: support check: partial - The sensor resistance check (about 2000 Ω at 20–25°C, replace if far off) is stated, but only as a corrective measure for the overtemperature fault, not for an implausible reading in general.
-->
