processList = {
    'p8_ee_Z_Zbb_ecm125':{},
    'p8_ee_Z_Zcc_ecm125':{},
}

inputDir  = "Events"
outputDir = "stage1"

nCPUS     = 8


class RDFanalysis():

    def analysers(df):
        df2 = (
            df
            # First using the jets as defined in the EDM4HEP file
            .Alias("Jet3","Jet#3.index")
            .Define("jet_btag", "ReconstructedParticle::getJet_btag(Jet3, ParticleIDs, ParticleIDs_0)")
            .Define("num_btag", "ReconstructedParticle::getJet_ntags(jet_btag)")
            .Define("n_recojets",  "ReconstructedParticle::get_n(Jet)")
            .Define("jet_pt",  "ReconstructedParticle::get_pt(Jet)")
            .Define("selected_jets", "ReconstructedParticle::sel_pt(5.)(Jet)")
            .Define("jet_e",  "ReconstructedParticle::get_e(Jet)")
            .Define("jet_eta",  "ReconstructedParticle::get_eta(Jet)")
            .Define("jet_mass",  "ReconstructedParticle::get_mass(Jet)")
            .Define("jet_reso",  "ReconstructedParticle::resonanceBuilder(91)(selected_jets)")
            .Define("jet_reso_mass","ReconstructedParticle::get_mass(jet_reso)")
        )
        return df2


    def output():
        branchList = [
            "n_recojets",
            "jet_pt",
            "jet_e",
            "jet_eta",
            "jet_mass",
            "jet_btag",
            "num_btag",
            "jet_reso_mass"
        ]
        return branchList
