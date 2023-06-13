import camelot
input_pdf = camelot.read_pdf('india_factsheet_economic_n_hdi.pdf',flavor='lattice',pages='1,2')
print(input_pdf[2].df)

df = input_pdf[2].df.loc[11:14, 1:3]
df = df.reset_index(drop = True)
df.columns = ["KPI", "2001", "2011"]
df.loc[:, ["2001", "2011"]] = df.loc[:, ["2001", "2011"]].astype(float)
df.to_csv("packt_output.csv")
df.to_excel("packt_output_excel.xlsx")