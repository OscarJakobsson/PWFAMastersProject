
#import sys
#sys.path.append("~/../../Applications/VisIt.app/Contents/Resources/2.13.2/darwin-x86_64/lib/site-packages")
#sys.path.append("~/../../Applications/VisIt.app/Contents/Resources/2.13.2/darwin-x86_64/lib/python/lib/python2.7")


#import visit
#visit.Launch()


OpenDatabase("/../../Users/oscarjakobsson/The University of Manchester/Semester 7/Mphys/PWFA/SimulationData/test_run_linear_30pc/main.visit")
AddPlot("Pseudocolor", "operators/DataBinning/2D/Grid/Particles/edriver", 1, 1)
DataBinningAtts = DataBinningAttributes()
DataBinningAtts.numDimensions = DataBinningAtts.Two  # One, Two, Three
DataBinningAtts.dim1BinBasedOn = DataBinningAtts.Variable  # X, Y, Z, Variable
DataBinningAtts.dim1Var = "Grid/Particles/edriver/X"
DataBinningAtts.dim1SpecifyRange = 0
DataBinningAtts.dim1MinRange = 0
DataBinningAtts.dim1MaxRange = 1
DataBinningAtts.dim1NumBins = 200
DataBinningAtts.dim2BinBasedOn = DataBinningAtts.Variable  # X, Y, Z, Variable
DataBinningAtts.dim2Var = "Grid/Particles/edriver/Y"
DataBinningAtts.dim2SpecifyRange = 0
DataBinningAtts.dim2MinRange = 0
DataBinningAtts.dim2MaxRange = 1
DataBinningAtts.dim2NumBins = 200
DataBinningAtts.dim3BinBasedOn = DataBinningAtts.Variable  # X, Y, Z, Variable
DataBinningAtts.dim3Var = "default"
DataBinningAtts.dim3SpecifyRange = 0
DataBinningAtts.dim3MinRange = 0
DataBinningAtts.dim3MaxRange = 1
DataBinningAtts.dim3NumBins = 50
DataBinningAtts.outOfBoundsBehavior = DataBinningAtts.Clamp  # Clamp, Discard
DataBinningAtts.reductionOperator = DataBinningAtts.Count  # Average, Minimum, Maximum, StandardDeviation, Variance, Sum, Count, RMS, PDF
DataBinningAtts.varForReduction = "default"
DataBinningAtts.emptyVal = 0
DataBinningAtts.outputType = DataBinningAtts.OutputOnBins  # OutputOnBins, OutputOnInputMesh
DataBinningAtts.removeEmptyValFromCurve = 1
SetOperatorOptions(DataBinningAtts, 1)

DrawPlots()
RecenterView()



for i in range(TimeSliderGetNStates()):
  SetTimeSliderState(i)
  RecenterView()
  SaveWindow()
