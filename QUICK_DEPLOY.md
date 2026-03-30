# 🚀 Push to GitHub & Deploy to Streamlit Cloud

Your git is configured! Now follow these steps:

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Enter repository name: `bank-churn-prediction`
3. Choose **Public** (so everyone can access your app)
4. Click **Create repository**

## Step 2: Push Your Code to GitHub

After creating the repo, you'll see a page with commands. Run this in your terminal:

```bash
cd /Users/chhinh.dalfro/Documents/Script/Data_Scient/churn_streamlit_app
git branch -M main
git remote add origin https://github.com/chhinh36/bank-churn-prediction.git
git push -u origin main
```

**Note:** You may be prompted to authenticate. Use one of these options:

- **GitHub Personal Access Token** (recommended for CLI)
  1. Go to Settings → Developer settings → Personal access tokens → Tokens (classic)
  2. Click "Generate new token (classic)"
  3. Check `repo` and `gist` scopes
  4. Copy the token and paste it when prompted for password

- **SSH Key** (alternative)
  1. Already set up SSH? Run: `git remote set-url origin git@github.com:chhinh36/bank-churn-prediction.git`
  2. Then run: `git push -u origin main`

## Step 3: Deploy to Streamlit Cloud

Once your code is on GitHub:

1. Go to https://share.streamlit.io
2. Click **Sign up** → Sign in with GitHub (allow access to your repos)
3. Click **Create app**
4. Fill in:
   - **Repository:** `chhinh36/bank-churn-prediction`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click **Deploy!**

**Your app will be live in 1-2 minutes!** 🎉

You'll get a public URL like:

```
https://bankchurnprediction-xxxxx.streamlit.app
```

Share this link with anyone!

---

## Need Help?

If you get stuck on Step 2 (authentication), let me know and I can help you generate a GitHub personal access token!
