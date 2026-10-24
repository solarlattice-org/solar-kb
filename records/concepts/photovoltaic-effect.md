---
id: concept:photovoltaic-effect
type: Concept
name: Photovoltaic effect
aliases:
- p-n junction photovoltaic effect
- photoelectric effect
category: Modules
concept_kind: physics
claims:
- claim_id: c1
  rel: explains
  target: comp:solar-cell
  note: A PV cell is defined as the most basic device showing the photovoltaic effect; cells are large-area
    photodiodes that turn light into electricity.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h196
    h: b8f165b409bd
  - src: src:iec-62446-1
    loc: sec=h53
    h: 3f51a01c98c4
  - src: src:se-academy-solaredge-gtec-solar-pv-components-08-how-do-solar-cells-work-video
    loc: sec=h1
    h: e6551044cc86
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:crystalline-silicon
  note: Doped silicon wafers form the p-n junction where the effect takes place; mono and poly cells work
    on the same principle.
  cite:
  - src: src:se-academy-solaredge-gtec-solar-pv-components-08-how-do-solar-cells-work-video
    loc: sec=h1
    h: e6551044cc86
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:open-circuit-voltage
  note: Charge carriers separated by the junction field build up a potential difference between the n
    and p regions; a single cell gives only around 0.5 V.
  cite:
  - src: src:se-academy-solaredge-gtec-solar-pv-components-08-how-do-solar-cells-work-video
    loc: sec=h1
    h: e6551044cc86
  review: drafted
---
The photovoltaic effect turns radiant energy, usually sunlight, straight into electrical energy. Unlike a heat engine, it involves no thermal step. A PV cell is the simplest device that shows this effect. One manual describes cells as large-area photodiodes. In a silicon cell, phosphorus doping makes an n-type layer with free electrons and boron doping makes a p-type layer with holes. Where the two layers meet, a depletion region with a built-in electric field forms. Light that reaches the depletion region creates electron-hole pairs. The junction field pushes the electrons and holes to opposite sides, which builds up a voltage between the n and p regions. When a load is connected, electrons flow through it and recombine with holes in the p region, so the cell delivers direct current. Real cells use a thin, heavily doped top n layer and a thick, lightly doped p layer. This widens the depletion region and lets more light reach it, so the cell produces more current. A single cell gives only around 0.5 volt. Cells are therefore connected in series and parallel inside a module to reach usable voltage and current, and an inverter converts the DC to AC for the grid.
