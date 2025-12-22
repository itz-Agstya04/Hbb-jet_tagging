FEATURE_COLS = [
    "fj_pt",
    "fj_sdmass",
    "fj_sdn2",
    "fj_n_sdsubjets",
    "fj_tau1",
    "fj_tau2",
    "fj_tau3",
    "fj_ptDR",
    "fj_relptdiff",
    "fj_jetNTracks",
    "fj_nSV",
    "fj_sdsj1_pt",
    "fj_sdsj1_mult",
    "fj_sdsj1_ptD",
    "fj_mass",
    "fj_eta",
    "fj_phi",
    "fj_sdsj1_eta",
    "fj_sdsj1_mass",
    "tau21",
    "tau32",
]

LABEL_COL = "label_H_bb"


def add_tau_features(df):
    df = df.copy()
    df["tau21"] = df["fj_tau2"] / df["fj_tau1"]
    df["tau32"] = df["fj_tau3"] / df["fj_tau2"]
    return df
