---
id: meas:dc-voltage-outside-mppt-range
type: Measurement
name: DC voltage outside MPPT range
aliases:
- Out of MPPT Zone
signals:
- point: model_103.DCV
  unit: unit:V
  pattern: DC input voltage below or above the MPPT window while AC power is reduced
---
This signature is a DC input voltage that falls below or rises above the rated MPPT voltage window of the inverter. Outside that window the inverter reduces its output power, and the reduction grows linearly with the distance from the range. The window depends on the model: for example, the SCA36KTL starts derating below 400V or above 800V, and the PVI 36TL starts below 540V or above 800V. Check the datasheet MPPT voltage range of the specific inverter, and keep in mind that some models let you adjust this range from the LCD. Monitoring systems can log DC voltage separately for each MPPT input, so you can compare each input with its limits. Inverter voltage floor losses produce this pattern when the array Vmp drops below the inverter's minimum DC input voltage. The inverter then cannot hold the maximum power point, and energy is left unused on the DC side.

<!-- review notes
- sentence 2: support check: partial - Passages say inverters derate linearly outside the MPPT range, but don't state the reduction grows linearly with distance from the range; the figure text is absent.
-->
