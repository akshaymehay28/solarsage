# Commissioning and Acceptance Testing

Commissioning establishes the baseline every later fault diagnosis compares
against. A plant commissioned carelessly will generate spurious "faults"
(or hide real ones) for its whole life.

## Electrical verification

Test every string: open-circuit voltage (against expected Voc for module
count and temperature), short-circuit or operating current under recorded
irradiance, insulation resistance to ground, and polarity - reversed strings
still produce plausible combiner-level readings and are a classic
commissioning miss. Sample IV curve traces provide the reference curves for
future comparison; store them with the irradiance and temperature at which
they were taken.

## Performance acceptance

A capacity test compares measured output against the model (typically PVsyst)
under a contractually defined regression method over several days of good
weather. An availability test proves the plant runs without trips over a
defined period. Both depend on calibrated irradiance sensors - certificate
dates matter and disputes frequently reduce to sensor calibration.

## Documentation baseline

The as-built record should include string maps (which modules feed which
combiner and inverter input), module serial numbers by position, all
commissioning measurements, setpoint and protection settings, and sensor
calibration certificates. Fault response later depends on this: locating an
underperforming string in monitoring is only useful if the string map tells
a technician which physical row to walk to.

## First-year review

Re-baseline after initial LID stabilisation and the first seasonal cycle;
early trend data reveals installation defects (loose terminations heating,
mis-aimed sensors) while remedies are still under installer warranty.
