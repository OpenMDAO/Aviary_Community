# Boeing C-40 Clipper Aviary Model
## Running this model
1. Run `aviary run_mission --phase_info C40_mission.py C40.csv`
> If you get a PyOptSparse is not installed error, try `aviary run_mission --phase_info C40_mission.py C40.csv --optimizer SLSQP`
2. To view the results, run `aviary dashboard C17`

## Model Information
1. Payload: 36,000 lbs (update `cargo_mass` entry in `C40.csv` to change)
2. Range: 3,200 nmi (update `phase_info` in `C40_mission.py` and `mission:design:range` entry in `C40.csv` to change)
3. Engines: CFM56 27,300 lbf turbofans

## Model Information Sources
1. https://www.boeing.com/content/dam/boeing/boeingdotcom/defense/c-40_series/pdf/c40a_product_card.pdf,
2. https://www.boeing.com/defense/c-40a#tech-spec 
3. https://en.wikipedia.org/wiki/Boeing_C-40_Clipper#Specifications 
4. For areas and sizes, 3-view images of aircraft and this tool were used: https://www.blocklayer.com/scale-fixereng 
5. Author: Jatin Soni