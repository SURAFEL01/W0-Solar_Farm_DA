# Solar Challenge Week 0
10 Academy Week 0 Challenge: Analyzing solar farm data for Benin, Sierra Leone, and Togo.

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/SURAFEL01/W0-Solar_Farm_DA.git
   cd solar-challenge-week1
2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
5. **Run Jupyter notebooks**:
   ```bash
   jupyter notebook
7. **Run Streamlit dashboard**:
   ```bash
   streamlit run app/main.py


#Folder Structure
*.github/workflows/: GitHub Actions workflows.
*src/: Source code for reusable modules.
*notebooks/: Jupyter notebooks for EDA and analysis.
*tests/: Unit tests (to be implemented).
*scripts/: Utility scripts.
*app/: Streamlit dashboard code.

#CI/CD
*A GitHub Actions workflow (.github/workflows/ci.yml) runs on push and pull requests to ensure dependencies are installed correctly.
