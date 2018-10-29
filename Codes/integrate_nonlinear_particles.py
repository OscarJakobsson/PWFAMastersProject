
#import sys
#sys.path.append("~/../../Applications/VisIt.app/Contents/Resources/2.13.2/darwin-x86_64/lib/site-packages")
#sys.path.append("~/../../Applications/VisIt.app/Contents/Resources/2.13.2/darwin-x86_64/lib/python/lib/python2.7")


#import visit
#visit.Launch()


OpenDatabase("/../../Users/oscarjakobsson/The University of Manchester/Semester 7/Mphys/PWFA/SimulationData/test_run_nonlinear_30pc/main.visit")
DefineScalarExpression("weightedEnergy", "<Particles/Ek/edriver>*<Particles/Weight/edriver>")
AddPlot("Histogram", "Grid/Particles/edriver/X", 1, 1)
HistogramAtts = HistogramAttributes()
HistogramAtts.basedOn = HistogramAtts.ManyZonesForSingleVar  # ManyVarsForSingleZone, ManyZonesForSingleVar
HistogramAtts.histogramType = HistogramAtts.Variable  # Frequency, Weighted, Variable
HistogramAtts.weightVariable = "Particles/Weight/edriver"
HistogramAtts.limitsMode = HistogramAtts.OriginalData  # OriginalData, CurrentPlot
HistogramAtts.minFlag = 0
HistogramAtts.maxFlag = 0
HistogramAtts.min = 0
HistogramAtts.max = 1
HistogramAtts.numBins = 32
HistogramAtts.domain = 0
HistogramAtts.zone = 0
HistogramAtts.useBinWidths = 1
HistogramAtts.outputType = HistogramAtts.Block  # Curve, Block
HistogramAtts.lineStyle = HistogramAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
HistogramAtts.lineWidth = 0
HistogramAtts.color = (200, 80, 40, 255)
HistogramAtts.dataScale = HistogramAtts.Linear  # Linear, Log, SquareRoot
HistogramAtts.binScale = HistogramAtts.Linear  # Linear, Log, SquareRoot
HistogramAtts.normalizeHistogram = 0
HistogramAtts.computeAsCDF = 0
SetPlotOptions(HistogramAtts)
DrawPlots()
Query("Integrate")

for i in range(TimeSliderGetNStates()/34):
	SetTimeSliderState(i*34)
	DrawPlots()
	RecenterView()
	Query("Integrate")

	print "%g" % GetQueryOutputValue()






