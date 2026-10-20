---
id: stressor:low-sun-angle
type: Stressor
name: Low sun angle
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 3
    max: 4
    unit: unit:PERCENT
  conditions: Combined winter loss from angle of incidence and low light at high-latitude, cold-climate
    sites such as Fairbanks, Alaska, as a share of annual energy production
  note: The loss stays small because summer insolation is much higher. For most crystalline silicon modules,
    angle-of-incidence losses are reported as negligible below about 60 degrees.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h87
    h: b622923feee6
  review: drafted
---
A low sun angle means the sun sits close to the horizon, so light hits the modules at a steep incidence angle and less of it reaches the cells. This is most pronounced at high latitudes in winter, where the sun may rise only about 2 degrees above the horizon at the solstice and give only a few hours of dim light. On tracker sites with rolling ground, terrain undulation yield losses are strongest in low sun-angle periods and tend to cluster at motor block boundaries, grade breaks and swales. Low sun angles, together with cold module temperatures, frame geometry and tracker position, affect how long snow stays on the array, which prolongs snow accumulation yield losses. Shade patterns move with the sun's position through the day and the seasons, and row-to-row self-shading grows when the sun's profile angle drops below the shading angle of the rows. Performance analyses often filter out periods of low solar elevation, because these periods add shading, self-shading and air-mass differences to the data. Exposure can be reduced by tuning backtracking parameters for each terrain zone, checking motor block sizing, and adjusting tilt or module orientation at the design stage. At snowy sites, operators can look at tracker stow, tilt or design changes where the economics justify them.

<!-- review notes
- sentence 1: support check: partial - Passage says greater angles of incidence couple less light onto cells and gives low sun elevation examples, but does not explicitly define low sun angle as near the horizon causing steep incidence.
- sentence 4: support check: partial - Passage says these factors affect how long snow remains, but doesn't say 'prolongs snow accumulation yield losses' or the direction of effect for each factor.
- sentence 5: support check: partial - Shade patterns changing over day and season and profile angle vs shading angle are stated, but not explicitly that row self-shading grows when profile angle drops below shading angle (implied by PRshaded definition).
- sentence 7: support check: partial - Backtracking refinement by zone and motor block sizing validation are in the mitigation, but tilt/module orientation adjustment at design stage is only from general shading evidence not tied to terrain; 'checking' vs 'adjusting tilt' is not stated for terrain.
-->
