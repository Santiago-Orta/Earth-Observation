
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:/Users/cc/Santi/UC3M/EO/Earth-Observation/auxiliary'
#indir = r"C:/Users/cc/Santi/UC3M/EO/EODP_TER_2021/EODP-TS-ISM/input/gradient_alt100_act150" # small scene
indir = r"C:/Users/cc/Santi/UC3M/EO/EODP-TS-E2E/sgm_out"
outdir = r"C:/Users/cc/Santi/UC3M/EO/EODP-TS-E2E/sgm_out/myoutput"

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
