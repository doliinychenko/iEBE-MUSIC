#!/usr/bin/env python
"""
    This script contains all the default parameters in the iEBE-MUSIC package.
"""

from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import shutil
import argparse

# initial condition
initial_dict = {
    'initial_state_type': "3DMCGlauber",  # 3DMCGlauber, IPGlasma
}


# IPGlasma
ipglasma = {
    'type': "minimumbias",  # minimumbias or fixed
    'database_name_pattern': "IPGlasma_database/AuAu_C{0:s}.h5",  # path for the database file
}


# 3DMCGlauber model
mcglauber_dict = {
    'database_name': "self",     # self: generate initial condition on the fly
    'Projectile':  "Pb",         # projectile nucleus name
    'Target'    :  "Pb",         # target nucleus name
    'roots'     :   17.3,        # collision energy (GeV)
    'useQuarks' :   1,           # switch to use valence quarks
    'Q2'        :   1.,          # the scale when evaluating the pdf
    'b_min'     :   0.,          # minimum impact parameter (fm)
    'b_max'     :   20.,         # maximum impact parameter (fm)
    'seed'      :   -1,          # random seed (-1: system)
    'only_event_statistics': 0,  # flag to only output the event_summary file
    'baryon_junctions': 0,       # 0: baryon number assumed to be at string end
                                 # 1: baryon number transported assuming baryon
                                 # junctions (at smaller x)
                                 # see arXiv:nucl-th/9602027
    'lambdaB': 0.4,              # parameter the controls the strength of
                                 # the baryon junction stopping
    'QCD_string_production_mode': 1,    # string production mode
                                        # 1: strings are produced randomly in the binary collision list
                                        # 2: strings are produced at the last binary collision
    'rapidity_loss_method': 2,          # 1: LEXUS
                                        # 2: parameterization
    'evolve_QCD_string_mode': 2,        # string evolution mode
                                        # 1: deceleration with fixed rapidity loss (m/sigma = 1 fm, dtau = 0.5 fm)
                                        # 2: deceleration with LEXUS sampled rapidit loss (both dtau and sigma fluctuate)
                                        # 3: deceleration with LEXUS sampled rapidit loss (m/sigma = 1 fm, dtau fluctuates)
                                        # 4: deceleration with LEXUS sampled rapidit loss (dtau = 0.5 fm, m/sigma fluctuates)
}


