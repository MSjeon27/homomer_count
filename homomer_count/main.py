import argparse
import codecs

def main():

    parser = argparse.ArgumentParser(description=(
        ""
        ))
    parser.add_argument('inp', metavar='i', help="Input file")
    parser.add_argument('-b', '--basenum', metavar='b', default=5, help="The number of continuous base number")
    parser.add_argument('-o', '--out', metavar='o', default='homomer_count.txt', help="Output file name")
    args = parser.parse_args()

    # read gzip file
    reader = codecs.getreader("utf-8")

    # Set definition to use different caculation by the type of input file (.fa or .fq)
    # Calculation for fasta file
    def honum_fa(fasta):
        with open(fasta, "r") as f:
            Anum = 0
            Tnum = 0
            Gnum = 0
            Cnum = 0
            for tig in f.read().split('>')[1:]:
                seq = ''.join(tig.split('\n')[1:])
                tmer = len(seq) - 4
                for p in range(tmer):
                    subseq = seq[p:p+5]
                    if subseq == 'AAAAA':
                        Anum = Anum + 1
                    elif subseq == 'TTTTT':
                        Tnum = Tnum + 1
                    elif subseq == 'GGGGG':
                        Gnum = Gnum + 1
                    elif subseq == 'CCCCC':
                        Cnum = Cnum + 1
                    else:
                        pass
        return Anum, Tnum, Gnum, Cnum

    # Calculation for fastq file
    def honum_fq(fastq):
        #f = reader(gzip.open(fastq, 'rb'))
        with open(fastq, "r") as f:
            Anum = 0
            Tnum = 0
            Gnum = 0
            Cnum = 0
            n = 0
            for line in f.readlines():
                n += 1
                try:
                    str(line[0].upper())
                    if str(line[0].upper()) in ['A', 'T', 'G', 'C']:
                        tmer = len(line.rstrip()) - 4
                        for p in range(tmer):
                            subseq = line.rstrip()[p:p+5]
                            if subseq == 'AAAAA':
                                Anum = Anum + 1
                            elif subseq == 'TTTTT':
                                Tnum = Tnum + 1
                            elif subseq == 'GGGGG':
                                Gnum = Gnum + 1
                            elif subseq == 'CCCCC':
                                Cnum = Cnum + 1
                            else:
                                pass
                except AttributeError:
                    pass
            return Anum, Tnum, Gnum, Cnum


    # Set output format
    out_list = []
    outfmt = """
    -----------homomer number count result-----------
    Input file: {}
    Continous base number: {}
    A homomer: {}
    T homomer: {}
    G homomer: {}
    C homomer: {}
    total: {}
    """

    with open(args.inp, 'r') as ipf:
        try:
            for l in ipf.readlines():
                # Check the type of input file
                if l.startswith('>'):
                    A, T, G, C = honum_fa(args.inp)
                    out_list.extend([A, T, G, C])
                else:
                    A, T, G, C = honum_fq(args.inp)
                    out_list.extend([A, T, G, C])
        except UnicodeDecodeError:
            A, T, G, C = honum_fq(args.inp)
            out_list.extend([A, T, G, C])

    # Generate output file
    with open(args.out, 'w') as otf:
        A = out_list[0]
        T = out_list[1]
        G = out_list[2]
        C = out_list[3]
        otf.write(outfmt.format(args.inp, args.basenum, A, T, G, C, A + T + G + C))