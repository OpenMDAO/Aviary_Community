# Boeing 757-200 Aviary Model
## Running this model
1. Run `aviary run_mission --phase_info B757_mission.py B757.csv`
> If you get a PyOptSparse is not installed error, try `aviary run_mission --phase_info B757_mission.py B757.csv --optimizer SLSQP`

## Model Information
1. Payload: 200 passengers (update `num_passengers` entry in `B757.csv` to change)
2. Range: 3,915 nmi (update `phase_info` in `B757_mission.py` and `mission:design:range` entry in `B757.csv` to change)
3. Engines: Pratt and Whitney 2000

## Model Information Sources
1. https://www.boeing.com/content/dam/boeing/boeingdotcom/company/about_bca/startup/pdf/historical/757_passenger.pdf
2. https://en.wikipedia.org/wiki/Boeing_757#Specifications 
3. For areas and sizes, 3-view images of aircraft and this tool were used: https://www.blocklayer.com/scale-fixereng 