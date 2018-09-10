import pandas
"""all the feature that is deleted is here"""
"""from charu"""

def drop_none_important_features(df):
    del df["anemia_who"]
    del df["bun"]
    del df["cl"]
    del df["co2"]
    del df["fasting"]
    del df["k"]
    del df["na"]
    del df["rdw"]
    del df["tga"]
    del df["tsh"]
    del df["wbc"]
    del df["confid_health"]
    del df["confid_instit"]
    del df["finfintot"]
    del df["finhlthtot"]
    del df["finuctot"]
    del df["fraud7"]
    del df["scam"]
    del df["gamma"]
    del df["risk"]
    del df["large_alpha"]
    del df["small_alpha"]
    del df["fin_literacy_pct"]
    del df["health_literacy_pct"]
    del df["literacy_total_pct"]
    del df["thyroid_cum"]
    del df["chf_cum"]
    del df["heart_cum"]
    del df["antibiotic_rx"]
    del df["antihyp_all_rx"]
    del df["antineoplastic_rx"]
    del df["cardiac_rx"]
    del df["dental_rx"]
    del df["dermatologic_rx"]
    del df["endocrine_rx"]
    del df["gastrointestinal_rx"]
    del df["hemotologic_rx"]
    del df["lipid_lowering_rx"]
    del df["musculoskeletal_rx"]
    del df["ophthalmic_rx"]
    del df["otic_rx"]
    del df["respiratory_rx"]
    del df["supplement_rx"]
    del df["urinary_rx"]
    del df["acetaminophen_rx"]
    del df["antiinfective_rx"]
    del df["vaccine_rx"]
    del df["antiarrhythmic_rx"]
    del df["diabetes_rx"]
    del df["antacid_rx"]
    del df["antidiarrheal_rx"]
    del df["antinausea_rx"]
    del df["antireflux_rx"]
    del df["laxative_rx"]
    del df["anticoagulant_rx"]
    del df["osteoporosis_rx"]
    del df["antiasthmatic_rx"]
    del df["antihistamine_rx"]
    del df["coughcoldallergy_rx"]
    del df["nasal_rx"]
    del df["alternative_rx"]
    del df["cartilage_base_rx"]
    del df["fish_oil_supplement_rx"]
    del df["glucosamine_rx"]
    del df["herbals_rx"]
    del df["macronutrient_rx"]
    del df["micronutrient_rx"]
    del df["mineral_rx"]
    del df["multivitamin_rx"]
    del df["nutrient_rx"]
    del df["other_dietary_rx"]
    del df["vitamin_minerals_rx"]
    del df["vitamin_rx"]
    del df["alphablocker_rx"]
    del df["benign_pros_hyper_rx"]
    del df["bphmed_rx"]
    del df["estrogen_vaginal_rx"]
    del df["urinary_antispas_rx"]
    del df["urinary_inc_rx"]
    # ==========================================================================
    del df['tot_meds_cnt'] # in the boolean section but it is not boolean
                           # instead it is presented as a sum
                           # also not marked as important, thus dropped
    return df #cleaned df

def clean_history(df):
    """
    drop the patient that has prev sickness history that might affect the
    final result of dcfdx
    from Charu
    """
    df = df[df.cancer_cum != 1]     # cancer
    df = df[df.dm_cum != 1]         # diabetes
    df = df[df.headinjrloc_cum !=1] # head injuries
    df = df[df.analgesic_rx != 1]   # analgesic_rx
    return df
