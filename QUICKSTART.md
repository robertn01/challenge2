# 🚀 Running Commander Orbit AI Mission Specialist Agent

## Overview
The Commander Orbit AI agent is now **fully integrated** into your Space Network Control Center. The system consists of:

1. **Flask API Server** (app.py) — Backend with AI agent and MCP tools
2. **Updated Website** (index.html) — Interactive UI with 3 tabs
3. **AI Agent** (space_mission_demo.py) — Mission planning specialist

---

## Quick Start (5 minutes)

### Step 1: Install Dependencies
```bash
cd /Users/haha/Desktop/AI_IWS/AI_UI

# Install Flask and CORS support
pip install -r requirements.txt
```

### Step 2: Run the Server
```bash
python3 app.py
```

You'll see:
```
======================================================================
COMMANDER ORBIT - FLASK API SERVER
======================================================================

Starting server on http://localhost:5000

Available Endpoints:
  GET  / (main ESA Atlas website)
  GET  /api/health
  GET  /api/agent/info
  POST /api/agent/plan-mission
  POST /api/agent/track-satellite
  GET  /api/agent/search-missions
  POST /api/agent/calculate-transfer
  GET  /api/agent/space-weather
  GET  /api/agent/constellation-status
```

### Step 3: Open in Browser
Navigate to: **http://localhost:5000**

---

## Using the AI Agent

### Tab 1: 📍 ESA Atlas
- Displays all 22 ESA member states
- Interactive map with agency locations
- Country directory table
- (Original functionality, still available)

### Tab 2: 🤖 Mission Planner (AI)
Click any card to query Commander Orbit:

1. **📋 Plan Mission**
   - AI analyzes ISS resupply mission
   - Returns orbital mechanics analysis
   - Launch window recommendations
   - Safety assessments

2. **🌦️ Space Weather**
   - Real-time KP index
   - Solar wind conditions
   - Launch favorability (GREEN/YELLOW/RED)

3. **🔍 Search Missions**
   - Query ESA mission database
   - Filter by agency or status
   - See upcoming launches

4. **🛰️ Constellation Status**
   - Monitor satellite health
   - Collision risk assessment
   - Debris avoidance status

### Tab 3: 📡 Real-Time Tracking
- Select ISS or Sentinel-1A
- Get real-time orbital position
- Altitude, velocity, orbital period
- Ground track information

---

## API Endpoints

All endpoints are available at `http://localhost:5000/api/`

### Health Check
```bash
curl http://localhost:5000/api/health
```

### Plan Mission
```bash
curl -X POST http://localhost:5000/api/agent/plan-mission \
  -H "Content-Type: application/json" \
  -d '{"mission_type": "iss_resupply"}'
```

### Track Satellite
```bash
curl -X POST http://localhost:5000/api/agent/track-satellite \
  -H "Content-Type: application/json" \
  -d '{"satellite_id": "ISS"}'
```

### Space Weather
```bash
curl http://localhost:5000/api/agent/space-weather
```

### Search Missions
```bash
curl http://localhost:5000/api/agent/search-missions?agency=ESA
```

### Constellation Status
```bash
curl http://localhost:5000/api/agent/constellation-status
```

---

## File Structure
```
/Users/haha/Desktop/AI_IWS/AI_UI/
├── app.py                          (Flask API server)
├── index.html                      (Updated website with tabs)
├── space_mission_demo.py           (AI agent implementation)
├── SPACE_MISSION_SPECIALIST.md     (Agent specification)
├── requirements.txt                (Python dependencies)
├── agents.md                       (Project guidelines)
├── memory.md                       (Project notes)
├── .env                            (API keys - not deployed)
├── .gitignore                      (Excludes secrets)
└── .git/                           (Version control)
```

---

## Stopping the Server

Press `Ctrl+C` in the terminal where Flask is running.

---

## For Production Deployment

To deploy this to a live server:

1. **Install Gunicorn** (production WSGI server):
   ```bash
   pip install gunicorn
   ```

2. **Run with Gunicorn**:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Use Nginx as reverse proxy** (optional)
   - Forward requests to Gunicorn
   - Handle SSL/HTTPS

---

## Troubleshooting

### Port 5000 already in use?
```bash
# Find what's using port 5000
lsof -i :5000

# Kill it
kill -9 <PID>

# Or use a different port
python3 app.py --port 5001
```

### ModuleNotFoundError: No module named 'flask'?
```bash
pip install flask flask-cors
```

### Can't connect to localhost:5000?
- Check firewall settings
- Make sure Flask server is running
- Try `127.0.0.1:5000` instead of `localhost:5000`

---

## Agent Capabilities

**Commander Orbit** currently handles:
- ✅ ISS mission planning
- ✅ Orbital mechanics calculations
- ✅ Space weather monitoring
- ✅ ESA mission database queries
- ✅ Satellite tracking and health monitoring
- ✅ Multi-agency coordination insights

**Future expansions:**
- Custom mission types (Moon, Mars, Deep Space)
- Real API connections (Actual ESA/NASA data)
- Trajectory optimization
- Cost-benefit analysis
- International agreement compliance checks

---

## Questions?

Refer to:
- `SPACE_MISSION_SPECIALIST.md` — Agent specification
- `space_mission_demo.py` — Source code
- `app.py` — Flask API implementation