# MUSIC
music_dict = {
    'echo_level':  1,   # control the mount of message output to screen
    'mode': 2,          # MUSIC running mode 2: Evolution only.
    'Initial_profile': 9,   # type of initial condition 
                            # 9: IPGlasma (full Tmunu),
                            #   -- 91: e and u^\mu,
                            #   -- 92: e only,
                            #   -- 93: e, u^\mu, and pi^\munu
                            # 13: dynamical initialization (3dMCGlauber)
                            #   -- 131: 3dMCGlauber with zero nucleus thickness
    # read in initial conditions from external file
    'Initial_Distribution_input_filename': 'initial/epsilon-u-Hydro.dat',
    's_factor': 0.190,      # normalization factor read in initial data file
    'Initial_time_tau_0': 0.4,  # starting time of the hydrodynamic evolution (fm/c)
    'Total_evolution_time_tau': 30.,  # the maximum allowed running evolution time (fm/c)
    'Delta_Tau': 0.005,             # time step to use in the evolution [fm/c]
    'boost_invariant':  1,  # whether the simulation is boost-invariant 
    'Eta_grid_size': 14.0,  # spatial rapidity range 
                            # [-Eta_grid_size/2, Eta_grid_size/2 - delta_eta]
    'Grid_size_in_eta': 1,  # number of the grid points in spatial rapidity direction
    'X_grid_size_in_fm': 20.0,  # spatial range along x direction in the transverse plane 
                                # [-X_grid_size_in_fm/2, X_grid_size_in_fm/2]
    'Y_grid_size_in_fm': 20.0,  # spatial range along x direction in the transverse plane 
                                # [-X_grid_size_in_fm/2, X_grid_size_in_fm/2]
    'Grid_size_in_x': 200,      # number of the grid points in x direction
    'Grid_size_in_y': 200,      # number of the grid points in y direction
    'EOS_to_use': 9,            # type of the equation of state
                                # 0: ideal gas
                                # 1: EOS-Q from azhydro
                                # 7: lattice EOS s95p-v1.2 for UrQMD
                                # 9: hotQCD EOS with UrQMD
                                # 14: neos_BQS lattice EoS at finite mu_B
                                # 17: BEST lattice EoS at finite mu_B
    # transport coefficients
    'quest_revert_strength': 10.0,         # the strength of the viscous regulation
    'Viscosity_Flag_Yes_1_No_0': 1,        # turn on viscosity in the evolution
    'Include_Shear_Visc_Yes_1_No_0': 1,    # include shear viscous effect
    'Shear_to_S_ratio': 0.12,              # value of \eta/s
    'T_dependent_Shear_to_S_ratio': 0,     # flag to use temperature dep. \eta/s(T)
    'Include_Bulk_Visc_Yes_1_No_0': 1,     # include bulk viscous effect
    'T_dependent_zeta_over_s': 7,          # parameterization of \zeta/s(T)
    'Include_second_order_terms': 1,       # include second order non-linear coupling terms
    'Include_vorticity_terms': 0,          # include vorticity coupling terms
    'Include_Rhob_Yes_1_No_0': 0,
    'turn_on_baryon_diffusion': 0,
    'kappa_coefficient': 0.4,

    # switches to output evolution information
    'output_hydro_debug_info': 0,   # flag to output debug information
    'output_evolution_data': 0,     # flag to output evolution history to file
    'output_movie_flag': 0,
    'output_evolution_T_cut': 0.145,
    'outputBinaryEvolution': 1,     # output evolution file in binary format
    'output_evolution_every_N_eta': 1,  # output evolution file every Neta steps
    'output_evolution_every_N_x':  2,   # output evolution file every Nx steps
    'output_evolution_every_N_y': 2,    # output evolution file every Ny steps
    'output_evolution_every_N_timesteps':1,  # output evolution every Ntime steps

    # parameters for freeze out and Cooper-Frye 
    'Do_FreezeOut_Yes_1_No_0': 1,       # flag to find freeze-out surface
    'Do_FreezeOut_lowtemp': 1,          # flag to include cold corona
    'freeze_out_method': 4,             # method for hyper-surface finder
                                        # 4: Cornelius
    'freeze_surface_in_binary': 1,      # switch to output surface file in binary format
    'average_surface_over_this_many_time_steps': 10,   # the step skipped in the tau
    'freeze_Ncell_x_step': 1,
    'freeze_Ncell_eta_step': 1,
    'freeze_eps_flag': 0,
    'N_freeze_out': 1,
    'eps_freeze_max': 0.18,
    'eps_freeze_min': 0.18,
    'use_eps_for_freeze_out': 1,  # find freeze-out surface 
                                  # 0: use temperature, 1: use energy density
}


