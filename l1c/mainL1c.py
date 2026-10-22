
# MAIN FUNCTION TO CALL THE L1C MODULE

from l1c.src.l1c import l1c

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:/Users/cc/Santi/UC3M/EO/Earth-Observation/auxiliary'
# GM dir + L1B dir
#indir = r"C:/Users/cc/Santi/UC3M/EO/EODP_TER_2021/EODP-TS-L1C/input/gm_alt100_act150,C:/Users/cc/Santi/UC3M/EO/EODP_TER_2021/EODP-TS-L1C/input/l1b_output"
indir = r"C:/Users/cc/Santi/UC3M/EO/EODP-TS-E2E/gm_out,C:/Users/cc/Santi/UC3M/EO/EODP_TER_2021/EODP-TS-L1B/myoutputs_l1b"
outdir = r"C:/Users/cc/Santi/UC3M/EO/EODP_TER_2021/EODP-TS-L1C/myoutput_l1c"

# Initialise the ISM
myL1c = l1c(auxdir, indir, outdir)
myL1c.processModule()
