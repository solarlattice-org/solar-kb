---
id: method:module-level-playback-review
type: DetectionMethod
name: Module-level production playback review
aliases:
- Show playback
- layout playback
- module-level monitoring comparison
- playback feature
- weekly playback
claims:
- claim_id: c1
  rel: produces
  target: meas:module-late-wakeup
  note: In the example, two modules produced less than their peers until about 9 am, with the lowest point
    at 8:30, every day. This confirmed shading.
  quote: PV modules 1.0.15 and 1.0.18 "wake up" later than the others. This is likely caused by shading.
  cite:
  - src: src:se-academy-monitoring-platform-na-technical-06-system-performance-analysis-in-the-monitoring-platform
    loc: sec=h4
    h: f0f37319d05b
  - src: src:se-academy-monitoring-platform-02-system-performance-analysis-in-the-monitoring-platform
    loc: sec=h4
    h: d5c282e7ccb2
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
Module-level production playback review is a remote check in the monitoring platform's Layout tab. It replays the power of each module over a chosen day or week. Open the Layout tab and expand Show playback. Pick a Daily or Weekly period, drag the red line bar to the day or time you want, and press Play. Pick a sunny day for the review, because shading effects are hard to see on cloudy days. Modules that wake up later or produce less than their neighbours at the same time each day point to shading. Confirm it by checking that the pattern repeats across the week. Weekly playback is especially useful in winter, when the low sun brings more underproduction complaints. If the loss happens at a set time, have the owner look at the roof at that time. Playback helps rule out shading and module diode problems before a site visit, which avoids unnecessary truck rolls. A suspected optimizer still has to be tested on site, and a suspected panel diode should be raised with the module manufacturer. Playback alone does not separate every cause of underproduction. String design, incorrect mapping, a failing optimizer and a failing panel are also listed as possible sources.

<!-- review notes
- sentence 6: support check: partial - Playback to check shading and diode issues to avoid truck rolls, optimizer tested on site, and panel diode via module manufacturer are stated; but 'rule out' diode via playback is loosely worded, and fine detail is plausible.
- sentence 7: support check: partial - Other sources are listed, but the passage does not explicitly say playback alone cannot separate every cause; that is an inference.
- sentence 7: review: partial - The other underproduction sources (string design, incorrect mapping, failing optimizer, failing panel) are listed, but the claim that playback alone cannot separate every cause is an inference the passage does not state.
-->