# iSS
iss_dict = {
    'hydro_mode': 2,    # mode for reading in freeze out information 
    'turn_on_bulk': 0,  # read in bulk viscous pressure
    'turn_on_rhob': 0,  # read in net baryon chemical potential
    'turn_on_diff': 0,  # read in baryon diffusion current

    'include_deltaf_shear': 1,      # include delta f contribution from shear
    'include_deltaf_bulk': 0,       # include delta f contribution from bulk
    'include_deltaf_diffusion': 0,  # include delta f contribution from diffusion

    'bulk_deltaf_kind': 1,     # 0: 14-momentum approximation, 1: relaxation time approximation
    'restrict_deltaf': 0,      # flag to apply restriction on the size of delta f
    'deltaf_max_ratio': 1.0,   # the maximum allowed size of delta f w.r.t f0
    'f0_is_not_small': 1,      # include (1 \pm f_0) factor in delta f

    'randomSeed': -1,   # If <0, use system clock.
    'calculate_vn': 0,  # 1/0: whether to calculate the 
    'MC_sampling': 2,   # 0/1/2/3: whether to perform Monte-Carlo sampling
                        # (not required for spectra calculation). 
                        # 0: No sampling. 
                        # 1: use dN_dxtdetady to sample. 
                        # 2: use dN_dxtdy to sample. 
                        # 3: use dN_pTdpTdphidy to sample 
                        #    (overwrites calculate_vn to be 1). 
    'sample_upto_desired_particle_number': 0,  # 1: flag to run sampling until desired
                                               # particle numbers is reached
    'number_of_repeated_sampling': 10,         # number of repeaded sampling
    'number_of_particles_needed': 100000,      # number of hadrons to sample

    'sample_y_minus_eta_s_range': 4,    # y_minus_eta_s will be sampled
    'sample_pT_up_to': -1,  # Up to this value will pT be sampled; 
                            # if<0 then use the largest value in the pT table.
    'dN_dy_sampling_model': 30, # 30: Use Poisson distribution to sample the 
                                #      whole dN_dy.
    'dN_dy_sampling_para1': 0.16,  # Additional parameters for dN/dy sampling. 
                                   # -- For dN_dy_sampling_model==10 or 20, 

    'perform_decays': 0,             # flag to perform resonance decay
    'local_charge_conservation': 0,  # flag to impose local charge conservation
    
    'y_LB': -5.0,       # lower bound for y-sampling; 
    'y_RB': 5.0,        # upper bound for y-sampling;

    'output_samples_into_files': 0,  # output particle samples into individual files
    'store_samples_in_memory': 1,    # flag to store particle samples in memory
    'use_OSCAR_format': 1,           # output results in OSCAR format
    'use_gzip_format': 0,  # output results in gzip format (only works with
                           # store_samples_in_memory = 1)
    'calculate_vn_to_order': 9,     # v_n's are calculated up to this order
    'use_pos_dN_only': 0,           # 1: all negative emission functions will be skipped. 
    'grouping_particles': 1,  # 0/1: Particles will be re-order according to 
                              # their mass. This parameter combined with 
                              # grouping_tolerance parameter can make particles 
                              # with similar mass and chemical potentials to be 
                              # sampled together.
    'grouping_tolerance': 0.01,  # If two particles adjacent in the table have 
                                 # mass and chemical potentials close within this 
                                 # relative tolerance, they are considered to be 
                                 # identical and will be sampled successively 
                                 # without regenerating the dN / (dxt deta dy) 
                                 # matrix for efficiency.
    'minimum_emission_function_val': 1e-30,  # If dN/(dx_t deta dy) is evaluated to 
                                             # be smaller than this value, then it 
                                             # is replaced by this value.
    'use_historic_flow_output_format': 0,
    'eta_s_LB': -0.5,      # lower bound for eta_s sampling; used only when 
                           # sampling using total energy flux
    'eta_s_RB': 0.5,       # upper bound for eta_s sampling.
    'use_dynamic_maximum': 0,   # 0/1: Whether to automatically reduce the 
                                # guessed maximum after some calculations. 
                                # Work only when MC_sampling is set to 2.
    'adjust_maximum_after': 100000,  # Used only when use_dynamic_maximum=1. 
                                     # After the number of sampling given by 
                                     # this parameter the guessed maximum is 
                                     # adjusted.
    'adjust_maximum_to': 1.2,   # [1,inf]: When guessed maximum is adjusted, 
                                # it is adjusted to the "observed maximum" 
                                # multiplied by this value. Note that the 
                                # "observed maximum" is measured relative to 
                                # the guessed maximum. See code for details.
    'calculate_dN_dtau': 0,     # Output dN_dtau table. Only applicable 
                                # if MC_sampling parameter is set to 1.
    'bin_tau0': 0.6,            # used to generate bins for 
                                # calculate_dN_dtau_using_dN_dxtdeta function
    'bin_dtau': 0.2,            # used to generate bins for 
                                # calculate_dN_dtau_using_dN_dxtdeta function
    'bin_tau_max': 17.0,        # used to generate bins for 
                                # calculate_dN_dtau_using_dN_dxtdeta function
    'calculate_dN_dx': 0,       # Output dN_dx table. Only applicable 
                                # if MC_sampling parameter is set to 1.
    'bin_x_min': -10.0,         # used to generate bins for 
                                # calculate_dN_dx_using_dN_dxtdeta function
    'bin_dx': 0.5,              # used to generate bins 
                                # for calculate_dN_dx_using_dN_dxtdeta function
    'bin_x_max': 10.0,          # used to generate bins for 
                                # calculate_dN_dx_using_dN_dxtdeta function
    'calculate_dN_dphi': 0,     # Output dN_dphi table. Only applicable 
                                # if calculate_vn parameter is set to 1.
    'calculate_dN_deta':1,      # Output dN_deta table. Only applicable 
                                # if MC_sampling parameter is set to 1.
    'calculate_dN_dxt':1,       # Output dN_dxt table. Only applicable 
                                # if MC_sampling parameter is set to 1.
    'output_dN_dxtdy_4all': 0,  # Output dN_dxtdy table. Only applicable 
                                # if MC_sampling parameter is set to 2.
}


