---
id: prod:sma-sb-av-41
type: Product
name: Sunny Boy 3.0-6.0-1AV-41
aliases:
- SB 1AV-41
- SBx.x-1AV-41
- SBxx-1AV-41
- SB3.0-1AV-41
- SB3.6-1AV-41
- SB4.0-1AV-41
- SB5.0-1AV-41
- SB6.0-1AV-41
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  note: Listed in SMA's Sunny Boy manuals knowledge-base article.
  cite:
  - src: src:sma-kb-sunny-boy-manuals
    loc: sec=h1
    h: 21d1434a3c94
  review: drafted
- claim_id: c2
  rel: lacks
  target: func:system-manager
  scope:
    firmware_min: 3.10.xx.R
  note: SMA device compatibility table marks System Manager functionality as not available for the SB
    1AV-41 models (listed from firmware 3.10.xx.R).
  cite:
  - src: src:sma-doc-275857
    loc: tbl=3.r2
    h: 9cdb07995308
  - src: src:sma-doc-275857
    loc: tbl=3
    h: 63e5d75ca23e
  review: drafted
---
One SMA compatibility table supports these inverters from firmware 3.10.xx.R. Another lists the minimum inverter firmware as 3.10.18.R. The same table marks System Manager functionality as not available for this family. SMA lists these inverters as not having a user interface powered by ennexOS. Manuals and other documents for the family are available through SMA's Sunny Boy manuals article and download area.
