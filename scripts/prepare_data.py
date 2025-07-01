import pandas as pd


def standardizeColumn(col: pd.Series):
	return (col - col.mean()) / col.std()

def prepareDataset(input_csv, output_csv):
	df = pd.read_csv(input_csv)

	target_col = "loan_status"
	target = df[target_col]
	df = df.drop(columns=[target_col])

	numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
	categorical_cols = df.select_dtypes(include=['object', 'category']).columns

	df[numeric_cols] = df[numeric_cols].apply(standardizeColumn)

	df = pd.get_dummies(df, columns=categorical_cols).astype(float).round(3)

	df[target_col] = target

	df.to_csv(output_csv, index=False)

prepareDataset("data/loan_data_raw.csv", "data/loan_data_prepared.csv")