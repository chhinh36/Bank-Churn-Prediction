# 🚀 Deployment Guide for Streamlit Cloud

This guide explains how to deploy your Streamlit app on **Streamlit Cloud** for free public access.

---

## Step 1: Push Your Code to GitHub

### 1a. Configure Git

```bash
cd /Users/chhinh.dalfro/Documents/Script/Data_Scient/churn_streamlit_app
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### 1b. Stage and Commit Files

```bash
git add .
git commit -m "Initial commit: Bank Churn Prediction Streamlit App"
```

### 1c. Create a GitHub Repository

1. Go to [github.com](https://github.com) and sign in
2. Click **New repository** (green button)
3. Name it: `bank-churn-prediction` (or your preferred name)
4. Choose **Public** (for public access)
5. Do NOT initialize with README/gitignore (use local)
6. Click **Create repository**

### 1d. Push to GitHub

After creating the repo, GitHub will show you commands. Run:

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/bank-churn-prediction.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## Step 2: Deploy on Streamlit Cloud

### 2a. Sign Up for Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **Sign up** and sign in with your GitHub account
3. Authorize Streamlit to access your GitHub repos

### 2b. Deploy Your App

1. Click **Create app** button
2. Select:
   - **Repository**: `YOUR_USERNAME/bank-churn-prediction`
   - **Branch**: `main`
   - **Main file path**: `app.py`
3. Click **Deploy!**

Streamlit will build and deploy your app. It typically takes 1-2 minutes.

### 2c. Get Your Live Link

Once deployed, you'll get a public URL like:

```
https://bankchurnprediction-xxxxx.streamlit.app
```

Share this link with anyone to let them use your app!

---

## Step 3: Update Your App

Whenever you update your code:

```bash
cd /Users/chhinh.dalfro/Documents/Script/Data_Scient/churn_streamlit_app
git add .
git commit -m "Your commit message"
git push origin main
```

Streamlit Cloud automatically redeploys when you push to GitHub!

---

## 📋 Requirements for Deployment

✅ Your project includes:

- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `model.pkl`, `features.pkl`, `threshold.pkl` - Model files
- `.streamlit/config.toml` - Streamlit configuration
- `.gitignore` - Git ignore rules

---

## Troubleshooting

**"FileNotFoundError" on deployed app:**

- Make sure all `.pkl` files are in the same directory as `app.py`
- The app uses relative paths that work in any directory

**"Module not found" error:**

- Check that all packages in `requirements.txt` are listed

**App is slow to load:**

- Streamlit Cloud's free tier has limited resources
- First load is slower (~20-30 seconds)

---

## 🎉 You're Done!

Your app is now live and accessible to everyone with the link!

Enjoy sharing your Churn Prediction app! 🏦
