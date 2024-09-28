
# AICTE Applications Data Analysis

This repository contains data analysis and visualizations for the **AICTE Applications**. It is part of a Smart India Hackathon (SIH) project where various data points related to colleges and applications under AICTE are analyzed to extract insights.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Visualizations](#visualizations)


## Overview

This project focuses on analyzing a dataset related to **AICTE applications**, providing insights such as:
- College locations
- Tier classifications of colleges
- University affiliations
- College land area categorization
- Program types (Tech/Non-Tech)
- Participation in skill development programs

The analysis is performed using Python's data science libraries such as `pandas`, `matplotlib`, and `seaborn`. The code provides interactive and insightful visualizations to help understand trends in the AICTE dataset.

## Dataset

The dataset consists of the following fields for each college application:

- **application_id**: Unique ID of the application
- **college_name**: Name of the college
- **location**: Location of the college (State)
- **city**: City of the college
- **state**: State of the college
- **college_type**: Tier classification (Tier 1, Tier 2, Tier 3)
- **affiliation**: University affiliation
- **land_area_acres**: Land area of the college (in acres)
- **program_type**: Type of program offered (Tech or Non-Tech)
- **registration_deadline**: Application registration deadline
- **participation_in_skill_dev**: Participation in skill development programs (boolean)

### Example Entry:

```json
{
    "application_id": "APP-202401",
    "college_name": "Tech Institute of Engineering",
    "location": "Delhi",
    "city": "New Delhi",
    "state": "Delhi",
    "college_type": "Tier 1",
    "affiliation": "Delhi University",
    "land_area_acres": 5.5,
    "program_type": "Tech",
    "registration_deadline": "2024-01-31",
    "participation_in_skill_dev": true
}
```

## Features

This repository includes scripts to perform the following analyses:

1. **State-wise Distribution**: Analyze the distribution of applications by state and city.
2. **College Tier Analysis**: Breakdown of applications based on college tiers (Tier 1, 2, 3).
3. **Affiliation Analysis**: Distribution of applications according to university affiliation.
4. **Land Area Grouping**: Categorization of colleges based on their land area (Small, Medium, Large).
5. **Tech vs Non-Tech Program Analysis**: Number of applications from Tech and Non-Tech colleges.
6. **Skill Development Participation**: Analyze colleges participating in skill development programs.

## Installation

To use this project locally, follow the steps below:

### Prerequisites

- Python 3.x must be installed on your system.
- Install the necessary Python libraries by following the instructions below.

### Step-by-step Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ria05/SIH_AICTE_ANALYSIS.git
   cd SIH_AICTE_ANALYSIS
   ```

2. **Install dependencies:**

   To install the required libraries, run:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, if a `requirements.txt` file is not included, install the libraries manually:

   ```bash
   pip install pandas matplotlib seaborn
   ```

## Usage

Once you have installed the necessary dependencies, you can run the analysis script to visualize and analyze the data.

### Run the Analysis

Execute the Python script as follows:

```bash
python sampleAnalysis.py
```

This will:
- Perform the data analysis.
- Display visualizations using `matplotlib` and `seaborn`.

### Modify Data

If you have your own dataset, replace the current dataset within the script or load a new dataset using `pandas` and apply the same analysis functions.

## Visualizations

The project includes the following visualizations:

1. **State-wise Applications:**
   A bar plot showing the number of applications submitted by colleges in different states.

   ![applicationsByState](https://github.com/user-attachments/assets/acff6779-40ff-4403-a4e3-d70ee617722b)


2. **College Tier Distribution:**
   A breakdown of the number of applications from Tier 1, Tier 2, and Tier 3 colleges.

   ![tierDistribution](https://github.com/user-attachments/assets/1d881d32-1f4e-49c6-b90b-4a1508c5f035)


3. **University Affiliation:**
   A bar plot showing the university affiliations of colleges that have applied.

   ![applicationUniversityAffilation](https://github.com/user-attachments/assets/52ff2c8f-662c-46c8-a4af-066ec3fabbbe)


4. **Land Area Grouping:**
   A plot showing the grouping of colleges based on their land area (Small, Medium, Large).

  ![LandArea](https://github.com/user-attachments/assets/5c1ab9e2-de42-431c-83d5-e13308a8375b)


5. **Tech vs Non-Tech Programs:**
   Visualization of the distribution of applications from Tech and Non-Tech programs.

   ![programType](https://github.com/user-attachments/assets/91d615a6-019f-48f4-901c-ae7b71d10b6a)


6. **Skill Development Participation:**
   A bar chart showing how many colleges participate in skill development programs.

   ![skillDevelopment](https://github.com/user-attachments/assets/cf14c7ea-bf94-4b45-9f47-d985ab90fb2d)


