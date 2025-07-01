import pandas as pd


def standardizeColumn(col: pd.Series):
	return (col - col.mean()) / col.std()

def prepareDataset(input_csv, output_csv):
	df = pd.read_csv(input_csv)

	# ignore output column
	target_col = "loan_status"
	target = df[target_col]
	df = df.drop(columns=[target_col])

	numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
	categorical_cols = df.select_dtypes(include=['object', 'category']).columns

	# standardize numerical (minus mu divided by sigma)
	df[numeric_cols] = df[numeric_cols].apply(standardizeColumn).round(3)

	# will apply one_hot encoding to categorical values
	df = pd.get_dummies(df, columns=categorical_cols).astype(float)

	df[target_col] = target

	df.to_csv(output_csv, index=False)

prepareDataset("data/loan_data_raw.csv", "data/loan_data_prepared.csv")