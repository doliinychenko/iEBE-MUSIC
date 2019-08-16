if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
            description='Prepare SMASH particles list to be sampled with iSS',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--iss_tables_folder', type=str,
                        default='', help='folder, where iSS holds tables')
    args = parser.parse_args()
    try:
        iss_tables_folder = args.iss_tables_folder
    except:
        parser.print_help()
        exit(0)
    
    input_file_name = iss_tables_folder + '/pdg.dat'
    output_file_name = iss_tables_folder + '/chosen_particles.dat'
    infile = open(input_file_name, 'r')
    outfile = open(output_file_name, 'w')
    while (True):
        line = infile.readline()
        if (not line): break
        line_split = line.split()
        pdg = line_split[0]
        ndecays = int(line_split[-1])
        mass = float(line_split[2])
        for _ in xrange(ndecays): infile.readline()
        if (mass > 0.1 and mass < 2.5):
            outfile.write(pdg + '\n')
    infile.close()
    outfile.close()
