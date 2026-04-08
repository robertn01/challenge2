#!/usr/bin/env python3
"""
Commander Orbit Flask API Server
Exposes the Space Mission Specialist AI agent via REST API
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime, timedelta
import json
import sys

# Import the agent
from space_mission_demo import CommanderOrbit, MCPToolsSimulator

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # Enable CORS for all routes

# Initialize the agent
agent = CommanderOrbit()

# API Routes

@app.route('/', methods=['GET'])
def index():
    """Serve the main ESA Atlas webpage"""
    return send_from_directory('.', 'index.html')

@app.route('/api/agent/info', methods=['GET'])
def agent_info():
    """Get agent information and capabilities"""
    return jsonify({
        "name": "Commander Orbit",
        "role": "Space Mission Planning Specialist",
        "organization": "International Space University (ISU)",
        "status": "operational",
        "system_prompt": agent.system_prompt(),
        "tools": [
            {
                "name": "satellite_position_api",
                "description": "Real-time orbital position and tracking data",
                "capabilities": ["ISS tracking", "ESA satellite monitoring", "orbital decay predictions"]
            },
            {
                "name": "esa_mission_database",
                "description": "ESA mission planning and coordination database",
                "capabilities": ["Mission search", "Launch scheduling", "Agency coordination"]
            },
            {
                "name": "orbital_calculator",
                "description": "Orbital mechanics and trajectory analysis",
                "capabilities": ["Hohmann transfer", "Delta-V calculation", "Transit time"]
            },
            {
                "name": "space_weather_api",
                "description": "Solar activity and space environment monitoring",
                "capabilities": ["KP index", "Launch favorability", "Radiation alerts"]
            }
        ]
    })

@app.route('/api/agent/plan-mission', methods=['POST'])
def plan_mission():
    """Plan a space mission using the agent"""
    try:
        data = request.json
        mission_type = data.get('mission_type', 'iss_resupply')
        
        if mission_type == 'iss_resupply':
            # Use the existing demo mission plan
            plan = agent.plan_mission_to_iss_api()
            return jsonify({
                "status": "success",
                "mission_plan": plan,
                "timestamp": datetime.now().isoformat()
            })
        else:
            return jsonify({
                "status": "error",
                "message": f"Mission type '{mission_type}' not yet implemented"
            }), 400
            
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/agent/track-satellite', methods=['POST'])
def track_satellite():
    """Track a specific satellite in real-time"""
    try:
        data = request.json
        satellite_id = data.get('satellite_id', 'ISS')
        
        position = agent.tools.get_orbital_position(satellite_id, datetime.now().isoformat())
        
        if 'error' in position:
            return jsonify({
                "status": "error",
                "message": position['error']
            }), 404
        
        return jsonify({
            "status": "success",
            "tracking_data": position,
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/agent/search-missions', methods=['GET'])
def search_missions():
    """Search ESA mission database"""
    try:
        agency = request.args.get('agency')
        status = request.args.get('status')
        
        results = agent.tools.search_missions(agency=agency, status=status)
        
        return jsonify({
            "status": "success",
            "missions": results,
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/agent/calculate-transfer', methods=['POST'])
def calculate_transfer():
    """Calculate orbital transfer parameters"""
    try:
        data = request.json
        origin_altitude = data.get('origin_altitude_km', 200)
        target_altitude = data.get('target_altitude_km', 408)
        
        transfer = agent.tools.calculate_transfer(
            origin_altitude_km=origin_altitude,
            target_altitude_km=target_altitude
        )
        
        return jsonify({
            "status": "success",
            "transfer": transfer,
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/agent/space-weather', methods=['GET'])
def space_weather():
    """Get current space weather conditions"""
    try:
        weather = agent.tools.get_space_weather()
        
        return jsonify({
            "status": "success",
            "weather": weather,
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/agent/constellation-status', methods=['GET'])
def constellation_status():
    """Get ESA satellite constellation health status"""
    try:
        satellites = ["ISS", "COPERNICUS-SENTINEL-1A"]
        constellation = {}
        
        for sat_id in satellites:
            position = agent.tools.get_orbital_position(sat_id, datetime.now().isoformat())
            constellation[sat_id] = position
        
        return jsonify({
            "status": "success",
            "constellation": constellation,
            "health_summary": {
                "operational_satellites": len(satellites),
                "collision_risk": "none",
                "debris_avoidance_required": False
            },
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Add helper method to CommanderOrbit for API responses
def add_api_methods():
    """Add API-friendly methods to the agent"""
    def plan_mission_to_iss_api():
        """Return mission plan without printing"""
        iss_position = agent.tools.get_orbital_position("ISS", datetime.now().isoformat())
        transfer = agent.tools.calculate_transfer(origin_altitude_km=200, target_altitude_km=408)
        weather = agent.tools.get_space_weather()
        
        mission_plan = {
            "mission_name": "Dragon Resupply-15 (ISS Utilization)",
            "status": "APPROVED_FOR_EXECUTION",
            "iss_position": iss_position['position'],
            "iss_target_altitude_km": 408.5,
            "launch_site": "Cape Canaveral, Florida",
            "launch_window_utc": (datetime.now() + timedelta(days=5)).isoformat(),
            "spacecraft": "SpaceX Dragon 2",
            "cargo_mass_kg": 2700,
            "mission_duration_days": 30,
            "transfer_analysis": {
                "type": transfer['transfer_type'],
                "delta_v_kmps": transfer['delta_v_required_kmps'],
                "transit_hours": transfer['transit_time_hours']
            },
            "space_weather": {
                "kp_index": weather['kp_index'],
                "launch_favorability": weather['launch_favorability'],
                "recommendations": weather['recommendations']
            },
            "safety_risk_assessment": "GREEN - All parameters nominal",
            "international_coordination": ["ESA", "Roscosmos", "JAXA"],
            "approvals_required": ["NASA JSC", "CNES", "DLR"],
            "approval_status": "Pending final ESA coordination review"
        }
        return mission_plan
    
    agent.plan_mission_to_iss_api = plan_mission_to_iss_api

add_api_methods()

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    """API health check"""
    return jsonify({
        "status": "healthy",
        "service": "Commander Orbit Mission Specialist API",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("\n" + "="*70)
    print("COMMANDER ORBIT - FLASK API SERVER")
    print("="*70)
    print("\nStarting server on http://localhost:5000")
    print("\nAvailable Endpoints:")
    print("  GET  / (main ESA Atlas website)")
    print("  GET  /api/health")
    print("  GET  /api/agent/info")
    print("  POST /api/agent/plan-mission")
    print("  POST /api/agent/track-satellite")
    print("  GET  /api/agent/search-missions")
    print("  POST /api/agent/calculate-transfer")
    print("  GET  /api/agent/space-weather")
    print("  GET  /api/agent/constellation-status")
    print("\n" + "="*70 + "\n")
    
    app.run(debug=True, port=5000, host='127.0.0.1')
