---
id: method:camera-observation
type: DetectionMethod
name: Site camera observation
claims:
- claim_id: c1
  rel: produces
  target: meas:snow-cover-imagery
  note: Camera views showing snow on module surfaces are lined up with SCADA production residuals and
    weather data to confirm snow accumulation losses.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h6
    h: 0935b66311ac
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h2
    h: cf13e86d6896
  review: drafted
---
Site camera observation means using cameras on site to see whether snow is covering the modules. The images are lined up in time with weather data, such as snowfall, snow depth, temperature, wind and irradiance, and with production residuals from SCADA. Together these data confirm snow accumulation losses: the plant is available and sensors show usable sunlight, but snow-covered modules produce no current. Camera views also show how fast the array clears during melt or slide-off, so you can compare that recovery with the snow-loss assumptions in the energy model. The visible snow cover does not always match the energy lost, because partial clearing can leave current uneven across strings and substrings. Also check for cold-weather inverter behavior, clipping, curtailment, frozen tracker stow, sensor icing and albedo effects before blaming snow.

<!-- review notes
- sentence 1: support check: partial - Passages mention camera observations of module cover but never define the term; the use of cameras to see snow cover is only implied.
- sentence 3: support check: partial - Passages describe the signature (plant available, irradiance usable, covered modules can't convert to current) but don't say these data together confirm it, and 'produce no current' overstates partial clearing.
- sentence 4: support check: partial - Passages say to compare measured recovery curves with snow-loss assumptions and mention camera observations, but don't state that camera views show the clearing rate.
-->
