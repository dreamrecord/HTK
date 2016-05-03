#!/usr/bin/python

import argparse

if __name__ == '__main__':
    
    # argparse
    parser = argparse.ArgumentParser(description='generate ProtoFile')

    parser.add_argument('-m', '--modelListPath', help='model list file path', default='modelList')
    parser.add_argument('-s', '--numOfStates', type=int, help='# of states of HMM', default=5)
    parser.add_argument('-g', '--numOfGaussians', type=int, help='# of Gaussian of a HMM state', default=5)
    parser.add_argument('-o', '--outputPath', help='output file path', default='lib/mix2_10.hed')

    args = parser.parse_args()

    startState = 2
    endState = args.numOfStates-1

    # load model list
    with open(args.modelListPath, 'r') as modelListFile:
        modelList = modelListFile.read().splitlines()

    # write to file
    with open(args.outputPath, 'w') as outputFile:
        
        for modelIndex in xrange(len(modelList)):
            outputFile.write('MU ' + str(args.numOfGaussians) + ' {' + modelList[modelIndex] + '.state[' + str(startState) + '-' + str(endState) + '].mix}\n')
