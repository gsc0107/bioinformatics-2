'''
Creates an abundance matrix given p-value adjusted FIMO --text output. 
'''

import argparse
import copy

def get_motifs(fname):
    ''' 
    Gets all available motifs within a FIMO output file.
    @param fname: Input FIMO filename.
    '''
    motifs = {}
    for linenum, i in enumerate(open(fname)):
        if linenum > 0:
            i = i.strip().split('\t')
            m = i[0]
            if m not in motifs:
                motifs[m] = 0 # each motif references 
    return motifs

def get_identifiers(fname):
    ''' 
    Gets all available identifiers within a FIMO output file.
    @param fname: Input FIMO filename.
    '''
    ids = {}
    motifs = get_motifs(fname)
    for linenum, i in enumerate(open(fname)):
        if linenum > 0:
            i = i.strip().split('\t')
            accn = i[1]
            if accn not in ids:
                ids[accn] = copy.deepcopy(motifs) # K => motif, V => counts
    return ids # return collection

def build_matrix(fname):
    ''' 
    Builds a matrix given a p-value adjusted set of TFBS mappings generated
    from FIMO.
    @param fname: Input FIMO filename. 
    '''
    ids = get_identifiers(fname)
    for i in ids:
        print(i, ids[i])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', metavar='FILE', required=True,
                        help='p-value adjusted from FIMO using --text mode [na]')
    args = vars(parser.parse_args())
    build_matrix(fname = args['i'])
    