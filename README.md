# Voice It Out (VIO)
**Speak. Report. Get Help.**

> *A secure, AI-powered sanctuary for survivors of Gender-Based Violence (GBV).*

![Mission](https://img.shields.io/badge/Mission-Giving_Them_A_Voice-purple?style=flat-square)
![Tech Stack](https://img.shields.io/badge/Built_With-Django_&_Tailwind-pink?style=flat-square)
![AI Powered](https://img.shields.io/badge/AI-Sentiment_Engine-green?style=flat-square)

---

## The Problem
In Kenya, **45% of women** between ages 15–49 have experienced physical or sexual violence. Yet, nearly **90% never report it**.
The barriers are real: **Fear of retaliation, Stigma, and Lack of Safe Channels.**

## The Solution
**Voice It Out** is not just a reporting form; it is a **Digital Safety Ecosystem**.
We leverage **AI (Natural Language Processing)** and **Geolocation Technology** to bridge the gap between silence and immediate help, ensuring that no cry for help goes unheard.

---

##  Key Features 

### 1. Ghost Protocol (Privacy First)
* **100% Anonymity:** No forced login or IP tracking for reporters.
* **Encrypted Data:** Reports are stripped of metadata to protect survivor identity.

### 2.  AI Sentinel Engine
* **Real-time Triage:** We use `TextBlob` (NLP) to analyze incident descriptions instantly.
* **Urgency Tagging:**
    * "I am uncomfortable" → 🟢 **Normal Risk**
    * "He is threatening to kill me" → **CRITICAL RISK** (Immediate Dashboard Alert)

### 3. SOS & Geolocation
* **WhatsApp Live Link:** Generates a one-click SOS message with precise GPS coordinates to send to trusted contacts.
* **Emergency Hotlines:** Direct integration with **1195 (GBV Helpline)** and **999**.

### 4. Interactive Safety Dashboard
* **Threat Radar:** A holographic visualization of incident types (Stalking, Violence, etc.).
* **Digital Go-Bag:** A secure checklist for survivors to prepare escape documents (IDs, Logbooks).
* **Vio Chatbot:** An embedded JS assistant for 24/7 triage and support.

---

## Tech Stack

* **Backend:** Python 3.10+, Django 5.0
* **Frontend:** HTML5, Tailwind CSS (Glassmorphism UI), Chart.js
* **AI/ML:** TextBlob (Sentiment Analysis)
* **Database:** SQLite (Development)

---

## Installation Guide

Follow these steps to run the project locally:

**1. Clone the Repository**
```bash
git clone https://github.com/Flora72/VoiceitOut.git
cd VoiceitOut
