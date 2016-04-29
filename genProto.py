#!/usr/bin/python

import argparse

if __name__ == '__main__':
    
    # argparse
    parser = argparse.ArgumentParser(description='generate ProtoFile')

    parser.add_argument('-s', '--numOfStates', type=int, help='# of states of HMM', default=5)
    parser.add_argument('-o', '--outputPath', help='output file path', default='lib/proto')

    args = parser.parse_args()

    # write to file
    with open(args.outputPath, 'w') as outputFile:
        
        outputFile.write('~o <VECSIZE> 39 <MFCC_Z_E_D_A>\n')
        outputFile.write('~h \"proto\"\n')
        outputFile.write('<BeginHMM>\n')
        outputFile.write('<NumStates> ' + str(args.numOfStates))
        
        # Gaussian init for each states
        for state in xrange(2, args.numOfStates):
            
            outputFile.write('\n<State> ' + str(state))

            outputFile.write('\n<Mean> 39\n')
            
            for i in xrange(39):
                outputFile.write(str(0.0) + ' ')

            outputFile.write('\n<Variance> 39\n')

            for i in xrange(39):
                outputFile.write(str(1.0) + ' ')

        # transition probability init
        outputFile.write('\n<TransP> ' + str(args.numOfStates) + '\n')
        
        outputFile.write('0.0 1.0 ')
        
        for i in xrange(args.numOfStates-2):
            outputFile.write(str(0.0) + ' ')

        outputFile.write('\n')

        for i in xrange(1, args.numOfStates-1):
            
            for j in xrange(args.numOfStates):

                if j == i or j == i+1:
                    outputFile.write(str(0.5) + ' ')
                else:
                    outputFile.write(str(0.0) + ' ')

            outputFile.write('\n')

        for i in xrange(args.numOfStates):
            outputFile.write(str(0.0) + ' ')

        # finish
        outputFile.write('\n<EndHMM>\n')
