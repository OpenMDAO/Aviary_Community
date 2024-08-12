# LM C5 Galaxy - Multimission Aviary Setup
## Running The Mission
1. Open C5_Galaxy And Run The Following In The Terminal:
`python runScript.py`

2. To See An Overview Of The Mission, Run The Following Command After The Optimization Finishes: `aviary dashboard runScript`

## Model Information
C5_phase_info.py contains the function mission_select() which contains the phase info for two seperate missions. mission_select() takes in several inputs in order to select which mission you want to run and how to run the mission (i.e. the simulation parameters). This allows the user to have multiple different mission profiles saved and easily toggle between them which is convenient when considering more than one possible mission for example. The inputs, in order, to mission_select() are:

1. `phase_select` (str, no default): Which mission profile to choose

2. `Opt_mach` (bool, default = False): True turns mach into a variable, false follows the predefined mach bounds

3. `Opt_alt` (bool, default = False): True turns altitude into a variable, false follows the predefined altitude bounds

4. `Opt_mass` (bool, default = True): True turns mass into a variable, optimizes for fuel burn

5. `takeoff` (bool, default = False): Add a simplified takeoff simulation to the mission (if false then the mission begins at climb)

6. `landing` (bool, default = False): Add a simplified landing simulation to the mission (if false then the mission end at the ends of descent)

7. `polynomial_control_order` (int, default = 2): Polynomial order for dymos

8. `num_segments` (int, default = 3): How many segments dymos should use for the mission 

9. `order` (int, default = 3): Order for dymos

Since all inputs have a default value, only phase_select must be specified in order to run. The first mission in C5_phase_info.py is a simple mission including a climb, cruise, and descent phase. The seccond mission is similar to the first but with an additional climb phase added.

## Modifying Outputs
1. To have Aviary print the simulation run to an output file, run the following command instead (replacing `<OUTPUT_FILE_NAME>` with the correct name for the output file): `python runScript.py > <OUTPUT_FILE_NAME>`

2. To have Aviary output all values from the mission/simulation add the following to runScript.py at the end of the 'Run Aviary' section: `prob.model.list_vars(print_arrays = True , units = True)`

3. To check the accuracy of all partial derivatives from the simulation add the following at the end of the 'Run Aviary' section of runScript.py: `prob.check_partials()`