# hadronic afterburner toolkit
hadronic_afterburner_toolkit_dict = {
    'echo_level': 9,    # control the mount of print messages
    'read_in_mode': 2,  # mode for reading in particle information
                        # 0: reads outputs from OSCAR outputs
                        # 1: reads outputs from UrQMD outputs
                        # 2: reads outputs from zipped UrQMD outputs
                        # 3: reads outputs from Sangwook's UrQMD outputs 
                        #    (without header lines)
                        # 4: reads outputs from UrQMD 3.3p2 outputs
                        # 10: reads outputf from gzip outputs
    'run_mode': 0,      # running mode for the program
                        # 0: collect single particle spectra and vn
                        # 1: compute HBT correlation function
                        # 2: collect event-by-event particle yield
                        #    distribution (pT and rapdity cuts are
                        #    specified by pT_min, pT_max, rap_min,
                        #    and rap_max)
                        # 3: compute balance function
    'randomSeed': -1,
    'particle_monval': 211,     # particle Monte-Carlo number
    'distinguish_isospin': 1,   # flag whether to distinguish the isospin of particles
    'event_buffer_size': 100,       # the number of events read in at once
    'resonance_weak_feed_down_flag': 0,  # include weak feed down contribution
    'resonance_feed_down_flag': 0,  # perform resonance feed down
                                    # (will read in all hadrons and filter particle
                                    #  after decays are performed)
    'select_resonances_flag': 0,    # perform resonance decays only for selected particle species
    'resonance_weak_feed_down_Sigma_to_Lambda_flag': 0,    # include weak feed down contribution
                                                           # turn on only for Lambda (monval=3122)
                                                           # for Sigma^0 -> Lambda + gamma
    'net_particle_flag': 0,         # flag to collect net particle yield distribution
    # Parameters for single particle spectra and vn
    'order_max': 9,     # the maximum harmonic order of anisotropic flow
    'compute_correlation': 0,       # flag to compute correlation function
    'flag_charge_dependence': 0,    # flag to compute charge dependence correlation
    'npT': 41,          # number of pT points for pT-differential spectra and vn
    'pT_min': 0.05,     # the minimum value of transverse momentum (GeV)
    'pT_max': 4.05,     # the maximum value of transverse momentum (GeV)
    'rap_min': -0.5,    # minimum value of rapidity integration range for mid-rapidity observables 
    'rap_max': 0.5,     # maximum value of rapidity integration range for mid-rapidity observables 

    'rap_type': 1,      # 0: for pseudo-rapidity; 1: for rapidity
    'rapidity_distribution': 1,   # 1: output particle rapidity distribution 
    'n_rap': 101,                 # numpber of points in rapidity distr.
    'rapidity_dis_min': -5.0,     # minimum value of particle rapidity distribution
    'rapidity_dis_max': 5.0,      # maximum value of particle rapidity distribution
    'vn_rapidity_dis_pT_min': 0.20,  # the minimum value of pT for vn rap. distr.
    'vn_rapidity_dis_pT_max': 3.0,   # the maximum value of pT for vn rap. distr.

    'check_spatial_dis': 0,         # flag to check dN/dtau distribution
    'intrinsic_detas': 0.1,         # deta_s in the output samples
    'intrinsic_dtau': 0.01,         # dtau in the output samples
    'intrinsic_dx': 0.1,            # dx in the output samples
    # Parameters for HBT correlation functions
    'needed_number_of_pairs': 30000000,    # number of pairs for eack K point
    'number_of_oversample_events': 100,    # number of the combined events in the numerator
    'number_of_mixed_events': 50,          # number of the mixed events in the denorminator
    'invariant_radius_flag': 0,     # 0: compute 3D HBT correlation function
                                    # 1: compute 1D HBT correlation function for q_inv
    'azimuthal_flag': 0,            # 0: compute the azimuthal averaged HBT correlation function
                                    # 1: compute azimuthal dependent HBT correlation function
    'kT_differenitial_flag': 1,     # 0: integrate the pair momentum k_T over  a given kT range for correlation function
                                    # 1: compute the correlation function at each specifiec kT point
    'n_KT': 6,      # number of the pair momentum k_T to calculate
    'KT_min': 0.0,  # minimum value of the pair momentum k_T 
    'KT_max': 1.0,  # maximum value of the pair momentum k_T 
    'n_Kphi': 48,   # number of the azimuthal angles for the pair momentum k_T 
                    # (range is assumed to be from 0 to 2*pi)
    'Krap_min': -0.5,   # minimum accept pair momentum rapidity
    'Krap_max': 0.5,    # maximum accept pair momentum rapidity
    'buffer_rapidity': 5.0,     # collect particles with rapidity from [Krap_min - buffer_rapidity, Krap_max + buffer_rapidity]
    'qnpts': 31,    # number of points for momentum q (difference of the pair momentum) for correlaction function
    'q_min': -0.15,     # minimum value for momentum q (GeV)
    'q_max': 0.15,      # maximum value for momentum q (GeV)
    'reject_decay_flag': 0,         # reject particles from resonance decays
                                    # 0: no rejection
                                    # 1: reject particles from all decay channels
                                    # 2: reject particles only from long lived resonance decays (future)
    'tau_reject': 10.,              # reject decay particle whose tau_f > tau_reject
                                    # only effective when reject_decay_flag == 2
    # options for calculting Balance function
    'particle_alpha': 9998,     # monte carlo number for particle alpha
    'particle_beta': -9998,     # monte carlo number for particle beta
    'Bnpts': 21,                # number of bins for the balance function
    'Brap_max': 2.0,    # the maximum \Delta y rapidity for balance function
    'BpT_min': 0.2,     # the minimum pT cut for particles used in balance function
    'BpT_max': 3.0,     # the maximum pT cut for particles used in balance function
}


