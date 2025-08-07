# 📡 Telecom Tower Drive Test Tool

**Client:** Insta ICT Solution Pvt. Ltd  
**Developed by:** Devesh Sawarkar & Team 
**Project Date:** February 23, 2024  
**Tech Stack:** Python, Flask, OpenCV, Tesseract OCR, Pandas, Firestore, Power BI

---

## 🧠 Overview

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

### Admin Panel
- ✅ Site Allocation to Riggers
- 📥 View/Download Pre/Post Data
- 🖼️ Image Folder Access
- 📄 Excel Report Export

### User Panel
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

## 🧪 Sample Workflows

### 📸 Image Extraction & OCR

```plaintext
Step 1: User uploads pre-change tower images (multiple angles)
Step 2: System extracts key visual parameters via OCR
Step 3: Admin reviews extracted data
Step 4: After changes, user uploads post-change images
Step 5: System performs comparison & generates report
