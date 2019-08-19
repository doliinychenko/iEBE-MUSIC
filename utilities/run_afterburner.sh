#!/bin/bash -l
#SBATCH --qos=debug
#SBATCH -N 1
#SBATCH -J afterburner
#SBATCH -t 30:00
#SBATCH -L SCRATCH
#SBATCH -C haswell
#SBATCH --mail-type=ALL
#SBATCH --mail-user=doliinychenko@lbl.gov

SMASH_ROOT=~/smash-devel/
UTILITIES=~/iEBE-MUSIC/utilities
ISS_ROOT=./SMASH_0/iSS

mv UrQMDev_0 SMASH_0
# provide SMASH particle table to iSS
${SMASH_ROOT}/build/smash -x -i ${UTILITIES}/config.yaml > ${ISS_ROOT}/iSS_tables/pdg.dat
python ${UTILITIES}/prepare_SMASH_particles_for_iSS.py -i ${ISS_ROOT}/iSS_tables/

cd ${ISS_ROOT}
mkdir -p results
cp ../hydro_event/surface*.dat results/surface.dat
cp ../hydro_event/music_input results/music_input
./iSS.e
mkdir -p SMASH_input && rm -rf SMASH_input/*
mkdir -p SMASH_results && rm -r SMASH_results/*
python ${UTILITIES}/convert_iSS_output_to_SMASH_input.py -i OSCAR.DAT -o SMASH_input/
npr=`nproc`
for (( i=1; i<=$npr; i++ ))
do
    mkdir -p SMASH_results/${i}
    ${SMASH_ROOT}/build/smash -i ${UTILITIES}/config.yaml \
    	                  -o SMASH_results/${i} \
    	                  -c "Modi: {List: {File_Directory: SMASH_input/}}" \
    	                  -c "Modi: {List: {File_Prefix: sampled_particles}}" \
    		          -c "Modi: {List: {Shift_Id: ${i}}}" > SMASH_results/${i}/out.txt &
done
wait
python ~/smash-analysis/test/energy_scan/mult_and_spectra.py \
    --input_files SMASH_results/*/particles_binary.bin \
    --output_files yspectra.txt mtspectra.txt ptspectra.txt v2.txt meanmt0_midrapidity.txt meanpt_midrapidity.txt midrapidity_yield.txt total_multiplicity.txt
