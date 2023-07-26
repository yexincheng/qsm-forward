"""
This script uses the qsm_forward library to generate BIDS-compliant files 
from a simulated MRI data. 

The simulation uses default reconstruction parameters (with peak_snr set to 100)
and tissue parameters that are generated by the `simulate_susceptibility_sources` 
function of the qsm_forward library.

The simulation results are saved in the "bids" directory.

Author: Ashley Stewart (a.stewart.au@gmail.com)
"""


import qsm_forward

if __name__ == "__main__":
    recon_params = qsm_forward.ReconParams()
    recon_params.subject = "simulated-sources"
    recon_params.peak_snr = 100

    tissue_params = qsm_forward.TissueParams(
        chi=qsm_forward.generate_susceptibility_phantom(
            resolution=[100, 100, 100],
            background=0,
            large_cylinder_val=0.005,
            small_cylinder_radii=[4, 4, 4, 7],
            small_cylinder_vals=[0.05, 0.1, 0.2, 0.5]
        )
    )

    qsm_forward.generate_bids(tissue_params, recon_params, "bids")

