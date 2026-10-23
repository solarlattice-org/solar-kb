---
id: mit:ground-fuse-replacement
type: Mitigation
name: Ground fuse replacement
aliases:
- fuse for solar module ground
---
Ground fuse replacement means swapping out a defective fuse in the grounding path of the solar modules. On the Fronius Galvo, status code 472 reports a defective module ground fuse, and the inverter stops feeding power into the grid until the fuse is replaced. Status code 551 reports the same defective fuse but only as a warning on the display, and the fix is the same. If either code comes back after the fuse has been replaced, call the system installer instead of just fitting another fuse. On grounding fuses like the SMA Plug-in Grounding, a sudden strong residual current from a ground fault blows the fuse. Find and clear the ground fault first, then check the fuse and replace it if needed. The inverter also detects residual currents that persist over time, so clearing a ground fault early can keep the fuse from blowing. Before replacing any fuse, check that the new fuse exactly matches the original size, prepare the site for maintenance and wear the required PPE.

<!-- review notes
- sentence 2: support check: partial - Code 472 row states defective module ground fuse and no grid feed-in with replacement as the fix, but the passage does not mention the Fronius Galvo model.
- sentence 4: support check: partial - Both rows say to contact the installer if the code keeps recurring, but they do not say 'after replacement' or 'instead of fitting another fuse'.
-->
