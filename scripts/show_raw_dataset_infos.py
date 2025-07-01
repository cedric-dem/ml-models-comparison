import pandas as pd

def detectColumnTypes(file_path):
	df = pd.read_csv(file_path)

	for column in df.columns:
		dtype = df[column].dtype
		print("====> Column name "+column)

		if pd.api.types.is_integer_dtype(dtype) or pd.api.types.is_float_dtype(dtype):
			# is numerical value
			print("Numerical")
			print("Min     : "+str(round(df[column].min(),2)))
			print("Average : "+str(round(df[column].mean(),2)))
			print("Std     : "+str(round(df[column].std(),2)))
			print("Median : "+str(round(df[column].median(),2)))
			print("Max     : "+str(round(df[column].max(),2)))

		else:
			#is categorical column
			print("Categorical")
			uniques = df[column].dropna().unique()

			proportions = df[column].value_counts(normalize=True)
			print("Possible Values  : (",len(uniques), ") ")


			for val, prop in proportions.items():
				print(str(val) + " [ "+ str(round(prop * 100, 2))+" %] ", end=" ")  
			print()
		print("----")

detectColumnTypes("data/loan_data_raw.csv")
