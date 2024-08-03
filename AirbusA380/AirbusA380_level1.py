import aviary.api as av
from AirbusA380_phase_info import phase_info  
prob = av.run_aviary('AirbusA380.csv',phase_info, optimizer="SLSQP", make_plots=True,max_iter=200)
# prob.model.list_vars()

