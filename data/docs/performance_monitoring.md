# PV Performance Monitoring

Continuous monitoring separates normal weather-driven variation from genuine
faults, enabling operators to intervene before small losses become large ones.

## Performance ratio

The performance ratio (PR) is the ratio of actual energy yield to the yield
theoretically possible given measured irradiance. A healthy, well-maintained
system typically achieves a PR of 0.80-0.90. Sustained PR below 0.75 signals
a problem such as soiling, degradation, inverter clipping, or string outages.
PR should be temperature-corrected for meaningful comparison across seasons.

## Key weather variables

Plane-of-array irradiance is the dominant driver of output and the most
important variable to measure accurately. Module (or ambient) temperature is
second: crystalline silicon output falls roughly 0.3-0.45% per degree Celsius
above 25 C. Wind speed matters as it cools modules, and humidity and rainfall
inform soiling models. Combining these with historical output enables
expected-yield models against which faults are flagged.

## Fault signatures

Different faults leave different signatures: soiling shows gradual loss
strongest at high irradiance; PID shows progressive string-level loss;
bypass diode failure shows a fixed step loss; inverter faults show abrupt
total or partial outages. Feature engineering over time-lagged weather and
output data allows machine learning classifiers to separate these signatures.
