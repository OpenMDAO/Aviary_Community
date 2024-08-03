import aviary.api as av
from MD90_phase_info import phase_info  
prob = av.run_aviary('MD90.csv',phase_info, optimizer="SLSQP", make_plots=True,max_iter=1000)
# prob.model.list_vars()