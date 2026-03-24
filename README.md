# Data

## Source
Netflix Movies and TV Shows dataset from Kaggle:
https://www.kaggle.com/datasets/shivamb/netflix-shows?resource=download

## How to Get the Data
1. Download `netflix_titles.csv` from the Kaggle link above
2. Place it in the `data/raw/` folder
3. Run notebooks in order starting from `01_data_exploration.ipynb`

## Dataset Columns
| Column | Description |
|--------|-------------|
| show_id | Unique ID for each title |
| type | Movie or TV Show |
| title | Title of the content |
| director | Director name |
| cast | Main cast members |
| country | Country of production |
| date_added | Date added to Netflix |
| release_year | Year of release |
| rating | Content rating (PG, R, etc.) |
| duration | Duration in minutes or seasons |
| listed_in | Genre categories |
| description | Short description |


# 🎬 Netflix Movies & TV Shows — Exploratory Data Analysis

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.1-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

## 📌 Project Overview
This project performs a comprehensive Exploratory Data Analysis (EDA) 
on the Netflix Movies and TV Shows dataset to uncover content trends, 
growth patterns, and strategic insights that could guide content 
acquisition decisions.

---

## 🎯 Business Questions Answered
1. How many Movies vs TV Shows does Netflix have?
2. How has Netflix grown its content library over the years?
3. What are the most popular genres on Netflix?
4. Which countries produce the most Netflix content?
5. Which content ratings dominate the platform?

---

## 🔑 Key Findings

| # | Finding | Insight |
|---|---------|---------|
| 1 | Netflix has 2.4x more Movies than TV Shows | Movies are the core of Netflix's strategy |
| 2 | Content grew 10x from 2015 to 2019 | Aggressive expansion phase |
| 3 | International Movies is the #1 genre | Netflix investing heavily in global content |
| 4 | USA #1, India #2 in content production | Asia is Netflix's biggest growth market |
| 5 | TV-MA dominates ratings | Netflix targets mature adult audiences |

---

## 📊 Visualizations

### Movies vs TV Shows
![Content Type](outputs/figures/01_content_type.png)

### Netflix Growth Over the Years
![Growth](outputs/figures/02_growth_over_years.png)

### Top 10 Genres
![Genres](outputs/figures/03_top_genres.png)

### Top 10 Countries
![Countries](outputs/figures/04_top_countries.png)

### Content Ratings
![Ratings](outputs/figures/05_ratings.png)

---

## 🗂️ Project Structure
```
netflix-eda/
├── data/
│   ├── raw/                  # Original dataset
│   └── processed/            # Cleaned data
├── notebooks/
│   └── 01_data_exploration.ipynb
├── src/
│   ├── data_loader.py        # Data loading functions
│   ├── utils.py              # Data cleaning functions
│   └── visualizations.py    # Chart functions
├── outputs/
│   └── figures/              # Generated charts
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run This Project

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/netflix-eda.git
cd netflix-eda
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the dataset
Download `netflix_titles.csv` from:
https://www.kaggle.com/datasets/shivamb/netflix-shows

Place it in `data/raw/`

### 4. Run the notebook
```bash
jupyter notebook notebooks/01_data_exploration.ipynb
```

---

## 🛠️ Tools & Technologies
- **Python 3.14** — Core programming language
- **Pandas** — Data manipulation and analysis
- **Matplotlib** — Data visualization
- **Jupyter Notebook** — Interactive analysis environment

---

## 👤 Author
**Rohit Raj**
- GitHub: [TheR0HIT](https://github.com/TheR0HIT)

---

## 📄 License
This project is licensed under the MIT License.