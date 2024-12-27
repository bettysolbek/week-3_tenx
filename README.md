# **AlphaCare Insurance Solutions: Predictive Analytics Project**

## **Project Overview**
This project aims to analyze historical insurance claim data to optimize marketing strategies, identify low-risk client segments, and predict optimal premium values. By leveraging exploratory data analysis, data version control, hypothesis testing, and statistical modeling, the goal is to extract actionable insights and enhance business outcomes.

---

## **Tasks Breakdown**

### **Task 1: Git and GitHub (Project Planning & EDA)**

#### **Repository Setup**
1. **Create a GitHub Repository**:
   - Initialize with a `README.md` file.
2. **Branch Management**:
   - Create a branch named `task-1` for this task.
   - Commit frequently with clear, descriptive messages.

#### **Exploratory Data Analysis (EDA)**
1. **Data Summarization**:
   - Review column data types and calculate descriptive statistics.
   - Focus on variability in the `TotalPremium` and `TotalClaims` columns.

2. **Assess Data Quality**:
   - Identify and handle missing values.
   - Correct improper data types and ensure data consistency.

3. **Univariate Analysis**:
   - Generate histograms for numerical features (e.g., `TotalPremium`).
   - Create bar plots for categorical variables (e.g., `PolicyType`).

4. **Bivariate/Multivariate Analysis**:
   - Explore relationships between variables, such as `TotalPremium` vs. `TotalClaims` grouped by `ZipCode`.

5. **Outlier Detection**:
   - Use box plots and statistical methods to identify and document anomalies.

6. **Visualization**:
   - Develop three meaningful and visually engaging plots to summarize key findings.

---

### **Task 2: Data Version Control (DVC)**

#### **Set Up DVC**
1. **Install DVC**:
   ```bash
   pip install dvc
