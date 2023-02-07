export FCCDICTSDIR=$PWD
fccanalysis run analysis_stage1.py --output p8_ee_Z_Zbb_ecm125.root --files-list Events/p8_ee_Z_Zbb_ecm125.root
fccanalysis run analysis_stage1.py --output p8_ee_Z_Zcc_ecm125.root --files-list Events/p8_ee_Z_Zcc_ecm125.root
fccanalysis final analysis_final.py
fccanalysis plots analysis_plots.py
