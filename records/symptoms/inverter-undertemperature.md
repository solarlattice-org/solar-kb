---
id: symptom:inverter-undertemperature
type: Symptom
name: Inverter undertemperature
aliases:
- Excessively Low Ambient Temperature
- Minimum operating temperature not reached
- Low ambient temperature
---
This alarm means the inverter has found that the temperature is below the lowest temperature it can run at, so it stops feeding power to the grid. For the Sungrow units, the manual says to stop and disconnect the inverter, then restart it once the ambient temperature is back inside the operating range. It helps to log the inverter's internal temperature as a regular monitoring channel, so that low-temperature and high-temperature events can both be checked afterwards. This is the opposite of the excessively high ambient temperature alarm. The high-temperature alarm points to poor ventilation, direct sun or fan problems, and none of those apply to the cold-temperature stop.

<!-- review notes
- sentence 3: support check: partial - u11 advises recording inverter temperature (for ventilation/overheating assessment) and logging internal temperature, but doesn't mention checking low-temperature events afterward.
- sentence 4: support check: partial - The high-temperature fault's causes (ventilation, sunlight, fan) are listed in u10/u17 and the low-temperature fix doesn't involve them, but the passages don't explicitly say they don't apply or call it an opposite.
-->
