# 🏥 healthcare-kpis

### An End-to-End Data Analytics Project on the Healthcare Sector

Welcome to the **healthcare-kpis** repository! This project is a comprehensive data analytics solution designed to provide actionable insights for two key audiences: **healthcare administrators** and **patients**.

By transforming raw hospital and patient data into key performance indicators (KPIs), this project demonstrates a full data analytics workflow from data ingestion to a live, interactive web application.

📊 **Live Demo:** [Link to your Streamlit App on DuckDNS]


---

### 💡 Project Overview

The core objective was to analyze hospital performance and patient experience to deliver targeted insights. This project showcases the ability to manage a full data pipeline, leveraging Python for processing, Streamlit for a live app, and Power BI for in-depth reporting.

The project is structured around two core sets of KPIs:
1.  **Hospital KPIs:** Focused on operational efficiency, costs, and patient flow.
2.  **Patient KPIs:** Focused on satisfaction, affordability, and accessibility of care.

---

### 💾 Data & Sources

Given the sensitive nature of real-world healthcare data, this project uses a **realistic, synthetic dataset** generated with Python (`src/data_generator.py`). This simulated data is structured to be representative of real-world hospital operations and patient interactions, ensuring the analysis is practical and relevant.

The dataset fields include:
* `date`: The date of the record.
* `hospital_id`: A unique identifier for the hospital.
* `department`: The hospital department (e.g., Emergency, Cardiology).
* `patients_admitted`: Number of patients admitted on a given day.
* `avg_stay_days`: Average length of stay in days.
* `er_wait_time`: Average emergency room wait time in hours.
* `satisfaction_rating`: A score from 1-5.

---

### 🚀 Getting Started

Follow these simple steps to set up the project locally.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/SyedHassan007/Health-Care.git
    cd Health-Care
    ```
2.  **Create a virtual environment & install dependencies:**
    ```bash
    python -m venv venv
    venv\Scripts\activate # On Linux: source venv/bin/activate
    pip install -r requirements.txt
    ```
3.  **Generate the synthetic data:**
    ```bash
    python src/data_generator.py
    ```
4.  **Run the ETL process to clean the data:**
    ```bash
    python src/etl.py
    ```
5.  **Run the Streamlit app locally:**
    ```bash
    streamlit run src/app.py
    ```
    Your browser should open to `http://localhost:8501`.

---

### 📂 Repository Structure

* `data/`: Stores both raw and processed datasets.
* `notebooks/`: Jupyter notebooks documenting the analysis process.
* `src/`: All Python scripts for data generation, ETL, KPI calculations, and the Streamlit app.
* `powerbi/`: Contains the Power BI `.pbix` file.
* `excel/`: Contains the Excel KPI summary.
* `tests/`: Unit tests for the KPI calculation functions.
* `README.md`: The document you are reading!
* `LICENSE` : This contains the License

---

### 📊 Key Performance Indicators (KPIs)

#### **Hospital KPIs**
| KPI | Formula / Calculation | Description |
|---|---|---|
| **Bed Occupancy Rate** | (Total Patients Admitted / Total Available Beds) * 100 | Measures hospital utilization efficiency. |
| **Avg. Length of Stay (ALOS)** | Average `avg_stay_days` | A key metric for operational efficiency. |
| **Readmission Rate** | (Total Readmissions / Total Discharges) * 100 | Indicates the quality of care and patient outcomes. |
| **ER Wait Time** | Average `er_wait_time` | Measures patient access to emergency care. |
| **Cost per Patient** | Total Revenue / Total Patients | A financial health metric. |

#### **Patient KPIs**
| KPI | Calculation | Description |
|---|---|---|
| **Patient Satisfaction Score** | Average `satisfaction_rating` | Gauges overall patient experience. |
| **Avg. Treatment Cost** | Average `revenue` per medical condition | Helps patients understand potential financial burden. |
| **Appointment Availability** | A custom index based on patient admission volumes | A proxy for how easy it is to get an appointment. |
| **Out-of-Pocket Expenses** | `revenue` * (1 - `insurance_coverage`) | Measures the direct cost to the patient. |

---

### 🖼️ Sample Visuals

* **Monthly Admissions Trend:** A line chart showing the flow of patients over time.
* **Average Treatment Cost:** A bar chart illustrating the average cost of treatment for different conditions.

---

### 🤝 How to Contribute

This project is open-source. Feel free to fork the repository, open an issue, or submit a pull request with new features or improvements.

---

### 📧 Contact

* **Name:** Syed Allahdad Hassan
* **LinkedIn:** [LinkedIn](https://www.linkedin.com/in/syed-hassan-7b610829a/)
* **GitHub:** [GitHub](https://github.com/SyedHassan007/)