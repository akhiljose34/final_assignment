import pandas as pd
pd.set_option("display.max_columns", 50)
pd.set_option('display.max_rows', 500)
survey_file_input = "survey.csv"
raw_df = pd.read_csv(survey_file_input)
print(raw_df)
viz = raw_df [["Age", "Gender", "Country","supervisor", "state","self_employed", "remote_work", "tech_company","family_history", "treatment", "mental_health_consequence","phys_health_consequence"]]
print (viz)
viz.loc[(viz['supervisor']).isin((['Yes', 'Some of them'])), "family_history"] = "Yes"
viz.loc[(viz['mental_health_consequence'].isin(['Yes', 'Maybe'])), "mental_health_consequence"] = "Yes"
Lg_female = ["female", "Cis Female", "F", "Woman", "4"]
Lg_male = ["W", "male", "e", "Male-ish", "maile", "Cis Male", "Mal", "Male (CIS)"]
Lg_nonbinary = ["Trans-female", "something kinda male?", "queer/she/they 'non-binary"]
viz.loc[(viz['Gender'].isin(Lg_female)), "Gender"] = "Female"
viz.loc[(viz['Gender'].isin(Lg_male)), "Gender"] = "male"
viz.loc[(viz['Gender'].isin(Lg_nonbinary)), "Gender"] = "nonbinary"

print(viz['Gender'].unique())