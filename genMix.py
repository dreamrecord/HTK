#!/usr/bin/python

import argparse

if __name__ == '__main__':
    
    # argparse
    parser = argparse.ArgumentParser(description='generate ProtoFile')

    parser.add_argument('-s', '--numOfStates', type=int, help='# of states of HMM', default=5)
    parser.add_argument('-g', '--numOfGaussians', type=int, help='# of Gaussian of a HMM state', default=5)
    parser.add_argument('-o', '--outputPath', help='output file path', default='lib/mix2_10.hed')

    args = parser.parse_args()

    startState = 2
    endState = args.numOfStates-1

    modelList = ['liN', '#i', '#er', 'san', 'sy', '#u', 'liou', 'qi', 'ba', 'jiou', 'sil']

    # write to file
    with open(args.outputPath, 'w') as outputFile:
        
        for modelIndex in xrange(len(modelList)):
            outputFile.write('MU ' + str(args.numOfGaussians) + ' {' + modelList[modelIndex] + '.state[' + str(startState) + '-' + str(endState) + '].mix}\n')
