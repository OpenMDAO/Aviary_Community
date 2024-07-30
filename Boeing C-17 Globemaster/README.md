# Boeing C-17 Globemaster Aviary Model
## Running this model
1. Run `aviary run_mission --phase_info C17_mission.py C17.csv`
> If you get a PyOptSparse is not installed error, try `aviary run_mission --phase_info C17_mission.py C17.csv --optimizer SLSQP`
2. To view the results, run `aviary dashboard C17`

## Model Information
1. Payload: 164,900 lbs (update `cargo_mass` entry in `C17.csv` to change)
2. Range: 2,400 nmi (update `phase_info` in `C17_mission.py` and `mission:design:range` entry in `C17.csv` to change)
3. Engines: Pratt and Whitney 2000

## Model Information Sources
1. https://www.af.mil/About-Us/Fact-Sheets/Display/Article/1529726/c-17-globemaster-iii/
2. https://en.wikipedia.org/wiki/Boeing_C-17_Globemaster_III#Specifications_(C-17A) 
3. For areas and sizes, 3-view images of aircraft and this tool were used: https://www.blocklayer.com/scale-fixereng 
4. Author: Jatin Soni