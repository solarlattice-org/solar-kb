---
id: symptom:transformer-seal-loss
type: Symptom
name: Transformer seal loss
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On SMA Sunny Central CP XT inverters, error 6440 reports that the MV transformer has lost its
    hermetic seal. The corrective measure is to check the MV transformer.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r20
    h: 64639d75024e
  review: drafted
---
On SMA Sunny Central CP XT central inverters, transformer seal loss shows up as error 6440. The error means the medium-voltage transformer is no longer hermetically sealed. The manufacturer's corrective measure for this error is to inspect the MV transformer. When you inspect the inside of the transformer, check that the sealing strip is properly fixed. Take an oil sample at the oil leakage port and have it analysed to judge the transformer's operating condition. Regular periodic inspection helps catch abnormal transformer conditions before the damage grows. This matters because taking a transformer out of service causes considerable production losses.
