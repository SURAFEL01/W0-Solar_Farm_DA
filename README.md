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


## Folder Structure
```
   W0-Solar_Farm_DA/
   │
   ├── .github/workflows/     # GitHub Actions CI/CD workflows
   ├── src/                   # Core Python modules (reusable logic)
   ├── notebooks/             # Jupyter notebooks for EDA and data analysis
   ├── tests/                 # Unit tests (TBD)
   ├── scripts/               # Utility or data prep scripts
   ├── app/                   # Streamlit dashboard source code
   ├── requirements.txt       # Python dependencies
   └── README.md              # Project overview
```
   


## CI/CD with GitHub Actions

*A CI/CD pipeline is implemented using GitHub Actions to automate environment setup and dependency installation checks.*

* **Path**:  
  `.github/workflows/ci.yml`

* **Triggers**:  
  Runs on every:
  * `push`
  * `pull request`

* **Purpose**:  
  Ensures that:
  * The environment is set up correctly  
  * Dependencies install without issues

* **Example workflow**:
  ```yaml
  name: CI

  on: [push, pull_request]

  jobs:
    build:
      runs-on: ubuntu-latest

      steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt

      - name: Test environment
        run: echo "Environment setup successful!"




