
processList = {
    'p8_ee_Z_Zbb_ecm125':{},
    'p8_ee_Z_Zcc_ecm125':{},
}
#Input directory where the files produced at the pre-selection level are
inputDir  = "stage1"

#Input directory where the files produced at the pre-selection level are
outputDir  = "final"

nCPUS     = 8

#Link to the dictonary that contains all the cross section informations etc...
procDict = "../GenScripts/FCCee_procDict_spring2021_IDEA.json"

#produces ROOT TTrees, default is False
doTree = True

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {"sel0":"n_recojets>=0",
           "sel1":"num_btag>0"}
#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {
    "jet_pt":{"name":"jet_pt","title":"Jet P_{T} [GeV]","bin":25,"xmin":0,"xmax":100},
    "jet_e":{"name":"jet_e","title":"Jet energy [GeV]","bin":25,"xmin":0,"xmax":100},
    "jet_eta":{"name":"jet_eta","title":"Jet #eta","bin":15,"xmin":-3,"xmax":3},
    "jet_mass":{"name":"jet_mass","title":"Jet Mass [GeV]","bin":25,"xmin":0,"xmax":100},
    "n_recojets":{"name":"n_recojets","title":"Number of jets","bin":10,"xmin":0,"xmax":10},
    "jet_btag":{"name":"jet_btag","title":"btag jets","bin":10,"xmin":0,"xmax":10},
    "num_btag":{"name":"num_btag","title":"Number of b jets","bin":10,"xmin":0,"xmax":10},
    "jet_reso_mass":{"name":"jet_reso_mass","title":"#M_jj [GeV]","bin":20,"xmin":40,"xmax":120},
    "jets_reso_eekt_mass":{"name":"jets_reso_eekt_mass","title":"#M_jj [GeV]","bin":20,"xmin":40,"xmax":120},
    "sel_jets_pt":{"name":"sel_jets_pt","title":"Jet P_{T} [GeV]","bin":25,"xmin":0,"xmax":100},

}
