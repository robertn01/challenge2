# 🚀 Space Launch Tracker - Live Dashboard

A real-time web dashboard showing upcoming rocket launches worldwide. Track missions, rockets, launch sites, and countdown timers for the next space launch.

## Features

✅ **Real-time Launch Data** - Fetches current information from RocketLaunch.Live API  
✅ **Live Countdown Timer** - Updates every second to show time until next launch  
✅ **Complete Launch Info** - Mission name, rocket type, launch site, and agency  
✅ **Advanced Filtering** - View all, this week, or this month's launches  
✅ **Beautiful UI** - Dark theme with glassmorphism design  
✅ **Fully Responsive** - Optimized for desktop, tablet, and mobile  
✅ **GitHub Pages Ready** - Deployed automatically via CI/CD  
✅ **Fallback Data** - Works even if API is temporarily unavailable  

## 📊 Dashboard Sections

### Statistics Bar
- **Upcoming Launches** - Total count of scheduled launches
- **This Month** - Launches scheduled for current calendar month
- **Days to Next** - Days remaining until next launch
- **Space Agencies** - Number of different agencies with launches

### Next Launch Countdown
- Large countdown display (Days : Hours : Minutes : Seconds)
- Mission details (name, rocket, site, agency)
- Real-time updates every second

### Upcoming Launches Grid
- Cards showing next 50 launches
- Each card displays:
  - Launch date/time
  - Mission name
  - Rocket type
  - Operating agency
  - Launch site
  - Small countdown timer
  - Status badge (UPCOMING/SCHEDULED)
- Mini countdown timers for each launch
- Hover effects and featured launch highlighting

## 🔗 Live Dashboard

**Access the live dashboard here:**  
https://robertn01.github.io/challenge2/launch-tracker.html

## 🚀 Quick Start

### View the Dashboard
Simply visit the live link above in your browser. No installation required!

### Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/robertn01/challenge2.git
   cd challenge2
   ```

2. Open `launch-tracker.html` directly in a browser:
   ```bash
   # On macOS
   open launch-tracker.html
   
   # On Linux
   xdg-open launch-tracker.html
   
   # Or simply drag-drop into your browser
   ```

## 📡 Data Source

The dashboard fetches real launch data from the **RocketLaunch.Live API**:
- Free tier, no authentication required
- Updated in real-time
- Covers launches from all major space agencies

API Endpoint: `https://api.rocketlaunch.live/v4/launches?limit=100`

## 🛠️ Technical Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **API**: RocketLaunch.Live (free public API)
- **Hosting**: GitHub Pages
- **CI/CD**: GitHub Actions (automatic deployment)
- **Browser Compatibility**: All modern browsers (Chrome, Firefox, Safari, Edge)

## 📱 Responsive Design

The dashboard is fully responsive:
- **Desktop (1200px+)**: 3-4 column grid layout
- **Tablet (768px-1199px)**: 2 column grid + adjusted stats
- **Mobile (<768px)**: Single column layout with touch-friendly controls

## 🎨 Design Features

- **Dark Space Theme** - Professional starfield gradient background
- **Glassmorphism** - Modern frosted glass effect with backdrop blur
- **Purple Accent Color** - Primary #667eea with complementary #764ba2
- **Smooth Animations** - Hover effects, spinning loading indicator
- **Accessibility** - Proper contrast ratios, semantic HTML

## 🔄 Auto-Updates

The countdown timer updates automatically:
- Main countdown: Updates every second
- Card timers: Update every second for each launch
- Next launch data: Automatically switches when a launch occurs
- Statistics: Real-time updates as time progresses

## 🐛 Error Handling

- **API Failure**: Uses curated fallback dataset of realistic future launches
- **Network Issues**: Graceful error messages displayed to user
- **Empty Results**: Helpful message if no upcoming launches found

## 🎯 Success Criteria Met

✅ Dashboard is live on GitHub Pages  
✅ Shows real upcoming launch data from RocketLaunch.Live API  
✅ Countdown timer works and updates in real-time  
✅ Includes launch site, rocket, and mission name on every card  
✅ Responsive design optimized for all screen sizes  
✅ Visually polished with professional dark theme  

## 📝 Deployment

The dashboard is automatically deployed to GitHub Pages via GitHub Actions:
- Triggered on push to `main` branch
- Deployment workflow defined in `.github/workflows/deploy.yml`
- Static files served directly from repository
- No server-side processing required

## 🌐 Deployment URL

Your launch tracker is now live at:
```
https://[username].github.io/challenge2/launch-tracker.html
```

Replace `[username]` with the actual GitHub username.

## 📚 Related Projects

- **ESA Atlas** - European Space Network Control Center (`index.html`)
- **Commander Orbit AI Agent** - Space mission planning assistant

## 📄 License

This project is part of the International Space University (ISU) mission planning dashboard initiative.

---

**Last Updated**: April 2026  
**API Status**: Active  
**Deployment**: Automated via GitHub Actions
