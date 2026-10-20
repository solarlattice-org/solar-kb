---
id: meas:shorted-diode-reading
type: Measurement
name: Shorted diode reading
aliases:
- short-circuited diode
- Short-circuited bypass diodes
---
The best way to find out whether a bypass diode is shorted or open is to test it directly with a multimeter set to diode or ohmmeter mode. Bypass diodes fail in one of two main ways, short circuit or open circuit, and short circuits are reported more often than open circuits. A diode reads as shorted if it is physically shorted inside the junction box, if it was mounted the wrong way round, or if lightning or static discharge exposed it to high voltage. A shorted bypass diode permanently lowers the module's voltage capability and can shift the maximum power point of the whole array. Before you take a direct diode reading, a shorted diode may first show up as an open-circuit voltage lower than expected, or as a step or notch in the IV curve. If the blocking diode voltage falls outside the pass range, investigate further to find out whether the diode failed on its own or because of another system fault.

<!-- review notes
- sentence 4: support check: partial - The passage says short-circuited diodes constantly have lower voltage capability and may shift the array's MPP, but it doesn't say the lowering is permanent, only 'constantly'. That is close, so the gap is small.
- sentence 5: support check: partial - Lower Voc is stated as a sign of a shorted diode, and a shorted bypass diode is listed as a possible cause of steps or notches. However, notches have many other causes such as shading, so they are not specific to a shorted diode.
-->
