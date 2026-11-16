# QuantumBeat: a contactless quantum heart monitor (concept demo)

**Live app:** https://ahmedpoowid.github.io/quantumbeat/

QuantumBeat is our team's project for the ATRC Quantum Challenge 2026–2027
(Applied Technology School – Al Ain). Quantum magnetometers could read the heart's
tiny magnetic field without electrodes, and statistics flag unusual gaps between beats.

This web app is a concept demonstration. Press **Run sample scan** to generate a
30-second synthetic heartbeat signal. The app then measures the average heart rate
and every beat gap, and flags gaps with a z-score above 1.5.

> Synthetic data only. It does not connect to a sensor or measure a real heart.
> Not for diagnosis or treatment.

The whole app is one file, `index.html`, so it also works offline: download it and
open it in any web browser.
