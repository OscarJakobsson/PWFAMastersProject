
#import sys
#sys.path.append("~/../../Applications/VisIt.app/Contents/Resources/2.13.2/darwin-x86_64/lib/site-packages")
#sys.path.append("~/../../Applications/VisIt.app/Contents/Resources/2.13.2/darwin-x86_64/lib/python/lib/python2.7")


#import visit
#visit.Launch()


OpenDatabase("/../../Users/oscarjakobsson/The University of Manchester/Semester 7/Mphys/PWFA/SimulationData/test_run_linear_30pc/main.visit")
DefineScalarExpression("weightedEnergy", "<Particles/Ek/edriver>*<Particles/Weight/edriver>")
AddPlot("Histogram", "Grid/Particles/edriver/X", 1, 1)
HistogramAtts = HistogramAttributes()
HistogramAtts.basedOn = HistogramAtts.ManyZonesForSingleVar  # ManyVarsForSingleZone, ManyZonesForSingleVar
HistogramAtts.histogramType = HistogramAtts.Variable  # Frequency, Weighted, Variable
HistogramAtts.weightVariable = "weightedEnergy"
HistogramAtts.limitsMode = HistogramAtts.OriginalData  # OriginalData, CurrentPlot
HistogramAtts.minFlag = 0
HistogramAtts.maxFlag = 0
HistogramAtts.min = 0
HistogramAtts.max = 1
HistogramAtts.numBins = 100
HistogramAtts.domain = 0
HistogramAtts.zone = 0
HistogramAtts.useBinWidths = 1
HistogramAtts.outputType = HistogramAtts.Curve  # Curve, Block
HistogramAtts.lineStyle = HistogramAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
HistogramAtts.lineWidth = 2
HistogramAtts.color = (0, 0, 0, 255)
HistogramAtts.dataScale = HistogramAtts.Linear  # Linear, Log, SquareRoot
HistogramAtts.binScale = HistogramAtts.Linear  # Linear, Log, SquareRoot
HistogramAtts.normalizeHistogram = 0
HistogramAtts.computeAsCDF = 0
SetPlotOptions(HistogramAtts)


for i in range(TimeSliderGetNStates()):
	SetTimeSliderState(i)
	DrawPlots()
	RecenterView()
	Query("Integrate")

	print "%g" % GetQueryOutputValue()