Parameters_list = [
    (mcglauber_dict, "input", 0),
    (music_dict, "music_input_mode_2", 2),
    (iss_dict, "iSS_parameters.dat", 1),
    (hadronic_afterburner_toolkit_dict, "parameters.dat", 1)
]

path_list = [
    '../codes/3dMCGlauber/',
    '../codes/MUSIC/',
    '../codes/iSS/',
    '../codes/hadronic_afterburner_toolkit/'
]


def update_parameters_dict(par_dict_name):
    """This function update the parameters dictionaries with user's settings"""
    parameters_dict = __import__(par_dict_name)
    initial_condition_type = (
                    parameters_dict.initial_dict['initial_state_type'])
    if initial_condition_type == "IPGlasma":
        ipglasma.update(parameters_dict.ipglasma)
        if 'Initial_profile' not in parameters_dict.music_dict:
            parameters_dict.music_dict['Initial_profile'] = 9
        if 'Initial_Distribution_input_filename' not in parameters_dict.music_dict:
            parameters_dict.music_dict[
                'Initial_Distribution_input_filename'] = (
                        'initial/epsilon-u-Hydro.dat')
        if 'boost_invariant' not in parameters_dict.music_dict:
            parameters_dict.music_dict['boost_invariant'] = 1

        if parameters_dict.music_dict['boost_invariant'] == 1:
            parameters_dict.iss_dict['hydro_mode'] = 1
        else:
            parameters_dict.iss_dict['hydro_mode'] = 2

        if 'Include_Rhob_Yes_1_No_0' not in parameters_dict.music_dict:
            parameters_dict.music_dict['Include_Rhob_Yes_1_No_0'] = 0
    else:
        mcglauber_dict.update(parameters_dict.mcglauber_dict)
        if 'Initial_profile' not in parameters_dict.music_dict:
            parameters_dict.music_dict['Initial_profile'] = 13
        if 'Initial_Distribution_input_filename' not in parameters_dict.music_dict:
            parameters_dict.music_dict[
                'Initial_Distribution_input_filename'] = 'initial/strings.dat'
        if 'boost_invariant' not in parameters_dict.music_dict:
            parameters_dict.music_dict['boost_invariant'] = 0
        parameters_dict.iss_dict['hydro_mode'] = 2
        if 'Include_Rhob_Yes_1_No_0' not in parameters_dict.music_dict:
            parameters_dict.music_dict['Include_Rhob_Yes_1_No_0'] = 1
    music_dict.update(parameters_dict.music_dict)
    iss_dict.update(parameters_dict.iss_dict)
    hadronic_afterburner_toolkit_dict.update(
        parameters_dict.hadronic_afterburner_toolkit_dict)


