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

            .Define("RP_px",          "ReconstructedParticle::get_px(ReconstructedParticles)")
            .Define("RP_py",          "ReconstructedParticle::get_py(ReconstructedParticles)")
            .Define("RP_pz",          "ReconstructedParticle::get_pz(ReconstructedParticles)")
            .Define("RP_phi",          "ReconstructedParticle::get_phi(ReconstructedParticles)")
            .Define("RP_e",           "ReconstructedParticle::get_e(ReconstructedParticles)")
            .Define("RP_m",           "ReconstructedParticle::get_mass(ReconstructedParticles)")
            .Define("RP_q",           "ReconstructedParticle::get_charge(ReconstructedParticles)")

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

            .Define("pseudo_jets",    "JetClusteringUtils::set_pseudoJets(RP_px, RP_py, RP_pz, RP_e)")


            .Define("FCCAnalysesJets_eekt1", "JetClustering::clustering_ee_kt(2, 2, 1, 0)(pseudo_jets)")
            .Define("jets_eekt1","JetClusteringUtils::get_pseudoJets(FCCAnalysesJets_eekt1)")
            .Define("jets_reso_eekt", "JetClusteringUtils::resonanceBuilder(91)(jets_eekt1)")
            .Define("jets_reso_eekt_mass", "JetClusteringUtils::get_m(jets_reso_eekt)")

            .Define("sel_jets", "JetClusteringUtils::sel_pt(10.)(jets_eekt1)")

            .Define("sel_jets_pt", "JetClusteringUtils::get_pt(sel_jets)")

            #.Define("jets_reso_eekt", "JetClusteringUtils::recoilbuilder::recoilbuilder(jets_eekt1)")

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
            "jet_reso_mass",
            "jets_reso_eekt_mass",
            "sel_jets_pt"
        ]
        return branchList
