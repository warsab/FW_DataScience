# 📊 FW Utils

**Author:** Warrick Sabatta  
**Version:** 0.1  
**Description:**  
A modular, user-friendly Python utility library for data analysts and data scientists 🧠.  
It includes functions for data extraction, styling, visualization, and diagnostics — all in one compact package.

---

## 📁 Project Structure
```
fw_utils/
│
├── extractors.py # 🔢 Functions to extract values (e.g., numbers from strings)
├── styling.py # 🎨 DataFrame styling helpers
├── visualization.py # 📈 Correlation, scatter, outliers, and dist plots
├── diagnostics.py # 🧪 Missing value reporting and diagnostics
└── init.py # Makes this a Python package  
```

---

## 🚀 Installation

### Option 1: Clone from GitHub

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
pip install -e .
```

### Option 2: Copy into your project
Just copy the fw_utils/ folder into your project and use it directly!  

## 🧩 Usage Examples  
# Importing functions from modules
from fw_utils.extractors import extract_nr
from fw_utils.styling import make_pretty, view_df
from fw_utils.visualization import corr_plot, scatter_plot
from fw_utils.diagnostics import missing_values

# Example usage
```
df['amount'] = df['description'].apply(extract_nr)  # Extract numbers from text
make_pretty(df)                                     # Style a table
corr_plot(df)                                       # Show correlation matrix
missing_values(df)                                  # See missing data summary
```
## 📦 Dependencies
Make sure you have these packages installed (automatically handled with pip install -e .):
- pandas
- numpy
- plotly
- IPython

Optional for diagnostics:
- matplotlib
- seaborn
- scikit-learn

## 🖼 Logo Support
Some functions (e.g., scatter_plot, missing_values, etc.) accept a logo_path parameter.

To include your brand/logo:
```
scatter_plot(df, target="price", columns=["area"], logo_path="logo.png")

```
## 💡 Why Use FW Utils?
- Modular and easy to use
- Jupyter/Fabric/Databricks/VSC notebook–friendly
- Visual-first: leverages Plotly and Pandas styling
- Boost your analysis & reporting with clean, consistent visuals

## 👨‍💻 Contributing
Pull requests are welcome! Feel free to fork and enhance the tool with new modules or fixes.  

## 📝 License
MIT License © 2025 Warrick Sabatta