def update_parameters_bayesian(bayes_file):
    parfile = open(bayes_file, "r")
    for line in parfile:
        key, val = line.split()
        if key in mcglauber_dict.keys():
            mcglauber_dict[key] = float(val)
        if key in music_dict.keys():
            music_dict[key] = float(val)


def output_parameters_to_files():
    """This function outputs parameters in dictionaries to files"""
    print("\U0001F375  Output input parameter files ...")
    for idict, (parameters_dict, fname, itype) in enumerate(Parameters_list):
        f = open(fname, "w")
        for key_name in parameters_dict:
            if itype in (0, 2):
                f.write("{parameter_name}  {parameter_value}\n".format(
                    parameter_name=key_name,
                    parameter_value=parameters_dict[key_name]))
            elif itype == 1:
                f.write("{parameter_name} = {parameter_value}\n".format(
                    parameter_name=key_name,
                    parameter_value=parameters_dict[key_name]))
        if itype == 2:
            f.write("EndOfData")
        f.close()
        shutil.move(path.join(path.abspath('.'), fname),
                    path.join(path.abspath(path_list[idict]), fname))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description='\U0000269B Welcome to iEBE-MUSIC parameter master',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-par', '--par_dict', metavar='',
                        type=str, default='parameters_dict_user',
                        help='user-defined parameter dictionary filename')
    parser.add_argument('-b', '--bayes_file', metavar='',
                        type=str, default='',
                        help='parameters from bayesian analysis')
    args = parser.parse_args()
    update_parameters_dict(args.par_dict)
    if args.bayes_file != "":
        update_parameters_bayesian(args.bayes_file)
    output_parameters_to_files()
