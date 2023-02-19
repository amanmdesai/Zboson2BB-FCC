import ROOT

# global parameters
intLumi        = 5.0e+06 #in pb-1
ana_tex        = 'e^{+}e^{-} #rightarrow Z'
delphesVersion = '3.4.2'
energy         = 240.0
collider       = 'FCC-ee'
inputDir       = 'final/'
formats        = ['png','pdf']
yaxis          = ['lin','log']
stacksig       = ['stack','nostack']
outdir         = 'plots/'

variables =   ["n_recojets",
            "jet_pt",
            "jet_e",
            "jet_eta",
            "jet_mass",
            "jet_btag",
            "num_btag",
            "jet_reso_mass",
            "jets_reso_eekt_mass",
            "sel_jets_pt"]

###Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['Zbb']   = ["sel0","sel1"]

extralabel = {}
extralabel['sel0'] = "Selection: n_jets >= 2"
extralabel['sel1'] = "Selection: n_btag > 1"

colors = {}
colors['Zbb'] = ROOT.kRed
colors['Zcc'] = ROOT.kBlue

plots = {}
plots['Zbb'] = {'signal':{'Zbb':['p8_ee_Z_Zbb_ecm125']},
               'backgrounds':{'Zcc':['p8_ee_Z_Zcc_ecm125']}}

legend = {}
legend['Zbb'] = 'Z #rightarrow bb'
legend['Zcc'] = 'Z #rightarrow cc'
