# 🚀 Deployment Guide: Launch Tracker on GitHub Pages

## Overview

Your Space Launch Tracker is configured to automatically deploy to GitHub Pages using GitHub Actions. Follow these steps to get it live.

## Step-by-Step Deployment

### 1. Enable GitHub Pages in Repository Settings

1. Go to your repository: **https://github.com/robertn01/challenge2**
2. Click **Settings** (top-right menu)
3. Scroll down to **"Pages"** section
4. Under **"Build and deployment"**:
   - **Source**: Select **"GitHub Actions"**
   - This should auto-select the workflow we created
5. Click **Save**

### 2. Trigger the Deployment Workflow

The workflow will be triggered automatically when you:
- Push to `main` or `master` branch
- Modify `launch-tracker.html` or `index.html`
- Manually trigger via GitHub Actions

**Manual trigger:**
1. Go to **Actions** tab
2. Find **"Deploy to GitHub Pages"** workflow
3. Click **Run workflow** → Select branch **main** → **Run workflow**

### 3. Verify the Deployment

1. Go to **Settings** → **Pages**
2. Look for the deployment message: "Your site is live at..."
3. Click the link to access your live dashboard

**Your dashboard will be available at:**
```
https://robertn01.github.io/challenge2/launch-tracker.html
```

## What Gets Deployed

The GitHub Actions workflow deploys:
- ✅ `launch-tracker.html` - Main Space Launch Tracker dashboard
- ✅ `index.html` - ESA Atlas map interface
- ✅ All CSS and JavaScript (inline in HTML)
- ✅ Any static assets in the repository

## Automatic Updates

The dashboard automatically updates because:
1. **Real-time API calls** - JavaScript fetches latest launch data directly from RocketLaunch.Live API
2. **Client-side rendering** - All updates happen in the browser
3. **No server needed** - Pure static hosting on GitHub Pages

## API Data Source

The dashboard fetches data from **RocketLaunch.Live API**:
- Endpoint: `https://api.rocketlaunch.live/v4/launches?limit=100`
- Updates: Real-time, refreshed on each page load
- Data: Actual upcoming launches from all major space agencies

## Troubleshooting

### Pages Not Building?

**Check the Actions log:**
1. Go to **Actions** tab
2. Find the "Deploy to GitHub Pages" workflow run
3. Check logs for any errors
4. Common issues:
   - Wrong branch (should be `main`)
   - Repository visibility (must be public for Pages)
   - File permissions

**Solution:**
```bash
# Ensure proper repository structure
git status
git add .
git commit -m "fix: ensure all files are tracked"
git push origin main
```

### Dashboard not showing real data?

**Check browser console:** (Press F12)
- Look for CORS errors (may need fallback data)
- Check if RocketLaunch API is accessible
- The dashboard includes fallback data if API fails

**Try local testing first:**
```bash
# Open directly in browser
cd /Users/haha/Desktop/AI_IWS/AI_UI
open launch-tracker.html
```

### Changes not appearing?

**Clear cache:**
- Hard refresh: `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
- Clear browser cache
- Wait for GitHub Actions workflow to complete (~1-2 minutes)

## Advanced Configuration

### Enable HTTPS (Automatic)

GitHub Pages automatically provides HTTPS certificates. Your dashboard will be:
```
https://robertn01.github.io/challenge2/launch-tracker.html
```

### Custom Domain (Optional)

To use a custom domain:
1. Go to **Settings** → **Pages**
2. Add your custom domain under "Custom domain"
3. Update DNS records at your domain provider
4. GitHub will auto-generate SSL certificate

### Environment Variables (If Needed)

Currently, the dashboard doesn't require environment variables. All data comes from:
- Public RocketLaunch.Live API
- Hardcoded fallback dataset
- Browser-based JavaScript

## Deployment Status

**Current Status:** ✅ Ready to Deploy

**What's configured:**
- ✅ GitHub Actions workflow (`.github/workflows/deploy.yml`)
- ✅ Static file hosting (all HTML/CSS/JS inline)
- ✅ Automatic HTTPS (GitHub Pages)
- ✅ Real-time data API integration
- ✅ Responsive design optimized for all devices

**Next steps:**
1. Enable GitHub Pages in repository settings (if not already done)
2. Push to `main` branch or manually trigger workflow
3. Wait for deployment (~1-2 minutes)
4. Access dashboard at: `https://robertn01.github.io/challenge2/launch-tracker.html`

## Monitoring Deployments

### GitHub Actions Dashboard

View deployment history:
1. Go to **Actions** tab
2. Select **Deploy to GitHub Pages** workflow
3. See all deployment runs with status (✅ or ❌)

### Environment Status

Check live status:
1. Go to **Settings** → **Pages**
2. Shows deployment status and live URL
3. Last deployment time and status

## Performance Tips

The dashboard is highly optimized:
- **No build step required** - Pure static files
- **Fast loading** - All CSS/JS inline
- **Cached data** - Browser caches launch data during session
- **Low bandwidth** - Only fetches API data once on page load
- **CDN distributed** - GitHub Pages uses global CDN

## Security

Your dashboard is secure:
- ✅ HTTPS encryption (automatic)
- ✅ No server-side code execution
- ✅ No database access
- ✅ Public API calls (no credentials exposed)
- ✅ Static files only (no vulnerabilities from dynamic code)

## FAQ

**Q: Will my dashboard update without refreshing?**  
A: Countdown timers update in real-time. To fetch new launches, refresh the page.

**Q: What if RocketLaunch API goes down?**  
A: Fallback dataset loads automatically with 6 realistic future launches.

**Q: Can I customize the launch data?**  
A: Yes! Edit the `loadFallbackData()` function in `launch-tracker.html` to modify fallback launches.

**Q: How often is the data updated?**  
A: The API provides real-time data. Dashboard refreshes data on page load.

**Q: Can I host this elsewhere?**  
A: Yes! Since it's pure static HTML, you can host on any service:
- Netlify
- Vercel
- AWS S3 + CloudFront
- Any web server

---

**Last Updated:** April 2026  
**Deployment Automated:** Yes (GitHub Actions)  
**Status:** ✅ Ready for Production
