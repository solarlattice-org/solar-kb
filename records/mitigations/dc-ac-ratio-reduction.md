---
id: mit:dc-ac-ratio-reduction
type: Mitigation
name: DC to AC ratio reduction
---
DC to AC ratio reduction means designing or reconfiguring the array so that the DC power connected to an inverter stays within the ratio recommended for that inverter. It protects against DC overload of the inverter: going over the recommended ratio can damage the inverter and voids the warranty. Strings should be sized to respect both the DC/AC ratio and the short-circuit current (Isc) limits, and to meet all applicable electrical codes. Each inverter model has its own maximum allowed ratio, so check the manual for that model; for example, Schneider Electric recommends a maximum of 1.5 for the Conext CL125. On the Conext CL125, any design above that limit must be reviewed by a Schneider Electric applications engineer. At sites that often see more than 1000 W/m2 of irradiance, one manual recommends keeping the ratio below the 1.5 limit. A lower ratio also cuts inverter clipping losses; once clipping goes above about 3%, raising the DC ratio further may add little value. The best ratio depends on the site's location and racking style, because a tracker or a site with strong sun delivers much more energy than a low fixed tilt or a weaker sun region.

<!-- review notes
- sentence 1: support check: partial - Passages say the recommended DC/AC ratio must be observed when sizing, but don't define 'DC to AC ratio reduction' as designing/reconfiguring to stay within the recommended ratio.
- sentence 7: support check: partial - Diminishing value above 3% clipping is stated, but the passage doesn't say a lower ratio cuts clipping losses (implied only by the clipping/ratio relation).
-->
