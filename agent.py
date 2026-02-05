import pandas as pd

class DataAnalysisAgent:

    def analyze(self, df):
        result = {}

        result["rows"] = df.shape[0]
        result["columns"] = df.shape[1]
        result["column_names"] = list(df.columns)
        result["missing_values"] = df.isnull().sum()

        result["summary"] = df.describe(include="all")

        numeric_cols = df.select_dtypes(include="number").columns
        result["numeric_columns"] = numeric_cols

        insights = []
        for col in numeric_cols:
            insights.append(
                f"{col}: max={df[col].max()}, min={df[col].min()}, avg={df[col].mean():.2f}"
            )

        result["insights"] = insights

        return result
