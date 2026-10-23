---
id: comp:ground-fuse
type: Component
name: PV ground fuse
aliases:
- Fuse for solar module ground
---
The PV ground fuse is the fuse that protects the solar module ground path in Fronius Galvo inverters. A defective ground fuse can trigger status code 472, and the inverter then stops feeding energy into the grid. Status code 551 reports the same defective fuse, but only as a warning on the display. The fix is to replace the ground fuse. If the code keeps coming back, contact the system installer. In the Galvo ground settings, the ground mode can be off, positive or negative. When the array is grounded, ground monitoring can be set to warning, error, or both. To get a proper ground connection, tighten all three GND ground terminals to the specified torque during installation.

<!-- review notes
- sentence 1: support check: partial - Passages say the fuse for solar module ground is defective (codes 472/551) but don't name it 'PV ground fuse' or say it protects the ground path, nor mention Galvo specifically.
- sentence 6: support check: partial - Passage says all three GND terminals must be tightened to the specified torque, but it doesn't link to a Galvo-specific context or the 'grounded array' beyond that; core is stated, so only minor detail missing.
- sentence 1: review: partial - The rows describe a 'fuse for solar module ground', but the passage text does not say the fuse protects the ground path or name Fronius Galvo inverters.
-->
