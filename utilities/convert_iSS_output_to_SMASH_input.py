def charge(pdg):
    s = str(pdg)
    antiparticle_sign = 1
    if s[0] == '-':
        s = s[1:]
        antiparticle_sign = -1
    # photon
    if (s == '22'): return 0
    # nuclei
    if  (len(s) == 10 and s[0:2] == '10'):
        return int(s[-7:-5]) * antiparticle_sign 
    quarks = ('000'+ s)[-4:-1]
    # lepton
    if quarks[0] == '0' and quarks[1] == '0':
        return -1
    # meson
    if quarks[0] == '0':
        if (int(quarks[1]) % 2 == int(quarks[2]) % 2):
            return 0
        else:
            return antiparticle_sign
    # baryon
    Q = 0
    for i in quarks:
        Q += (2 if (int(i) % 2 == 0) else -1)
    return Q / 3 * antiparticle_sign

def convert_iSS_output_to_SMASH_input(iSS_file, SMASH_folder):
    print "# Reading particles from ", input_file
    out_fname = "/sampled_particles"
    out_file_counter = 0
    events_per_file = 20
    output_file = open(SMASH_folder + out_fname + str(out_file_counter), 'w')
    output_file.write("#!OSCAR2013 particle_lists t x y z mass p0 px py pz pdg ID charge\n"
                      "# Units: fm fm fm fm GeV GeV GeV GeV GeV none none e\n"
                      "# SMASH\n")
    with open(iSS_file, 'r') as f:
        # header
        for _ in xrange(3): f.readline()
        line = f.readline()
        while True:
            ev_number, npart, _, _ = [int(s) for s in line.split()]
            output_file.write('# event %d in %d\n' % (ev_number % events_per_file, npart))
            if (ev_number % 1000 == 0):
                print ev_number, npart
            for i in xrange(npart):
                line = f.readline()
                n, pdg, px, py, pz, E, m, x, y, z, t = [float(s) for s in line.split()]
                ipdg = int(pdg)
                # Some particles are not represented by pdg code convention and need special treatment
                if (ipdg in [2110, 2210, 12110, 12210]):
                    ipdg += 19920009
                output_file.write('%10.4f %10.4f %10.4f %10.4f %10.4f %13.8f %13.8f %13.8f %13.8f %d %d %d\n' % \
                                  (t, x, y, z, m, E, px, py, pz, ipdg, n, charge(ipdg)))
            line = f.readline()
            if (line):
                output_file.write('# event %d end 0 impact 0\n' % (ev_number % events_per_file))
                if ((ev_number + 1) % events_per_file == 0):
                    output_file.close()
                    out_file_counter += 1
                    output_file = open(SMASH_folder + out_fname + str(out_file_counter), 'w')
            else:
                break
    output_file.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
            description='Converter from iSS output to SMASH particles list input',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input_file',
                        type=str, default='OSCAR.DAT',
                        help='file with sampled particles from iSS')
    parser.add_argument('-o', '--output_folder', type=str,
                        default='SMASH_input', help='folder with SMASH events')
    args = parser.parse_args()
    try:
        input_file = args.input_file
        output_folder = args.output_folder
    except:
        parser.print_help()
        exit(0)

    convert_iSS_output_to_SMASH_input(input_file, output_folder)
