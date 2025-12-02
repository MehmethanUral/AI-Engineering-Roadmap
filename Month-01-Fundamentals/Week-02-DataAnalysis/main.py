import pandas as pd
import numpy as np
import os

class DataAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
    
    def create_dummy_data(self):
        print(f"⚠️ '{self.file_path}' not found. Generating sample data...")
              
        data = {
            "Student_ID": range(1, 21),
            "Math": np.random.randint(40, 100, 20),
            "Physics": np.random.randint(30, 95,20),
            "Chemistry": np.random.randint(50, 100, 20),
            "Working_Hours": np.random.uniform(1.5, 10.0, 20).round(1)    
        }

        self.df = pd.DataFrame(data)
        self.df.to_csv(self.file_path, index=False)
        print(f"✅ '{self.file_path}' created successfully!\n")

    def load_data(self):
        if not os.path.exists(self.file_path):
            self.create_dummy_data()
        else:
            self.df = pd.read.csv(self.file_path)
            print(f"📂 Data loaded: {self.file_path}\n")
    
    def show_preview(self):
        if self.df is not None:
            print("--- 📊 Data Preview (First 5 Rows) ---")
            print(self.df.head())
            print("\n--- ℹ️ Dataset Information ---")
            print(self.df.info())
            print("-" *40)

    def calculate_statistics(self):
        if self.df is not None:
            print("\n--- 📈 Statistical Analysis ---")

            desc = self.df.describe().T
            
            desc["median"] = self.df.median(numeric_only=True)
            
            print(desc[["mean", "median", "std", "min", "max"]])
            print("-" *40)

def main():
    print("--- 🐼 Pandas Data Analysis Tool ---")

    file_name = "student_scores.csv"

    analyzer = DataAnalyzer(file_name)

    analyzer.load_data()
    analyzer.show_preview()
    analyzer.calculate_statistics()

if __name__ == "__main__":
    main()