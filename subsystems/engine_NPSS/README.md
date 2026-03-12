**Subsystem:** Numerical Propulsion System Simulation (NPSS)

**Author:** NASA

**Description:**

Subsystem for NPSS within Aviary. Sizes an NPSS model and produces a tabular engine performance data file in pre-mission, and interpolates on that data during mission.

Includes an example NPSS engine model, which is sized for a "standard" ~150 pax class single aisle transport

*Note* this subsystem was created in pre-1.0 Aviary and may not work out-of-the-box in current versions due to filepath changes or small changes in API

**Files:**

- `NPSS_Model/`: Folder containing the example NPSS engine model and OpenMDAO wrapper
- `test/`: Python unittest to verify subsystem is working
- `NPSS_engine_builder.py`: Aviary SubsytemBuilder definition
- `run_NPSS_example.py`: Sample script that runs an Aviary sizing problem incorporating the NPSS model as an external subsystem