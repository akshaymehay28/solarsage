# Thermographic (Infrared) Inspection

Infrared thermography finds electrical and cell-level faults by their heat
signatures while the plant operates under load. It is fast, non-contact, and
covers whole arrays - drone-mounted IR cameras can survey many megawatts per
day.

## Conditions for a valid survey

Survey under clear skies at irradiance of at least 600 W/m2, with the array
under normal operating load (not open-circuited - many faults only heat up
when current flows). Fly or view at a low incidence angle to avoid sky
reflections, early enough in the day that thermal contrast is not washed out.

## Interpreting thermal patterns

A single hot cell suggests cell damage, cracking, or localised shunting. A
patchwork or checkerboard of warm cells across a module suggests PID. One
substring uniformly warmer than the other two indicates a shorted or
conducting bypass diode. An entire module warmer than its neighbours often
means it is open-circuited (not producing, so absorbed light becomes heat).
A hot junction box points to a failing diode or connection inside; a hot
connector or cable termination indicates a high-resistance joint.

Temperature deltas guide urgency: differences under about 5 degrees Celsius
are usually benign or measurement noise; 5-10 degrees warrants tracking;
above 10-20 degrees against comparable cells or components warrants prompt
electrical follow-up (IV trace, EL image, or physical inspection).

## Limits

Thermography localises but does not fully diagnose - a hot cell could be a
crack, shading residue, or shunting. Confirm root cause with EL imaging or
IV curve tracing before replacing hardware.
