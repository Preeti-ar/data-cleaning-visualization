# Data Cleaning & Visualization Project

## Overview
This beginner-friendly Python project demonstrates how to clean a raw sales dataset, summarize it, and create visual reports.

## Dataset
`raw_sales_data.csv` is a small sample dataset created for this project. It includes sales dates, products, categories, units sold, unit prices, and cities. It intentionally contains missing values and a duplicate row for cleaning practice.

## Objectives
- Inspect missing values and duplicate records
- Fill missing numeric values using the median
- Fill missing city values with `Unknown`
- Remove duplicate rows
- Calculate revenue (`Units_Sold × Unit_Price`)
- Summarize revenue by product and units sold by city
- Create charts for the key findings

## Tools
- Python
- Pandas
- Matplotlib

## How to run
1. Install Python 3.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python analysis.py`

The script creates an `outputs` folder containing cleaned data, a product summary, and two charts.

## Key note
This is a demonstration project using a sample dataset, not real business data. Review the generated outputs before presenting any conclusions.

## Project structure
- `analysis.py` — data-cleaning and visualization code
- `raw_sales_data.csv` — sample raw dataset
- `requirements.txt` — required Python libraries
- `outputs/` — generated results after running the script
