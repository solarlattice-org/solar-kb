---
id: method:ml-fault-classification
type: DetectionMethod
name: Machine-learning fault classification
aliases:
- machine learning classifier
- Classification
claims:
- claim_id: c1
  rel: produces
  target: meas:prediction-bound-exceedance
  note: The classifier learns an expected power range from inverter parameters or past data; growing or
    sustained deviations outside it are flagged as a fault. In one field test a shaded module dropped
    power below the lower limit, but a later upper-limit crossing was a false alarm.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=h66
    h: 57e442fcb83c
  - src: src:iea-pvps-t13-07-2017
    loc: sec=5.3.1.1
    h: 33ef5a556b09
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:array-ratio-out-of-range
  note: The valid range is learned by linear regression on three months of power and irradiance history;
    for new plants a KNN estimate is used. A rule-based stage then diagnoses the fault.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=8.1
    h: 0feb8201aec2
  review: drafted
  review_note: 'support check: partial - Passages support the regression-learned range over three months,
    consecutive-out-of-range detection, KNN for new plants, irradiance filtering below 250 W/m2 and rule-based
    diagnosis, but not that POA irradiance is the reference specifically (pyrheliometer is mentioned).'
- claim_id: c3
  rel: produces
  target: meas:iv-curve-fault-class
  note: A Support Vector Machine evaluated I-V curve data at given instants and labelled each curve normal
    or faulty.
  cite:
  - src: src:iea-pvps-t13-07-2017
    loc: fig=38
    h: 0406c11857ea
  review: drafted
---
Machine-learning fault classification is a supervised method: a model is trained on labelled monitoring data and then sorts new observations into categories, such as normal operation or a particular type of fault. Common algorithms include decision trees, K nearest neighbors, logistic regression, neural networks and support vector machines. The data is divided into a training set and a separate test set, so the model's accuracy can be checked against data it has not seen before. In field use, the model learns the expected AC power or power-to-irradiance ratio from inverter and irradiance data and raises a fault when measured output stays outside that range. Reported examples detected partial shading, inverter faults, blown fuses, open string circuits and overheated inverters, and research also targets diagnosis of DC series arc faults. The same approach can classify I-V curves or EL cell images, for example sorting cells into good, cracked or corroded. Accuracy depends on how much training data there is: cracked cells were classified poorly because there were few examples and crack patterns vary a lot. False alarms still happen, so a flagged fault should be confirmed on site before any repair is made.

<!-- review notes
- sentence 8: support check: partial - The passage documents a false alarm, but it does not say a flagged fault should be confirmed on site before repair.
-->
