# 🛰️ TowerVision: AI-Powered Telecom OCR & Analytics Platform

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![Tesseract OCR](https://img.shields.io/badge/Tesseract-OCR-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow?logo=pandas)
![Firestore](https://img.shields.io/badge/Firestore-NoSQL%20DB-blue?logo=firebase)
![Power BI](https://img.shields.io/badge/Power%20BI-Visualization-yellow?logo=powerbi)

---

**Tags:**  
[`telecom`](#) [`ocr`](#) [`image-processing`](#) [`computer-vision`](#) [`opencv`](#) [`tesseract-ocr`](#) [`python`](#) [`flask`](#) [`pandas`](#) [`numpy`](#) [`firestore`](#) [`google-vision-api`](#) [`data-analytics`](#) [`powerbi`](#) [`automation`](#) [`data-visualization`](#) [`field-operations`](#) [`end-to-end-project`](#) [`portfolio-project`](#)  

---

## 📡 Overview
The **Telecom Tower Performance Management System** is an AI-powered platform built to optimize telecom site monitoring through automated **image validation**, **OCR-based data extraction**, and **report generation**. It enables seamless coordination between administrators, riggers, and engineers, ensuring efficient data tracking before and after tower equipment changes.

---

## 🎯 Key Objectives
- Enable image-based data validation using OCR and computer vision.
- Automate tower site assignment and performance tracking.
- Streamline data submission from riggers (field engineers).
- Generate accurate, actionable analytics and reports for audits.
- Maintain traceability of pre and post-installation changes.

---

## 🔍 Core Features

### 🔐 Authentication
- Secure **Admin** and **User** login portals.
- Role-based access to dashboards and functionalities.

### 🧾 OCR & Image Validation
- Integrated **Tesseract OCR** and **OpenCV** pipelines for extracting key image data:
  - Antenna height
  - Mechanical tilt
  - Pole tilt
  - Azimuth
  - Clutter
- Pre-trained image recognition models for validating user-uploaded tower images.

### 🗃️ Pre/Post-Change Data Handling
- Upload & store **pre-implementation images** by riggers.
- Capture **post-implementation images** with updates.
- Automated comparison between pre and post parameters.
- Visual folder structure for storing images by site and timestamp.

### 🛠️ Admin Capabilities
- Allocate towers to riggers based on project and region.
- View and confirm submitted image data.
- Download Excel-based reports and image logs.
- Trigger post-change updates and validations.

### 👷‍♂️ User (Rigger) Tools
- View assigned sites and project details.
- Upload pre and post change images.
- Validate captured images before submission.
- Monitor upload status and receive success confirmations.

### 📊 Analytics & Reports
- Generate detailed pre/post change Excel reports.
- Visual dashboards using **Power BI** to show:
  - Engineer performance
  - Validation accuracy
  - Completion rate
  - Error trends

---

## 🧱 System Modules

**Admin Panel**
- ✅ Site Allocation to Riggers
- 📥 View/Download Pre/Post Data
- 🖼️ Image Folder Access
- 📄 Excel Report Export

**User Panel**
- 📍 Allocation View
- 📤 Image Upload (Pre/Post)
- 📁 Folder-based Image Storage
- 📑 Submission Status

---

## 🧠 Technologies Used
- **Backend:** Python, Flask (REST API)
- **OCR & Vision:** OpenCV, Tesseract OCR, Google Vision API
- **Data Handling:** Pandas, NumPy
- **Database:** Firestore (Cloud-based NoSQL DB)
- **Visualization:** Power BI
- **Image Storage:** Structured folder architecture

---

## 🧪 Sample Workflow Diagram

```mermaid
flowchart TD
    A[User Uploads Pre-Change Images] --> B[OCR & Image Processing]
    B --> C[Data Extraction & Validation]
    C --> D[Admin Review & Approval]
    D --> E[User Uploads Post-Change Images]
    E --> F[Automated Comparison]
    F --> G[Report Generation & Dashboard Update]
