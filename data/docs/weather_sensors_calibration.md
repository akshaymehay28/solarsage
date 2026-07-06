# Weather Sensors and Data Quality

Fault detection is only as good as the weather data it compares against. A
miscalibrated pyranometer produces phantom faults or masks real ones.

## Instrumentation

Plane-of-array (POA) irradiance is the reference for performance-ratio
calculations. Thermopile pyranometers are the accuracy standard (1-2%);
silicon reference cells are cheaper and spectrally match PV better but
drift differently. Large plants should carry at least two independent
irradiance sensors so a drifting sensor can be identified by disagreement.
Module temperature sensors (back-of-module thermocouples) matter because
power corrections of roughly 0.4%/degree make a 5-degree error a 2% power
error. Ambient temperature, wind, and rainfall complete a basic station.

## Common data-quality failures

Soiled pyranometer domes read low, inflating apparent performance - clean
sensors on every site visit. A sensor knocked out of the array plane reads
the wrong geometry all day. Night-time non-zero irradiance offsets, frozen
values (stuck sensor or datalogger), and timezone or daylight-saving
misconfiguration (irradiance peak offset from solar noon) are all common
and all detectable with automated checks.

## Automated validation

Apply range checks (clear-sky irradiance ceiling for the site's latitude),
rate-of-change limits, cross-sensor consistency checks, and comparison with
satellite-derived irradiance as an independent reference. Flag rather than
silently correct: sensor faults and array faults can look identical until a
human confirms which side of the comparison is lying.
