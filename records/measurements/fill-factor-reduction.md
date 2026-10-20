---
id: meas:fill-factor-reduction
type: Measurement
name: Reduced fill factor
aliases:
- FF
---
Fill factor is one of the parameters that an IV curve trace gives for a single module or a string, along with power, short-circuit current, open-circuit voltage, and series and shunt resistance. A reduced fill factor means the IV curve shape has changed in a way that string Isc and Voc readings alone may not show. To judge the fill factor of a string, compare the measured curve with the theoretical sum of the individual module IV curves, then go to the string to find the faulty modules or the shading. For reference, typical fill factors at STC are 0.75 to 0.80 for polycrystalline silicon cells and 0.80 to 0.85 for monocrystalline silicon cells. Severe metallization corrosion lowers the fill factor because series resistance rises, and it usually also lowers short-circuit current. Light induced degradation lowers the fill factor together with short-circuit current, open-circuit voltage and maximum power. Measuring individual modules means disconnecting the whole string and losing production, so try visual inspection or infrared imaging first.

<!-- review notes
- sentence 2: support check: partial - u6 says the IV curve shows degradation not always found from string Isc and Voc, but it does not say a reduced fill factor specifically means a changed curve shape.
- sentence 5: support check: partial - u9 gives FF down from higher Rs and Isc down as IV signatures of corrosion, but says nothing about 'severe' corrosion or that Isc usually drops.
- sentence 7: support check: partial - u6 supports disconnecting the full string with production loss and trying visual inspection or IRT first, but it says the disconnection is needed for individual module measurements without saying the whole string must be disconnected as a general rule; the core is stated.
-->
