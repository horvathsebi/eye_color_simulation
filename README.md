## Overview
This project simulates the evolution of **eye color** in a population over multiple generations using **probabilistic modeling** and **Monte Carlo simulations**.  
It explores how genetic inheritance affects the distribution of brown, blue, and green eyes over time.

---

## Project Structure
- `eyecolors.py` — contains all main functions for simulating populations, generating offspring, and running simulations across generations
- `teszter.ipynb` — Jupyter Notebook used to test and run the functions from `eyecolors.py`
- `monte_carlo.xlsx` - Excel file to store the results from over numerous runs
- `README.md` — project description

---

## Features
- Simulates a population of individuals with alleles determining eye color
- Models inheritance rules for brown, green, and blue eyes
- Generates multiple future generations
- Runs **Monte Carlo simulations** to observe variability in outcomes
- Visualizes:
  - Eye color distribution over generations
  - Proportions of eye colors across multiple simulation runs

---

## Tech
- Python, Jupyter Notebook  
- Pandas, NumPy, Matplotlib, tqdm (progress bars for simulations)

---

## Expected Output
- **Line plots** showing the number of people with each eye color per generation  
- **Excel file** to store the data generated 

---

## How to run

### 1. Clone the repository
```bash
git clone https://github.com/horvathsebi/eye_color_simulation.git
cd eyecolor-simulation
```

### 2. Install required packages
```bash
pip install pandas numpy matplotlib tqdm
```

### 3. Run the analysis
- Open `tester.ipynb` to run pre-built examples  
- Or import and experiment with the functions in `eyecolors.py` in your own notebook/script  
