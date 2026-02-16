# -*- coding: utf-8 -*-
"""
███████ ██   ██ ███████ ███████ ████████ 
██      ██   ██ ██      ██         ██    
█████   ███████ █████   █████      ██    
██      ██   ██ ██      ██         ██    
███████ ██   ██ ███████ ███████    ██    

╔══════════════════════════════════════════════════════════╗
║                                                          ║
║     ███╗   ███╗ █████╗ ██████╗  ██████╗ ██████╗         ║
║     ████╗ ████║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗        ║
║     ██╔████╔██║███████║██████╔╝██║   ██║██████╔╝        ║
║     ██║╚██╔╝██║██╔══██║██╔══██╗██║   ██║██╔═══╝         ║
║     ██║ ╚═╝ ██║██║  ██║██║  ██║╚██████╔╝██║             ║
║     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝             ║
║                                                          ║
║              🤖 MARCO FILE HOST v4.0.0                  ║
║        🔥 ULTIMATE PREMIUM HOSTING SOLUTION 🔥          ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

🤖 MARCO FILE HOST - ULTIMATE PREMIUM EDITION
✨ Advanced Python & Node.js Script Hosting Bot
📦 Version 4.0 - ULTIMATE - FULLY LOADED (ALL ERRORS FIXED)
"""

import telebot
import subprocess
import os
import zipfile
import tempfile
import shutil
from telebot import types
import time
from datetime import datetime, timedelta
import logging
import psutil
import sqlite3
import threading
import re
import sys
import atexit
import requests
import json
import platform
import socket
import hashlib
import signal
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import random
import string
from threading import Thread
import urllib.parse

# --- Flask Keep Alive with ULTIMATE DESIGN ---
from flask import Flask, jsonify, render_template_string, request

app = Flask('')

@app.route('/favicon.ico')
def favicon():
    return '', 204

# ======================================================================
# 🔥 ULTIMATE PREMIUM WEB DASHBOARD DESIGN - GLASSMORPHISM + NEON
# ======================================================================
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <title>🔥 MARCO HOST • ULTIMATE PREMIUM</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>">
    
    <!-- Font Awesome 6 (Premium) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    
    <!-- Google Fonts: Space Grotesk + Clash Display -->
    <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=space-grotesk@300,400,500,600,700&display=swap" rel="stylesheet">
    
    <!-- Animate.css -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
    
    <!-- Particles.js -->
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    
    <style>
        /* ===== ULTIMATE PREMIUM VARIABLES ===== */
        :root {
            --primary: #00f5d4;
            --secondary: #ff006e;
            --accent: #9d4edd;
            --dark: #0a0a0f;
            --darker: #050508;
            --light: #ffffff;
            --glass: rgba(255, 255, 255, 0.05);
            --glass-border: rgba(255, 255, 255, 0.1);
            --neon-primary: 0 0 10px #00f5d4, 0 0 20px #00f5d4, 0 0 30px #00f5d4;
            --neon-secondary: 0 0 10px #ff006e, 0 0 20px #ff006e, 0 0 30px #ff006e;
            --neon-accent: 0 0 10px #9d4edd, 0 0 20px #9d4edd, 0 0 30px #9d4edd;
            --gradient-1: linear-gradient(135deg, #00f5d4 0%, #9d4edd 50%, #ff006e 100%);
            --gradient-2: linear-gradient(45deg, #4158D0 0%, #C850C0 46%, #FFCC70 100%);
            --gradient-3: linear-gradient(90deg, #00f5d4, #9d4edd, #ff006e, #00f5d4);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Space Grotesk', sans-serif;
            background: var(--dark);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            overflow-x: hidden;
            color: var(--light);
        }

        /* ===== PARTICLES BACKGROUND ===== */
        #particles-js {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
        }

        /* ===== CUSTOM CURSOR ===== */
        * {
            cursor: none !important;
        }

        .cursor {
            width: 20px;
            height: 20px;
            border: 2px solid var(--primary);
            border-radius: 50%;
            position: fixed;
            pointer-events: none;
            z-index: 9999;
            transition: all 0.1s ease;
            box-shadow: var(--neon-primary);
        }

        .cursor-follower {
            width: 40px;
            height: 40px;
            border: 2px solid var(--accent);
            border-radius: 50%;
            position: fixed;
            pointer-events: none;
            z-index: 9998;
            transition: all 0.15s ease;
            opacity: 0.5;
            box-shadow: var(--neon-accent);
        }

        /* ===== MAIN CONTAINER ===== */
        .container {
            position: relative;
            z-index: 10;
            width: 95%;
            max-width: 1400px;
            margin: 20px auto;
            background: var(--glass);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 50px;
            padding: 40px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }

        /* ===== PREMIUM HEADER ===== */
        .header {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 40px;
            position: relative;
        }

        .logo-wrapper {
            display: flex;
            align-items: center;
            gap: 20px;
        }

        .logo-3d {
            width: 80px;
            height: 80px;
            background: var(--gradient-1);
            border-radius: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
            transform: rotate(10deg) skew(-10deg);
            box-shadow: var(--neon-primary);
            animation: rotate3d 10s linear infinite;
        }

        @keyframes rotate3d {
            0%, 100% { transform: rotate(10deg) skew(-10deg) rotateY(0deg); }
            50% { transform: rotate(10deg) skew(-10deg) rotateY(180deg); }
        }

        h1 {
            font-family: 'Clash Display', sans-serif;
            font-size: 3rem;
            font-weight: 700;
            background: var(--gradient-3);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradient 3s linear infinite;
        }

        @keyframes gradient {
            0% { background-position: 0% 50%; }
            100% { background-position: 200% 50%; }
        }

        .status-badge {
            background: var(--glass);
            backdrop-filter: blur(10px);
            border: 1px solid var(--primary);
            padding: 12px 30px;
            border-radius: 50px;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            box-shadow: var(--neon-primary);
            animation: pulse 2s infinite;
        }

        .status-badge i {
            color: var(--primary);
        }

        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 var(--primary); }
            70% { box-shadow: 0 0 20px 10px rgba(0, 245, 212, 0.3); }
            100% { box-shadow: 0 0 0 0 rgba(0, 245, 212, 0); }
        }

        /* ===== STATS GRID ===== */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }

        .stat-card {
            background: var(--glass);
            backdrop-filter: blur(10px);
            border: 1px solid var(--glass-border);
            border-radius: 30px;
            padding: 30px;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transition: left 0.7s ease;
        }

        .stat-card:hover::before {
            left: 100%;
        }

        .stat-card:hover {
            transform: translateY(-10px) scale(1.02);
            border-color: var(--primary);
            box-shadow: var(--neon-primary);
        }

        .stat-icon {
            width: 60px;
            height: 60px;
            background: var(--gradient-2);
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            margin-bottom: 20px;
            transform: rotate(-5deg);
        }

        .stat-value {
            font-size: 2.5rem;
            font-weight: 700;
            font-family: 'Clash Display', sans-serif;
            background: var(--gradient-1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.2;
        }

        .stat-label {
            font-size: 1rem;
            color: rgba(255, 255, 255, 0.7);
            letter-spacing: 1px;
        }

        /* ===== INFO PANEL ===== */
        .info-panel {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .info-item {
            background: var(--glass);
            backdrop-filter: blur(10px);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 20px;
            display: flex;
            align-items: center;
            gap: 15px;
            transition: all 0.3s ease;
        }

        .info-item:hover {
            border-color: var(--accent);
            transform: translateX(10px);
        }

        .info-icon {
            width: 50px;
            height: 50px;
            background: var(--gradient-3);
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            animation: rotate 10s linear infinite;
        }

        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .info-content {
            flex: 1;
        }

        .info-label {
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.5);
            letter-spacing: 1px;
        }

        .info-value {
            font-size: 1.2rem;
            font-weight: 600;
            word-break: break-word;
        }

        /* ===== PROGRESS BARS ===== */
        .progress-container {
            margin-top: 30px;
        }

        .progress-item {
            margin-bottom: 15px;
        }

        .progress-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 5px;
        }

        .progress-bar {
            width: 100%;
            height: 10px;
            background: var(--glass);
            border-radius: 10px;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: var(--gradient-1);
            border-radius: 10px;
            animation: progress 2s ease-out forwards;
        }

        @keyframes progress {
            from { width: 0; }
        }

        /* ===== FOOTER ===== */
        .footer {
            margin-top: 50px;
            padding-top: 30px;
            border-top: 1px solid var(--glass-border);
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
        }

        .owner-info {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .owner-avatar {
            width: 50px;
            height: 50px;
            background: var(--gradient-2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
        }

        .channel-btn {
            background: var(--gradient-3);
            background-size: 200% auto;
            padding: 15px 40px;
            border-radius: 50px;
            color: white;
            text-decoration: none;
            font-weight: 600;
            letter-spacing: 1px;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            transition: all 0.3s ease;
            animation: gradient 3s linear infinite;
        }

        .channel-btn:hover {
            transform: scale(1.05);
            box-shadow: var(--neon-accent);
        }

        /* ===== GLITCH EFFECT ===== */
        .glitch {
            position: relative;
        }

        .glitch::before,
        .glitch::after {
            content: "MARCO FILE HOST";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0.8;
        }

        .glitch::before {
            color: var(--primary);
            z-index: -1;
            transform: translateX(-2px) translateY(-1px);
        }

        .glitch::after {
            color: var(--secondary);
            z-index: -2;
            transform: translateX(2px) translateY(1px);
        }

        /* ===== SCROLLBAR ===== */
        ::-webkit-scrollbar {
            width: 10px;
        }

        ::-webkit-scrollbar-track {
            background: var(--glass);
        }

        ::-webkit-scrollbar-thumb {
            background: var(--gradient-1);
            border-radius: 10px;
        }

        /* ===== MOBILE RESPONSIVE ===== */
        @media (max-width: 768px) {
            .container { padding: 20px; }
            h1 { font-size: 2rem; }
            .logo-3d { width: 60px; height: 60px; font-size: 30px; }
        }
    </style>
</head>
<body>
    <!-- Particles Background -->
    <div id="particles-js"></div>
    
    <!-- Custom Cursor -->
    <div class="cursor" id="cursor"></div>
    <div class="cursor-follower" id="cursor-follower"></div>

    <div class="container animate__animated animate__fadeInUp">
        <!-- Header -->
        <div class="header">
            <div class="logo-wrapper">
                <div class="logo-3d">
                    🤖
                </div>
                <h1 class="glitch">MARCO HOST</h1>
            </div>
            <div class="status-badge">
                <i class="fas fa-circle"></i>
                <span>SYSTEM: ONLINE</span>
                <i class="fas fa-bolt"></i>
            </div>
        </div>

        <!-- Stats Grid -->
        <div class="stats-grid">
            <div class="stat-card" data-aos="fade-up">
                <div class="stat-icon">
                    <i class="fas fa-hourglass-half"></i>
                </div>
                <div class="stat-value">{{ uptime }}</div>
                <div class="stat-label">Uptime</div>
            </div>
            <div class="stat-card" data-aos="fade-up" data-aos-delay="100">
                <div class="stat-icon">
                    <i class="fas fa-code-branch"></i>
                </div>
                <div class="stat-value">{{ active_scripts }}</div>
                <div class="stat-label">Active Scripts</div>
            </div>
            <div class="stat-card" data-aos="fade-up" data-aos-delay="200">
                <div class="stat-icon">
                    <i class="fas fa-users"></i>
                </div>
                <div class="stat-value">{{ total_users }}</div>
                <div class="stat-label">Total Users</div>
            </div>
            <div class="stat-card" data-aos="fade-up" data-aos-delay="300">
                <div class="stat-icon">
                    <i class="fas fa-memory"></i>
                </div>
                <div class="stat-value">{{ memory_usage }}%</div>
                <div class="stat-label">RAM Usage</div>
            </div>
        </div>

        <!-- Info Panel -->
        <div class="info-panel">
            <div class="info-item">
                <div class="info-icon"><i class="fas fa-server"></i></div>
                <div class="info-content">
                    <div class="info-label">Hostname</div>
                    <div class="info-value">{{ hostname }}</div>
                </div>
            </div>
            <div class="info-item">
                <div class="info-icon"><i class="fas fa-globe"></i></div>
                <div class="info-content">
                    <div class="info-label">Platform</div>
                    <div class="info-value">{{ platform[:30] }}...</div>
                </div>
            </div>
            <div class="info-item">
                <div class="info-icon"><i class="fab fa-python"></i></div>
                <div class="info-content">
                    <div class="info-label">Python</div>
                    <div class="info-value">{{ python_version }}</div>
                </div>
            </div>
            <div class="info-item">
                <div class="info-icon"><i class="fab fa-node-js"></i></div>
                <div class="info-content">
                    <div class="info-label">Node.js</div>
                    <div class="info-value">{{ node_version }}</div>
                </div>
            </div>
            <div class="info-item">
                <div class="info-icon"><i class="fas fa-network-wired"></i></div>
                <div class="info-content">
                    <div class="info-label">IP Address</div>
                    <div class="info-value">{{ ip_address }}</div>
                </div>
            </div>
            <div class="info-item">
                <div class="info-icon"><i class="fas fa-shield-alt"></i></div>
                <div class="info-content">
                    <div class="info-label">Security</div>
                    <div class="info-value">🔒 Enterprise Grade</div>
                </div>
            </div>
        </div>

        <!-- Progress Bars -->
        <div class="progress-container">
            <div class="progress-item">
                <div class="progress-header">
                    <span>CPU Usage</span>
                    <span>{{ cpu_usage|default(0) }}%</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {{ cpu_usage|default(0) }}%;"></div>
                </div>
            </div>
            <div class="progress-item">
                <div class="progress-header">
                    <span>Disk Usage</span>
                    <span>{{ disk_usage|default(0) }}%</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {{ disk_usage|default(0) }}%;"></div>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <div class="owner-info">
                <div class="owner-avatar">
                    👑
                </div>
                <div>
                    <div style="font-size: 0.8rem; opacity: 0.7;">OWNER</div>
                    <div style="font-weight: 600;">@Zinko158</div>
                </div>
            </div>
            <a href="{{ update_channel }}" class="channel-btn" target="_blank">
                <i class="fab fa-telegram-plane"></i>
                <span>JOIN PREMIUM CHANNEL</span>
                <i class="fas fa-arrow-right"></i>
            </a>
        </div>

        <!-- Version Watermark -->
        <div style="text-align: center; margin-top: 30px; opacity: 0.5; font-size: 0.8rem;">
            MARCO HOST • ULTIMATE PREMIUM EDITION v4.0 • 24/7 ENTERPRISE GRADE
        </div>
    </div>

    <script>
        // Particles Configuration
        particlesJS('particles-js', {
            particles: {
                number: { value: 80, density: { enable: true, value_area: 800 } },
                color: { value: '#00f5d4' },
                shape: { type: 'circle' },
                opacity: { value: 0.5, random: true },
                size: { value: 3, random: true },
                line_linked: {
                    enable: true,
                    distance: 150,
                    color: '#9d4edd',
                    opacity: 0.4,
                    width: 1
                },
                move: {
                    enable: true,
                    speed: 2,
                    direction: 'none',
                    random: true,
                    straight: false,
                    out_mode: 'out',
                    bounce: false
                }
            },
            interactivity: {
                detect_on: 'canvas',
                events: {
                    onhover: { enable: true, mode: 'repulse' },
                    onclick: { enable: true, mode: 'push' },
                    resize: true
                }
            },
            retina_detect: true
        });

        // Custom Cursor
        const cursor = document.getElementById('cursor');
        const cursorFollower = document.getElementById('cursor-follower');

        document.addEventListener('mousemove', (e) => {
            cursor.style.transform = `translate(${e.clientX - 10}px, ${e.clientY - 10}px)`;
            cursorFollower.style.transform = `translate(${e.clientX - 20}px, ${e.clientY - 20}px)`;
        });

        // Hover effect on interactive elements
        document.querySelectorAll('a, button, .stat-card').forEach(el => {
            el.addEventListener('mouseenter', () => {
                cursor.style.transform += ' scale(1.5)';
                cursorFollower.style.transform += ' scale(1.5)';
            });
            el.addEventListener('mouseleave', () => {
                cursor.style.transform = cursor.style.transform.replace(' scale(1.5)', '');
                cursorFollower.style.transform = cursorFollower.style.transform.replace(' scale(1.5)', '');
            });
        });

        // Auto-refresh every 10 seconds
        setTimeout(() => {
            location.reload();
        }, 10000);
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    try:
        uptime_seconds = time.time() - start_time
        uptime_str = str(timedelta(seconds=int(uptime_seconds)))
        
        try:
            import psutil
            memory_usage = psutil.virtual_memory().percent
            cpu_usage = psutil.cpu_percent(interval=1)
            disk_usage = psutil.disk_usage('/').percent
            hostname = socket.gethostname()
            platform_info = platform.platform()
            ip_address = socket.gethostbyname(socket.gethostname())
        except:
            memory_usage = 0
            cpu_usage = 0
            disk_usage = 0
            hostname = 'N/A'
            platform_info = 'N/A'
            ip_address = 'N/A'
        
        node_ver = get_node_version()
        
        return render_template_string(
            HTML_TEMPLATE,
            uptime=uptime_str,
            active_scripts=len(bot_scripts),
            total_users=len(active_users),
            memory_usage=memory_usage,
            cpu_usage=cpu_usage,
            disk_usage=disk_usage,
            hostname=hostname,
            platform=platform_info,
            python_version=sys.version.split()[0],
            node_version=node_ver,
            ip_address=ip_address,
            update_channel=UPDATE_CHANNEL
        )
    except Exception as e:
        return f"⚠️ Status Page Error: {e}"

@app.route('/api/status')
def api_status():
    return jsonify({
        'status': 'online',
        'active_scripts': len(bot_scripts),
        'total_users': len(active_users),
        'uptime': time.time() - start_time,
        'locked': bot_locked,
        'memory_usage': psutil.virtual_memory().percent if 'psutil' in sys.modules else 0
    })

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False, threaded=True)

def keep_alive():
    t = threading.Thread(target=run_flask, daemon=True)
    t.start()
    print(f"✨ Ultimate Web Dashboard started on port {os.environ.get('PORT', 8080)}")

# ======================================================================
# 🔥 CONFIGURATION
# ======================================================================
TOKEN = '8536678801:AAGZL_MKuj2LVsEHfol3W7S7Fp5JjR09SHw'
OWNER_ID = 6873534451
ADMIN_ID = 6873534451
YOUR_USERNAME = '@Zinko158'
UPDATE_CHANNEL = 'https://t.me/+NLb-9NFUSiY1YjVl'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_BOTS_DIR = os.path.join(BASE_DIR, 'upload_bots')
IROTECH_DIR = os.path.join(BASE_DIR, 'inf')
DATABASE_PATH = os.path.join(IROTECH_DIR, 'bot_data.db')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
NPM_CACHE_DIR = os.path.join(BASE_DIR, 'npm_cache')
PIP_CACHE_DIR = os.path.join(BASE_DIR, 'pip_cache')

for dir_path in [UPLOAD_BOTS_DIR, IROTECH_DIR, LOGS_DIR, NPM_CACHE_DIR, PIP_CACHE_DIR]:
    os.makedirs(dir_path, exist_ok=True)

FREE_USER_LIMIT = 5
SUBSCRIBED_USER_LIMIT = 15
ADMIN_LIMIT = 999
OWNER_LIMIT = float('inf')
PREMIUM_USER_LIMIT = 30

bot = telebot.TeleBot(TOKEN)

bot_scripts = {}
user_subscriptions = {}
user_files = {}
active_users = set()
admin_ids = {OWNER_ID}
bot_locked = False
maintenance_mode = False
start_time = time.time()

script_executor = ThreadPoolExecutor(max_workers=5)  # Increased for more power
broadcast_queue = Queue()
log_cleanup_queue = Queue()

# ======================================================================
# 🔥 ULTIMATE LOGGING SYSTEM
# ======================================================================
class UltimateColoredFormatter(logging.Formatter):
    """Premium colored logging with emojis"""
    grey = "\x1b[38;21m"
    blue = "\x1b[38;5;39m"
    yellow = "\x1b[38;5;226m"
    red = "\x1b[38;5;196m"
    bold_red = "\x1b[31;1m"
    green = "\x1b[38;5;40m"
    cyan = "\x1b[38;5;51m"
    purple = "\x1b[38;5;129m"
    orange = "\x1b[38;5;214m"
    pink = "\x1b[38;5;205m"
    reset = "\x1b[0m"
    
    EMOJIS = {
        logging.DEBUG: "🐛",
        logging.INFO: "📘",
        logging.WARNING: "⚠️",
        logging.ERROR: "❌",
        logging.CRITICAL: "💥"
    }
    
    FORMATS = {
        logging.DEBUG: grey + "[🐛 DEBUG] %(message)s" + reset,
        logging.INFO: green + "[📘 INFO] %(message)s" + reset,
        logging.WARNING: yellow + "[⚠️ WARNING] %(message)s" + reset,
        logging.ERROR: red + "[❌ ERROR] %(message)s" + reset,
        logging.CRITICAL: bold_red + "[💥 CRITICAL] %(message)s" + reset
    }
    
    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        emoji = self.EMOJIS.get(record.levelno, "")
        record.msg = f"{emoji} {record.msg}"
        formatter = logging.Formatter(log_fmt, datefmt='%Y-%m-%d %H:%M:%S')
        return formatter.format(record)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(UltimateColoredFormatter())
logger.addHandler(console_handler)

log_file = os.path.join(LOGS_DIR, f'bot_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
))
logger.addHandler(file_handler)

# ======================================================================
# 🔥 ULTIMATE DATABASE MANAGER
# ======================================================================
class UltimateDatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.local = threading.local()
        self._init_db()
    
    def get_connection(self):
        if not hasattr(self.local, 'connection'):
            self.local.connection = sqlite3.connect(self.db_path, timeout=30)
            self.local.connection.row_factory = sqlite3.Row
        return self.local.connection
    
    def _init_db(self):
        with self.get_connection() as conn:
            c = conn.cursor()
            # Subscriptions table
            c.execute('''CREATE TABLE IF NOT EXISTS subscriptions
                         (user_id INTEGER PRIMARY KEY, 
                          expiry TEXT,
                          tier TEXT DEFAULT 'basic',
                          added_by INTEGER,
                          added_date TEXT)''')
            
            # User files table with enhanced fields
            c.execute('''CREATE TABLE IF NOT EXISTS user_files
                         (user_id INTEGER, 
                          file_name TEXT,
                          file_type TEXT,
                          file_size INTEGER,
                          upload_date TEXT,
                          last_run TEXT,
                          run_count INTEGER DEFAULT 0,
                          total_runtime INTEGER DEFAULT 0,
                          status TEXT DEFAULT 'idle',
                          pid INTEGER,
                          PRIMARY KEY (user_id, file_name))''')
            
            # Active users table
            c.execute('''CREATE TABLE IF NOT EXISTS active_users
                         (user_id INTEGER PRIMARY KEY,
                          username TEXT,
                          first_name TEXT,
                          last_seen TEXT,
                          join_date TEXT,
                          total_uploads INTEGER DEFAULT 0,
                          total_runs INTEGER DEFAULT 0,
                          premium_status TEXT DEFAULT 'free')''')
            
            # Admins table
            c.execute('''CREATE TABLE IF NOT EXISTS admins
                         (user_id INTEGER PRIMARY KEY,
                          added_by INTEGER,
                          added_date TEXT,
                          permissions TEXT DEFAULT 'standard')''')
            
            # Script runs history
            c.execute('''CREATE TABLE IF NOT EXISTS script_runs
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          user_id INTEGER,
                          file_name TEXT,
                          start_time TEXT,
                          end_time TEXT,
                          status TEXT,
                          pid INTEGER,
                          exit_code INTEGER,
                          memory_usage INTEGER)''')
            
            # Settings
            c.execute('''CREATE TABLE IF NOT EXISTS settings
                         (key TEXT PRIMARY KEY,
                          value TEXT)''')
            
            # System metrics
            c.execute('''CREATE TABLE IF NOT EXISTS system_metrics
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          timestamp TEXT,
                          cpu_usage REAL,
                          memory_usage REAL,
                          disk_usage REAL,
                          active_scripts INTEGER)''')
            
            # Default settings
            c.execute('INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)',
                      ('bot_locked', 'false'))
            c.execute('INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)',
                      ('maintenance_mode', 'false'))
            c.execute('INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)',
                      ('total_scripts_run', '0'))
            conn.commit()
        
        logger.info("✅ Ultimate Database initialized with premium schema")

# ======================================================================
# 🔥 CREATE DATABASE MANAGER INSTANCE
# ======================================================================
db_manager = UltimateDatabaseManager(DATABASE_PATH)

# ======================================================================
# 🔥 LOAD ALL DATA FROM DATABASE
# ======================================================================
def load_all_data():
    global user_subscriptions, user_files, active_users, admin_ids, bot_locked
    
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        
        # Load subscriptions
        c.execute('SELECT user_id, expiry, tier FROM subscriptions')
        for row in c.fetchall():
            try:
                expiry = datetime.fromisoformat(row['expiry'])
                if expiry > datetime.now():
                    user_subscriptions[row['user_id']] = {
                        'expiry': expiry,
                        'tier': row['tier']
                    }
            except:
                pass
        
        # Load user files - only select existing columns (status and pid exist but we don't need them for cache)
        c.execute('SELECT user_id, file_name, file_type FROM user_files')
        for row in c.fetchall():
            user_files.setdefault(row['user_id'], []).append(
                (row['file_name'], row['file_type'])
            )
        
        # Load active users
        c.execute('SELECT user_id FROM active_users')
        for row in c.fetchall():
            active_users.add(row['user_id'])
        
        # Load admins
        c.execute('SELECT user_id FROM admins')
        for row in c.fetchall():
            admin_ids.add(row['user_id'])
        admin_ids.add(OWNER_ID)
        
        # Load bot_locked
        c.execute('SELECT value FROM settings WHERE key = "bot_locked"')
        row = c.fetchone()
        if row:
            bot_locked = row['value'] == 'true'
    
    logger.info(f"📊 Loaded: {len(user_subscriptions)} premium users, {len(active_users)} active users, {len(admin_ids)} admins")

load_all_data()

# ======================================================================
# 🔥 ULTIMATE HELPER FUNCTIONS (FIXED)
# ======================================================================
def get_user_folder(user_id):
    """Get or create user folder"""
    user_folder = os.path.join(UPLOAD_BOTS_DIR, str(user_id))
    os.makedirs(user_folder, exist_ok=True)
    return user_folder

def get_user_file_limit(user_id):
    """Get file limit based on user status"""
    if user_id == OWNER_ID: 
        return float('inf')
    if user_id in admin_ids: 
        return ADMIN_LIMIT
    if user_id in user_subscriptions:
        expiry = user_subscriptions[user_id].get('expiry', datetime.min)
        if expiry > datetime.now():
            return SUBSCRIBED_USER_LIMIT
    return FREE_USER_LIMIT

def get_user_file_count(user_id):
    """Get accurate file count from DB"""
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM user_files WHERE user_id = ?', (user_id,))
        return c.fetchone()[0]

def get_node_version():
    """Get Node.js version"""
    try:
        result = subprocess.run(['node', '--version'], 
                              capture_output=True, text=True, timeout=5)
        return result.stdout.strip() or 'Not installed'
    except:
        return 'Not installed'

def get_npm_version():
    """Get npm version"""
    try:
        result = subprocess.run(['npm', '--version'], 
                              capture_output=True, text=True, timeout=5)
        return result.stdout.strip() or 'Not installed'
    except:
        return 'Not installed'

def format_size(bytes_val):
    """Format bytes to human readable - FIXED: handle None and non-numeric"""
    if bytes_val is None:
        return "0 B"
    try:
        bytes_val = float(bytes_val)
        if bytes_val < 0:
            bytes_val = 0
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_val < 1024.0:
                return f"{bytes_val:.2f} {unit}"
            bytes_val /= 1024.0
        return f"{bytes_val:.2f} PB"
    except (TypeError, ValueError):
        return "0 B"

def format_time(seconds):
    """Format seconds to human readable"""
    return str(timedelta(seconds=int(seconds)))

def generate_unique_id(length=8):
    """Generate unique ID for logs"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def get_system_stats():
    """Get comprehensive system statistics - FIXED: handle permission errors"""
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        net = psutil.net_io_counters()
        
        # boot_time might raise PermissionError on some systems
        try:
            boot_time = datetime.fromtimestamp(psutil.boot_time()).isoformat()
        except:
            boot_time = datetime.now().isoformat()
        
        return {
            'cpu': cpu_percent,
            'cpu_count': psutil.cpu_count(),
            'memory_used': memory.used,
            'memory_total': memory.total,
            'memory_percent': memory.percent,
            'disk_used': disk.used,
            'disk_total': disk.total,
            'disk_percent': disk.percent,
            'net_sent': net.bytes_sent,
            'net_recv': net.bytes_recv,
            'processes': len(psutil.pids()),
            'boot_time': boot_time
        }
    except:
        return {}

def is_bot_running(owner_id, file_name):
    """Check if a specific script is running"""
    script_key = f"{owner_id}_{file_name}"
    script_info = bot_scripts.get(script_key)
    
    if script_info and script_info.get('process'):
        try:
            proc = psutil.Process(script_info['process'].pid)
            return proc.is_running() and proc.status() != psutil.STATUS_ZOMBIE
        except:
            if script_key in bot_scripts:
                del bot_scripts[script_key]
            return False
    return False

def kill_process_tree(process_info):
    """Kill process and all its children"""
    try:
        # Close log file if open
        if 'log_file' in process_info and process_info['log_file'] and not process_info['log_file'].closed:
            try:
                process_info['log_file'].close()
            except:
                pass
        
        process = process_info.get('process')
        if process and hasattr(process, 'pid'):
            pid = process.pid
            try:
                parent = psutil.Process(pid)
                children = parent.children(recursive=True)
                
                # Kill children first
                for child in children:
                    try:
                        child.terminate()
                    except:
                        try:
                            child.kill()
                        except:
                            pass
                
                # Kill parent
                parent.terminate()
                try:
                    parent.wait(timeout=3)
                except:
                    parent.kill()
                
                logger.info(f"✅ Killed process tree (PID: {pid})")
            except psutil.NoSuchProcess:
                pass
    except Exception as e:
        logger.error(f"Error killing process: {e}")

# ======================================================================
# 🔥 ULTIMATE FILE MANAGER
# ======================================================================
class UltimateFileManager:
    """Premium file management system"""
    
    @staticmethod
    def save_file(user_id, file_content, file_name):
        """Save file with duplicate handling"""
        user_folder = get_user_folder(user_id)
        file_path = os.path.join(user_folder, file_name)
        file_size = len(file_content)
        
        # Handle duplicates
        if os.path.exists(file_path):
            base, ext = os.path.splitext(file_name)
            counter = 1
            while os.path.exists(os.path.join(user_folder, f"{base}_{counter}{ext}")):
                counter += 1
            file_name = f"{base}_{counter}{ext}"
            file_path = os.path.join(user_folder, file_name)
        
        # Save file
        with open(file_path, 'wb') as f:
            f.write(file_content)
        
        # Update database - status column exists
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('''INSERT OR REPLACE INTO user_files 
                         (user_id, file_name, file_type, file_size, upload_date, status)
                         VALUES (?, ?, ?, ?, ?, ?)''',
                      (user_id, file_name, os.path.splitext(file_name)[1][1:].lower(), 
                       file_size, datetime.now().isoformat(), 'idle'))
            conn.commit()
        
        # Update cache
        user_files.setdefault(user_id, [])
        user_files[user_id] = [(f, t) for f, t in user_files[user_id] if f != file_name]
        user_files[user_id].append((file_name, os.path.splitext(file_name)[1][1:].lower()))
        
        logger.info(f"✅ File saved: {file_name} ({format_size(file_size)}) for user {user_id}")
        return file_path, file_size, file_name

    @staticmethod
    def delete_file(user_id, file_name):
        """Delete file and all related logs"""
        user_folder = get_user_folder(user_id)
        file_path = os.path.join(user_folder, file_name)
        
        # Delete main file
        if os.path.exists(file_path):
            os.remove(file_path)
        
        # Delete all related log files
        for f in os.listdir(user_folder):
            if f.startswith(os.path.splitext(file_name)[0]) and f.endswith('.log'):
                os.remove(os.path.join(user_folder, f))
        
        # Update database
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('DELETE FROM user_files WHERE user_id = ? AND file_name = ?',
                      (user_id, file_name))
            conn.commit()
        
        # Update cache
        if user_id in user_files:
            user_files[user_id] = [f for f in user_files[user_id] if f[0] != file_name]
            if not user_files[user_id]:
                del user_files[user_id]
        
        logger.info(f"🗑️ File deleted: {file_name} for user {user_id}")
        return True

    @staticmethod
    def get_file_info(user_id, file_name):
        """Get detailed file information"""
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('''SELECT * FROM user_files 
                        WHERE user_id = ? AND file_name = ?''',
                     (user_id, file_name))
            return c.fetchone()

# ======================================================================
# 🔥 ULTIMATE SCRIPT RUNNER WITH PM2 STYLE MANAGEMENT
# ======================================================================
class UltimateScriptRunner:
    """Premium script runner with advanced features"""
    
    def __init__(self):
        self.running_scripts = {}
        self.script_queue = Queue()
        self.start_worker()
        self.start_monitor()
    
    def start_worker(self):
        """Start script execution worker"""
        def worker():
            while True:
                try:
                    script_info = self.script_queue.get()
                    self._execute_script(script_info)
                except Exception as e:
                    logger.error(f"Script worker error: {e}")
                time.sleep(0.1)
        thread = Thread(target=worker, daemon=True)
        thread.start()
        logger.info("🚀 Script runner worker started")
    
    def start_monitor(self):
        """Monitor running scripts and update stats"""
        def monitor():
            while True:
                try:
                    for script_key, info in list(bot_scripts.items()):
                        try:
                            if info.get('process'):
                                proc = psutil.Process(info['process'].pid)
                                if not proc.is_running() or proc.status() == psutil.STATUS_ZOMBIE:
                                    # Process died, clean up
                                    self._cleanup_script(script_key, info)
                        except:
                            self._cleanup_script(script_key, info)
                except Exception as e:
                    logger.error(f"Monitor error: {e}")
                time.sleep(5)  # Check every 5 seconds
        thread = Thread(target=monitor, daemon=True)
        thread.start()
        logger.info("📊 Script monitor started")
    
    def _cleanup_script(self, script_key, info):
        """Clean up finished script"""
        try:
            if script_key in bot_scripts:
                # Update database
                with db_manager.get_connection() as conn:
                    c = conn.cursor()
                    c.execute('''UPDATE user_files 
                                SET status = 'idle', pid = NULL, last_run = ?
                                WHERE user_id = ? AND file_name = ?''',
                              (datetime.now().isoformat(), info['user_id'], info['file_name']))
                    
                    c.execute('''UPDATE script_runs SET end_time = ?, status = ? 
                                 WHERE user_id = ? AND file_name = ? AND status = 'running' ''',
                              (datetime.now().isoformat(), 'finished', 
                               info['user_id'], info['file_name']))
                    conn.commit()
                
                del bot_scripts[script_key]
                logger.info(f"✅ Cleaned up script: {info['file_name']}")
        except Exception as e:
            logger.error(f"Cleanup error: {e}")
    
    def _execute_script(self, script_info):
        """Execute script with all premium features"""
        script_path, user_id, user_folder, file_name, message, file_type = script_info
        script_key = f"{user_id}_{file_name}"
        chat_id = message.chat.id if message else None
        
        # Check Node.js for JS scripts
        if file_type == 'js':
            if not self._check_node(chat_id):
                return
            self._run_npm_install_if_needed(user_folder, chat_id)
        
        try:
            # Prepare environment
            env = os.environ.copy()
            env['PYTHONUNBUFFERED'] = '1'
            env['NODE_ENV'] = 'production'
            
            if file_type == 'js':
                node_modules = os.path.join(user_folder, 'node_modules')
                if os.path.exists(node_modules):
                    env['NODE_PATH'] = node_modules + (':' + env.get('NODE_PATH', '') if 'NODE_PATH' in env else '')
            
            # Create log file with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}_{timestamp}.log")
            log_file = open(log_path, 'w', encoding='utf-8')
            
            # Start process
            if file_type == 'py':
                process = subprocess.Popen(
                    [sys.executable, script_path],
                    cwd=user_folder,
                    stdout=log_file,
                    stderr=log_file,
                    stdin=subprocess.PIPE,
                    env=env,
                    text=True,
                    errors='ignore'
                )
            else:  # js
                process = subprocess.Popen(
                    ['node', script_path],
                    cwd=user_folder,
                    stdout=log_file,
                    stderr=log_file,
                    stdin=subprocess.PIPE,
                    env=env,
                    text=True,
                    errors='ignore'
                )
            
            # Store script info
            script_info_dict = {
                'process': process,
                'log_file': log_file,
                'log_path': log_path,
                'file_name': file_name,
                'user_id': user_id,
                'start_time': datetime.now(),
                'user_folder': user_folder,
                'type': file_type,
                'script_key': script_key,
                'pid': process.pid,
                'status': 'running'
            }
            bot_scripts[script_key] = script_info_dict
            
            # Update database
            with db_manager.get_connection() as conn:
                c = conn.cursor()
                c.execute('''UPDATE user_files 
                            SET status = 'running', pid = ?, last_run = ?, run_count = run_count + 1
                            WHERE user_id = ? AND file_name = ?''',
                          (process.pid, datetime.now().isoformat(), user_id, file_name))
                
                c.execute('''INSERT INTO script_runs 
                            (user_id, file_name, start_time, status, pid)
                            VALUES (?, ?, ?, ?, ?)''',
                         (user_id, file_name, datetime.now().isoformat(), 'running', process.pid))
                
                c.execute('''UPDATE active_users 
                            SET total_runs = total_runs + 1, last_seen = ?
                            WHERE user_id = ?''',
                         (datetime.now().isoformat(), user_id))
                conn.commit()
            
            logger.info(f"✅ Started {file_type.upper()} script: {file_name} (PID: {process.pid})")
            
            # Notify user
            if chat_id:
                markup = types.InlineKeyboardMarkup(row_width=2)
                markup.add(
                    types.InlineKeyboardButton("📊 Monitor", callback_data=f'cpu_{user_id}_{file_name}'),
                    types.InlineKeyboardButton("📜 Logs", callback_data=f'logs_{user_id}_{file_name}'),
                    types.InlineKeyboardButton("🛑 Stop", callback_data=f'stop_{user_id}_{file_name}'),
                    types.InlineKeyboardButton("🔙 Back", callback_data='back_to_main')
                )
                bot.send_message(
                    chat_id, 
                    f"🚀 **Script Started Successfully!**\n\n"
                    f"📄 **File:** `{file_name}`\n"
                    f"🆔 **PID:** `{process.pid}`\n"
                    f"⏱️ **Started:** {datetime.now().strftime('%H:%M:%S')}\n\n"
                    f"Use the buttons below to monitor:",
                    parse_mode='Markdown',
                    reply_markup=markup
                )
            
        except Exception as e:
            logger.error(f"❌ Failed to start script {file_name}: {e}")
            if chat_id:
                bot.send_message(chat_id, f"❌ Failed to start script: {e}")
    
    def _check_node(self, chat_id):
        """Check if Node.js is installed"""
        try:
            result = subprocess.run(['node', '--version'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                return True
            else:
                raise Exception("Node.js not found")
        except:
            if chat_id:
                bot.send_message(chat_id, "❌ **Node.js is not installed** on the server. Please contact admin.", parse_mode='Markdown')
            return False
    
    def _run_npm_install_if_needed(self, user_folder, chat_id):
        """Run npm install if package.json exists"""
        package_json = os.path.join(user_folder, 'package.json')
        if os.path.exists(package_json):
            def install():
                try:
                    if chat_id:
                        bot.send_message(chat_id, "📦 **Found package.json, running npm install...**", parse_mode='Markdown')
                    
                    result = subprocess.run(
                        ['npm', 'install', '--cache', NPM_CACHE_DIR],
                        cwd=user_folder,
                        capture_output=True,
                        text=True,
                        timeout=120
                    )
                    
                    if result.returncode == 0:
                        if chat_id:
                            bot.send_message(chat_id, "✅ **npm install completed successfully.**", parse_mode='Markdown')
                    else:
                        error = result.stderr[:500]
                        if chat_id:
                            bot.send_message(chat_id, f"⚠️ **npm install had issues:**\n`{error}`", parse_mode='Markdown')
                except subprocess.TimeoutExpired:
                    if chat_id:
                        bot.send_message(chat_id, "⚠️ **npm install timed out.**", parse_mode='Markdown')
                except Exception as e:
                    if chat_id:
                        bot.send_message(chat_id, f"❌ **npm install error:** {e}", parse_mode='Markdown')
            
            Thread(target=install, daemon=True).start()
    
    def run_script(self, script_path, user_id, user_folder, file_name, message, file_type='py'):
        """Queue script for execution"""
        self.script_queue.put((script_path, user_id, user_folder, file_name, message, file_type))
        return f"🔄 Script '{file_name}' queued for execution"

# Initialize ultimate script runner
script_runner = UltimateScriptRunner()

# Compatibility wrappers
def run_script(script_path, user_id, user_folder, file_name, message):
    script_runner.run_script(script_path, user_id, user_folder, file_name, message, 'py')

def run_js_script(script_path, user_id, user_folder, file_name, message):
    script_runner.run_script(script_path, user_id, user_folder, file_name, message, 'js')

# ======================================================================
# 🔥 ULTIMATE PACKAGE INSTALLER (FIXED)
# ======================================================================
class UltimatePackageInstaller:
    """Premium package installer with queue system"""
    
    def __init__(self):
        self.install_lock = threading.Lock()
        self.install_queue = Queue()
        self.start_installer()
    
    def start_installer(self):
        """Start package installer worker"""
        def worker():
            while True:
                try:
                    pkg_info = self.install_queue.get()
                    self._install_package(pkg_info)
                except Exception as e:
                    logger.error(f"Package installer error: {e}")
                time.sleep(0.5)
        thread = Thread(target=worker, daemon=True)
        thread.start()
        logger.info("📦 Package installer started")
    
    def _install_package(self, pkg_info):
        """Install package with progress tracking"""
        package, user_id, message, pkg_type = pkg_info
        chat_id = message.chat.id
        
        with self.install_lock:
            try:
                if pkg_type == 'python':
                    status_msg = bot.reply_to(message, f"🐍 **Installing Python package:** `{package}`...", parse_mode='Markdown')
                    
                    result = subprocess.run(
                        [sys.executable, '-m', 'pip', 'install', '--cache-dir', PIP_CACHE_DIR, package],
                        capture_output=True, text=True, timeout=120
                    )
                else:  # node
                    status_msg = bot.reply_to(message, f"📦 **Installing Node package:** `{package}`...", parse_mode='Markdown')
                    user_folder = get_user_folder(user_id)
                    
                    # Check if npm exists
                    try:
                        subprocess.run(['npm', '--version'], capture_output=True, check=True)
                    except:
                        bot.edit_message_text(
                            f"❌ **npm is not installed** on the server.\n\nCannot install Node packages.",
                            chat_id, status_msg.message_id,
                            parse_mode='Markdown'
                        )
                        return
                    
                    result = subprocess.run(
                        ['npm', 'install', '--cache', NPM_CACHE_DIR, package],
                        cwd=user_folder, capture_output=True, text=True, timeout=120
                    )
                
                if result.returncode == 0:
                    bot.edit_message_text(
                        f"✅ **Package Installed Successfully!**\n\n"
                        f"📦 **Package:** `{package}`\n"
                        f"📊 **Type:** {pkg_type.upper()}",
                        chat_id, status_msg.message_id,
                        parse_mode='Markdown'
                    )
                else:
                    error_msg = result.stderr[:500] if result.stderr else "Unknown error"
                    bot.edit_message_text(
                        f"❌ **Installation Failed**\n\n"
                        f"📦 **Package:** `{package}`\n"
                        f"⚠️ **Error:**\n`{error_msg}`",
                        chat_id, status_msg.message_id,
                        parse_mode='Markdown'
                    )
            except subprocess.TimeoutExpired:
                bot.edit_message_text(
                    f"⚠️ **Installation Timeout**\n\n"
                    f"📦 **Package:** `{package}`\n"
                    f"⏱️ **Time:** 120s",
                    chat_id, status_msg.message_id,
                    parse_mode='Markdown'
                )
            except Exception as e:
                bot.edit_message_text(
                    f"❌ **Installation Error**\n\n"
                    f"📦 **Package:** `{package}`\n"
                    f"⚠️ **Error:** {e}",
                    chat_id, status_msg.message_id,
                    parse_mode='Markdown'
                )
    
    def install_package(self, package, user_id, message, pkg_type='python'):
        """Queue package for installation"""
        self.install_queue.put((package, user_id, message, pkg_type))

package_installer = UltimatePackageInstaller()

# ======================================================================
# 🔥 ULTIMATE MODULE MAPPING
# ======================================================================
TELEGRAM_MODULES = {
    'telebot': 'pyTelegramBotAPI',
    'telegram': 'python-telegram-bot',
    'aiogram': 'aiogram',
    'pyrogram': 'pyrogram',
    'telethon': 'telethon',
}

COMMON_MODULES = {
    'requests': 'requests',
    'flask': 'Flask',
    'django': 'Django',
    'fastapi': 'fastapi',
    'aiohttp': 'aiohttp',
    'numpy': 'numpy',
    'pandas': 'pandas',
    'pillow': 'Pillow',
    'opencv': 'opencv-python',
    'tensorflow': 'tensorflow',
    'torch': 'torch',
    'discord': 'discord.py',
    'selenium': 'selenium',
    'beautifulsoup4': 'beautifulsoup4',
    'pymongo': 'pymongo',
    'redis': 'redis',
    'sqlalchemy': 'SQLAlchemy',
}

ALL_MODULES = {**TELEGRAM_MODULES, **COMMON_MODULES}

# ======================================================================
# 🔥 ULTIMATE INLINE KEYBOARD MENUS
# ======================================================================

def create_main_menu_inline(user_id):
    """Create premium main menu with inline buttons"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Main buttons
    buttons = [
        types.InlineKeyboardButton('📢 UPDATES', url=UPDATE_CHANNEL),
        types.InlineKeyboardButton('📤 UPLOAD', callback_data='upload'),
        types.InlineKeyboardButton('📂 MY FILES', callback_data='check_files'),
        types.InlineKeyboardButton('⚡ SPEED TEST', callback_data='speed'),
        types.InlineKeyboardButton('📊 STATISTICS', callback_data='stats'),
        types.InlineKeyboardButton('💳 PREMIUM', callback_data='premium_info'),
        types.InlineKeyboardButton('📞 SUPPORT', url=f'https://t.me/{YOUR_USERNAME.replace("@", "")}'),
        types.InlineKeyboardButton('ℹ️ ABOUT', callback_data='about'),
        types.InlineKeyboardButton('🛠️ TOOLS', callback_data='tools'),
        types.InlineKeyboardButton('🆘 HELP', callback_data='help')
    ]
    
    # Admin buttons
    if user_id in admin_ids:
        admin_buttons = [
            types.InlineKeyboardButton('👑 ADMIN PANEL', callback_data='admin_panel'),
            types.InlineKeyboardButton('🔒 LOCK' if not bot_locked else '🔓 UNLOCK', 
                                     callback_data='lock_bot' if not bot_locked else 'unlock_bot'),
            types.InlineKeyboardButton('📢 BROADCAST', callback_data='broadcast'),
            types.InlineKeyboardButton('📊 SYSTEM', callback_data='system_stats'),
            types.InlineKeyboardButton('🔄 RUN ALL', callback_data='run_all_scripts'),
            types.InlineKeyboardButton('🛑 STOP ALL', callback_data='stop_all_scripts'),
            types.InlineKeyboardButton('🧹 CLEAN LOGS', callback_data='clean_logs'),
            types.InlineKeyboardButton('🔄 RESTART BOT', callback_data='restart_bot')
        ]
        
        # Build admin layout
        markup.row(buttons[0])  # Updates
        markup.row(buttons[1], buttons[2])  # Upload, My Files
        markup.row(buttons[3], buttons[4])  # Speed, Stats
        markup.row(admin_buttons[0], admin_buttons[3])  # Admin Panel, System
        markup.row(admin_buttons[1], admin_buttons[4])  # Lock/Unlock, Run All
        markup.row(admin_buttons[2], admin_buttons[5])  # Broadcast, Stop All
        markup.row(admin_buttons[6], admin_buttons[7])  # Clean Logs, Restart
        markup.row(buttons[5], buttons[6])  # Premium, Support
        markup.row(buttons[7], buttons[8])  # About, Tools
        markup.row(buttons[9])  # Help
    else:
        # Build user layout
        markup.row(buttons[0])  # Updates
        markup.row(buttons[1], buttons[2])  # Upload, My Files
        markup.row(buttons[3], buttons[4])  # Speed, Stats
        markup.row(buttons[5], buttons[6])  # Premium, Support
        markup.row(buttons[7], buttons[8])  # About, Tools
        markup.row(buttons[9])  # Help
    
    return markup

def create_file_management_buttons(script_owner_id, file_name, is_running):
    """Create premium file management buttons"""
    markup = types.InlineKeyboardMarkup(row_width=3)
    
    if is_running:
        # Running state buttons
        markup.row(
            types.InlineKeyboardButton("🛑 STOP", callback_data=f'stop_{script_owner_id}_{file_name}'),
            types.InlineKeyboardButton("🔄 RESTART", callback_data=f'restart_{script_owner_id}_{file_name}'),
            types.InlineKeyboardButton("📊 CPU", callback_data=f'cpu_{script_owner_id}_{file_name}')
        )
        markup.row(
            types.InlineKeyboardButton("📜 LOGS", callback_data=f'logs_{script_owner_id}_{file_name}'),
            types.InlineKeyboardButton("🗑️ DELETE", callback_data=f'delete_{script_owner_id}_{file_name}'),
            types.InlineKeyboardButton("⏱️ UPTIME", callback_data=f'uptime_{script_owner_id}_{file_name}')
        )
        markup.row(
            types.InlineKeyboardButton("💾 MEMORY", callback_data=f'memory_{script_owner_id}_{file_name}'),
            types.InlineKeyboardButton("📊 DETAILS", callback_data=f'details_{script_owner_id}_{file_name}'),
            types.InlineKeyboardButton("🔄 REFRESH", callback_data=f'refresh_{script_owner_id}_{file_name}')
        )
    else:
        # Stopped state buttons
        markup.row(
            types.InlineKeyboardButton("▶️ START", callback_data=f'start_{script_owner_id}_{file_name}'),
            types.InlineKeyboardButton("🗑️ DELETE", callback_data=f'delete_{script_owner_id}_{file_name}'),
            types.InlineKeyboardButton("📜 LOGS", callback_data=f'logs_{script_owner_id}_{file_name}')
        )
    
    # Installation buttons
    markup.row(
        types.InlineKeyboardButton("📦 NPM INSTALL", callback_data=f'install_npm_{script_owner_id}_{file_name}'),
        types.InlineKeyboardButton("🐍 PIP INSTALL", callback_data=f'install_pip_{script_owner_id}_{file_name}')
    )
    
    # Navigation
    markup.row(
        types.InlineKeyboardButton("📂 BACK TO FILES", callback_data='check_files'),
        types.InlineKeyboardButton("🏠 MAIN MENU", callback_data='back_to_main')
    )
    
    return markup

def create_admin_panel():
    """Create premium admin panel"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Admin management
    markup.row(
        types.InlineKeyboardButton('➕ ADD ADMIN', callback_data='add_admin'),
        types.InlineKeyboardButton('➖ REMOVE ADMIN', callback_data='remove_admin')
    )
    markup.row(
        types.InlineKeyboardButton('📋 LIST ADMINS', callback_data='list_admins'),
        types.InlineKeyboardButton('🔧 PERMISSIONS', callback_data='admin_permissions')
    )
    
    # Subscription management
    markup.row(
        types.InlineKeyboardButton('💳 ADD PREMIUM', callback_data='add_subscription'),
        types.InlineKeyboardButton('💳 REMOVE PREMIUM', callback_data='remove_subscription')
    )
    markup.row(
        types.InlineKeyboardButton('🔍 CHECK SUB', callback_data='check_subscription'),
        types.InlineKeyboardButton('📊 SUB STATS', callback_data='subscription_stats')
    )
    
    # System management
    markup.row(
        types.InlineKeyboardButton('📊 SYSTEM STATS', callback_data='system_stats'),
        types.InlineKeyboardButton('🧹 CLEAN LOGS', callback_data='clean_logs')
    )
    markup.row(
        types.InlineKeyboardButton('🔄 RESTART BOT', callback_data='restart_bot'),
        types.InlineKeyboardButton('⚠️ MAINTENANCE', callback_data='maintenance_mode')
    )
    
    # Navigation
    markup.row(
        types.InlineKeyboardButton('📊 BOT STATS', callback_data='stats'),
        types.InlineKeyboardButton('🏠 MAIN MENU', callback_data='back_to_main')
    )
    
    return markup

def create_script_list_buttons(user_id, files):
    """Create paginated script list buttons"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    for fname, ftype in files[:8]:  # Show 8 files per page
        is_running = is_bot_running(user_id, fname)
        status_icon = "🟢" if is_running else "🔴"
        file_icon = "🐍" if ftype == 'py' else "🟨"
        btn_text = f"{file_icon} {status_icon} {fname[:15]}..."
        markup.add(types.InlineKeyboardButton(
            btn_text, 
            callback_data=f'file_{user_id}_{fname}'
        ))
    
    # Navigation
    nav_buttons = []
    if len(files) > 8:
        nav_buttons.append(types.InlineKeyboardButton("▶️ NEXT", callback_data='files_next'))
    nav_buttons.append(types.InlineKeyboardButton("📤 UPLOAD", callback_data='upload'))
    nav_buttons.append(types.InlineKeyboardButton("🏠 MAIN", callback_data='back_to_main'))
    
    markup.row(*nav_buttons)
    return markup

# ======================================================================
# 🔥 DATABASE HELPERS
# ======================================================================
def save_subscription(user_id, expiry, tier='premium'):
    """Save user subscription"""
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        expiry_str = expiry.isoformat()
        c.execute('''INSERT OR REPLACE INTO subscriptions 
                     (user_id, expiry, tier, added_date)
                     VALUES (?, ?, ?, ?)''',
                  (user_id, expiry_str, tier, datetime.now().isoformat()))
        
        c.execute('''UPDATE active_users SET premium_status = ? 
                     WHERE user_id = ?''', (tier, user_id))
        conn.commit()
    
    user_subscriptions[user_id] = {'expiry': expiry, 'tier': tier}
    logger.info(f"💳 Subscription added for user {user_id} until {expiry}")

def remove_subscription_db(user_id):
    """Remove user subscription"""
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('DELETE FROM subscriptions WHERE user_id = ?', (user_id,))
        c.execute('''UPDATE active_users SET premium_status = 'free' 
                     WHERE user_id = ?''', (user_id,))
        conn.commit()
    
    if user_id in user_subscriptions:
        del user_subscriptions[user_id]
    logger.info(f"💳 Subscription removed for user {user_id}")

# ======================================================================
# 🔥 MESSAGE HANDLERS
# ======================================================================

@bot.message_handler(commands=['start', 'menu'])
def command_send_welcome(message):
    """Handle /start and /menu commands"""
    user_id = message.from_user.id
    chat_id = message.chat.id
    user_name = message.from_user.first_name or "User"
    user_username = message.from_user.username
    
    # Check if bot is locked
    if bot_locked and user_id not in admin_ids:
        bot.send_message(
            chat_id, 
            "🔒 **Bot is currently under maintenance**\nPlease try again later.", 
            parse_mode='Markdown'
        )
        return
    
    # Register new user
    if user_id not in active_users:
        active_users.add(user_id)
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('''INSERT OR REPLACE INTO active_users 
                         (user_id, username, first_name, last_seen, join_date)
                         VALUES (?, ?, ?, ?, ?)''',
                      (user_id, user_username, user_name, 
                       datetime.now().isoformat(), datetime.now().isoformat()))
            conn.commit()
        
        # Notify owner
        try:
            notification = (
                f"🎉 **New User Joined!**\n\n"
                f"👤 **Name:** {user_name}\n"
                f"🆔 **ID:** `{user_id}`\n"
                f"✳️ **Username:** @{user_username or 'N/A'}\n"
                f"📅 **Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
            bot.send_message(OWNER_ID, notification, parse_mode='Markdown')
        except Exception as e:
            logger.error(f"Failed to notify owner: {e}")
    
    # Get user stats
    file_limit = get_user_file_limit(user_id)
    current_files = get_user_file_count(user_id)
    limit_display = "∞" if file_limit == float('inf') else str(file_limit)
    
    # Determine user status
    if user_id == OWNER_ID:
        user_status = "👑 **OWNER**"
    elif user_id in admin_ids:
        user_status = "🛡️ **ADMIN**"
    elif user_id in user_subscriptions:
        expiry = user_subscriptions[user_id].get('expiry')
        if expiry and expiry > datetime.now():
            days_left = (expiry - datetime.now()).days
            user_status = f"⭐ **PREMIUM** ({days_left} days left)"
        else:
            user_status = "🆓 **FREE**"
            if expiry:
                remove_subscription_db(user_id)
    else:
        user_status = "🆓 **FREE**"
    
    # Create welcome message
    welcome_text = f"""
╔══════════════════════════════════════╗
║     🔥 **MARCO HOST PREMIUM** 🔥     ║
╚══════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 **User:** {user_name}
🆔 **ID:** `{user_id}`
✳️ **Username:** @{user_username or 'N/A'}
🔰 **Status:** {user_status}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 **STORAGE**
• Used: `{current_files}` / `{limit_display}` files
• Limit: {'♾️ Unlimited' if file_limit == float('inf') else f'📦 {file_limit} files'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 **PREMIUM FEATURES**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ **Python 3.11+** • Full support
✅ **Node.js 20+** • npm ecosystem
✅ **ZIP Upload** • Auto-extract
✅ **Auto Dependencies** • pip/npm
✅ **Real-time Logs** • Live monitoring
✅ **Process Control** • Start/Stop/Restart
✅ **Resource Monitor** • CPU/RAM per script
✅ **24/7 Uptime** • Enterprise grade

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 **Quick Start:**
1️⃣ Upload `.py`, `.js`, or `.zip`
2️⃣ Bot auto-detects main script
3️⃣ Installs dependencies
4️⃣ Runs 24/7 with monitoring

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👇 **Use buttons below** 👇
"""
    
    # Send welcome message
    try:
        photos = bot.get_user_profile_photos(user_id, limit=1)
        if photos.total_count > 0:
            file_id = photos.photos[0][-1].file_id
            bot.send_photo(
                chat_id, 
                file_id, 
                caption=welcome_text, 
                parse_mode='Markdown', 
                reply_markup=create_main_menu_inline(user_id)
            )
        else:
            bot.send_message(
                chat_id, 
                welcome_text, 
                parse_mode='Markdown',
                reply_markup=create_main_menu_inline(user_id)
            )
    except Exception:
        bot.send_message(
            chat_id, 
            welcome_text, 
            parse_mode='Markdown',
            reply_markup=create_main_menu_inline(user_id)
        )

@bot.message_handler(commands=['help'])
def command_help(message):
    """Handle /help command"""
    help_text = """
🆘 **HELP & SUPPORT**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📤 **UPLOADING FILES**
• Send `.py`, `.js`, or `.zip` files
• Bot automatically detects main script
• Max file size: 50MB

📂 **MANAGING FILES**
• Use `/checkfiles` to see your files
• Click on any file to manage it
• Start/Stop/Restart/Delete/Logs

🤖 **RUNNING SCRIPTS**
• Files auto-run after upload
• Monitor CPU/RAM usage
• View real-time logs
• Auto-restart on crash

📊 **COMMANDS**
• `/start` - Main menu
• `/help` - This help menu
• `/stats` - Bot statistics
• `/speed` - Speed test
• `/checkfiles` - Your files
• `/manage <filename>` - Manage file

💎 **PREMIUM**
• 15 files instead of 5
• Priority support
• More resources
• Contact @Zinko158

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    bot.reply_to(message, help_text, parse_mode='Markdown')

@bot.message_handler(commands=['stats'])
def command_stats(message):
    """Handle /stats command"""
    user_id = message.from_user.id
    chat_id = message.chat.id
    is_admin = user_id in admin_ids
    
    # Get stats
    system_stats = get_system_stats()
    total_users = len(active_users)
    
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM user_files')
        total_files = c.fetchone()[0]
        
        c.execute('SELECT COUNT(*) FROM subscriptions')
        premium_users = c.fetchone()[0]
    
    # Calculate running scripts
    running_scripts = 0
    user_scripts = 0
    for key, info in bot_scripts.items():
        if is_bot_running(info['user_id'], info['file_name']):
            running_scripts += 1
            if info['user_id'] == user_id:
                user_scripts += 1
    
    uptime_seconds = time.time() - start_time
    uptime_str = format_time(uptime_seconds)
    
    # Build stats message
    stats_text = f"""
📊 **MARCO HOST STATISTICS**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👥 **Total Users:** `{total_users:,}`
📁 **Total Files:** `{total_files:,}`
🤖 **Active Scripts:** `{running_scripts}`
💎 **Premium Users:** `{premium_users}`
⏱️ **Bot Uptime:** `{uptime_str}`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 **YOUR STATS**
• Files: `{get_user_file_count(user_id)}`
• Running: `{user_scripts}`
• Status: {'🛡️ Admin' if is_admin else '⭐ Premium' if user_id in user_subscriptions else '🆓 Free'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    # Add admin stats
    if is_admin:
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('SELECT COUNT(*) FROM active_users')
            db_users = c.fetchone()[0]
            c.execute("SELECT COUNT(*) FROM script_runs WHERE DATE(start_time) = DATE('now')")
            today_runs = c.fetchone()[0]
        
        stats_text += f"""
🔰 **ADMIN STATISTICS**

💾 **SYSTEM**
• CPU: `{system_stats.get('cpu', 0)}%`
• RAM: `{system_stats.get('memory_percent', 0)}%`
• Disk: `{system_stats.get('disk_percent', 0)}%`

📊 **DATABASE**
• Active Users: `{db_users:,}`
• Today Runs: `{today_runs:,}`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    bot.reply_to(message, stats_text, parse_mode='Markdown')

@bot.message_handler(commands=['speed'])
def command_speed(message):
    """Handle /speed command"""
    chat_id = message.chat.id
    
    # Send typing action
    bot.send_chat_action(chat_id, 'typing')
    
    # Measure API latency
    start_time_api = time.time()
    sent_msg = bot.reply_to(message, "⚡ **Testing connection speed...**", parse_mode='Markdown')
    api_latency = round((time.time() - start_time_api) * 1000, 2)
    
    # Measure download speed
    download_start = time.time()
    bot.get_me()
    download_speed = round((time.time() - download_start) * 1000, 2)
    
    # Calculate scores
    total_score = api_latency + download_speed
    if total_score < 500:
        rating = "🚀 **EXCELLENT**"
        color = "🟢"
    elif total_score < 1000:
        rating = "⚡ **GOOD**"
        color = "🟡"
    elif total_score < 2000:
        rating = "🐢 **FAIR**"
        color = "🟠"
    else:
        rating = "🐌 **POOR**"
        color = "🔴"
    
    speed_text = f"""
⚡ **SPEED TEST RESULTS**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📡 **API Latency:** `{api_latency}ms`
📥 **Download Speed:** `{download_speed}ms`
🏓 **Ping Pong:** `{api_latency * 2}ms`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 **Overall Rating:** {rating}
🎯 **Total Score:** `{total_score:.0f}ms` {color}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚦 **Bot Status:** {'🟢 ONLINE' if not bot_locked else '🔴 LOCKED'}
⏱️ **Response Time:** {'⚡ Fast' if api_latency < 500 else '🐢 Slow'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    bot.edit_message_text(speed_text, chat_id, sent_msg.message_id, parse_mode='Markdown')

@bot.message_handler(commands=['checkfiles'])
def command_checkfiles(message):
    """Handle /checkfiles command"""
    user_id = message.from_user.id
    chat_id = message.chat.id
    
    # Get files from database
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT file_name, file_type, file_size, upload_date FROM user_files WHERE user_id = ? ORDER BY upload_date DESC', (user_id,))
        files = c.fetchall()
    
    if not files:
        # No files
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📤 UPLOAD NOW", callback_data='upload'))
        markup.add(types.InlineKeyboardButton("🏠 MAIN MENU", callback_data='back_to_main'))
        
        bot.send_message(
            chat_id,
            "📂 **YOUR FILES**\n\n✨ **No files uploaded yet**\n\n📤 Upload your first file now!",
            parse_mode='Markdown',
            reply_markup=markup
        )
        return
    
    # Calculate storage
    file_count = len(files)
    limit = get_user_file_limit(user_id)
    limit_display = "∞" if limit == float('inf') else str(limit)
    
    # Build message
    message_text = f"""
📂 **YOUR FILES** ({file_count}/{limit_display})
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    for i, (fname, ftype, fsize, udate) in enumerate(files, 1):
        is_running = is_bot_running(user_id, fname)
        status = "🟢 RUNNING" if is_running else "🔴 STOPPED"
        icon = "🐍" if ftype == 'py' else "🟨" if ftype == 'js' else "📦"
        upload_time = datetime.fromisoformat(udate).strftime("%m/%d %H:%M")
        
        message_text += f"\n{icon} `{fname}`\n"
        message_text += f"   ├─ **Status:** {status}\n"
        message_text += f"   ├─ **Size:** {format_size(fsize)}\n"
        message_text += f"   └─ **Uploaded:** {upload_time}\n"
    
    message_text += "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n👇 **Click a file below to manage** 👇"
    
    # Create file list buttons
    markup = types.InlineKeyboardMarkup(row_width=2)
    for fname, ftype, _, _ in files[:8]:
        is_running = is_bot_running(user_id, fname)
        status_icon = "🟢" if is_running else "🔴"
        file_icon = "🐍" if ftype == 'py' else "🟨"
        btn_text = f"{file_icon} {status_icon} {fname[:15]}"
        markup.add(types.InlineKeyboardButton(
            btn_text, 
            callback_data=f'file_{user_id}_{fname}'
        ))
    
    # Navigation buttons
    nav_row = []
    if len(files) > 8:
        nav_row.append(types.InlineKeyboardButton("▶️ NEXT", callback_data='files_next'))
    nav_row.append(types.InlineKeyboardButton("📤 UPLOAD", callback_data='upload'))
    nav_row.append(types.InlineKeyboardButton("🏠 MAIN", callback_data='back_to_main'))
    
    markup.row(*nav_row)
    bot.send_message(chat_id, message_text, parse_mode='Markdown', reply_markup=markup)

@bot.message_handler(commands=['manage'])
def command_manage(message):
    """Handle /manage <filename> command"""
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        bot.reply_to(
            message, 
            "❌ **Usage:** `/manage filename`\n\nExample: `/manage bot.py`", 
            parse_mode='Markdown'
        )
        return
    
    file_name = parts[1].strip()
    user_id = message.from_user.id
    
    # Check if file exists
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT file_type, file_size, upload_date FROM user_files WHERE user_id = ? AND file_name = ?', 
                 (user_id, file_name))
        row = c.fetchone()
    
    if not row:
        bot.reply_to(message, f"❌ **File not found:** `{file_name}`", parse_mode='Markdown')
        return
    
    file_type = row[0]
    file_size = row[1]
    upload_date = datetime.fromisoformat(row[2]).strftime("%Y-%m-%d %H:%M")
    is_running = is_bot_running(user_id, file_name)
    
    # Create management message
    manage_text = f"""
⚙️ **FILE MANAGEMENT**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 **File:** `{file_name}`
📁 **Type:** {file_type.upper()}
📦 **Size:** {format_size(file_size)}
📅 **Uploaded:** {upload_date}
🔰 **Status:** {'🟢 RUNNING' if is_running else '🔴 STOPPED'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    bot.send_message(
        message.chat.id,
        manage_text,
        parse_mode='Markdown',
        reply_markup=create_file_management_buttons(user_id, file_name, is_running)
    )

# ======================================================================
# 🔥 FILE UPLOAD HANDLER
# ======================================================================
@bot.message_handler(content_types=['document'])
def handle_file_upload(message):
    """Handle file uploads"""
    user_id = message.from_user.id
    chat_id = message.chat.id
    doc = message.document
    
    logger.info(f"📥 File upload from user {user_id}: {doc.file_name} ({doc.mime_type}, {doc.file_size} bytes)")
    
    # Check if bot is locked
    if bot_locked and user_id not in admin_ids:
        bot.reply_to(message, "🔒 **Bot is locked**\nFile uploads are disabled.", parse_mode='Markdown')
        return
    
    # Check file limit
    file_limit = get_user_file_limit(user_id)
    current_files = get_user_file_count(user_id)
    if current_files >= file_limit:
        limit_msg = (
            f"⚠️ **File Limit Reached!**\n\n"
            f"📊 Current: {current_files} / {file_limit} files\n\n"
            f"💡 **Solutions:**\n"
            f"• Delete old files with /checkfiles\n"
            f"• Upgrade to Premium for more slots\n"
            f"• Contact @{YOUR_USERNAME.replace('@', '')}"
        )
        bot.reply_to(message, limit_msg, parse_mode='Markdown')
        return
    
    # Check file name
    file_name = doc.file_name
    if not file_name:
        bot.reply_to(message, "❌ **Invalid file**\nFile has no name.", parse_mode='Markdown')
        return
    
    # Check file extension
    file_ext = os.path.splitext(file_name)[1].lower()
    allowed_exts = ['.py', '.js', '.zip', '.txt', '.json', '.html', '.css', '.md']
    if file_ext not in allowed_exts:
        exts_str = '`, `'.join(allowed_exts)
        bot.reply_to(
            message, 
            f"❌ **Unsupported file type**\n\nAllowed: `{exts_str}`", 
            parse_mode='Markdown'
        )
        return
    
    # Check file size
    max_size = 50 * 1024 * 1024  # 50MB
    if doc.file_size > max_size:
        bot.reply_to(
            message, 
            f"❌ **File too large**\nMax size: {max_size // 1024 // 1024}MB", 
            parse_mode='Markdown'
        )
        return
    
    # Download file
    status_msg = bot.reply_to(
        message, 
        f"📥 **Downloading...**\n"
        f"📄 File: `{file_name}`\n"
        f"📦 Size: {format_size(doc.file_size)}\n"
        f"⏳ Please wait...",
        parse_mode='Markdown'
    )
    
    try:
        file_info = bot.get_file(doc.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        bot.edit_message_text(
            f"✅ **Download Complete!**\n"
            f"📄 File: `{file_name}`\n"
            f"📦 Size: {format_size(doc.file_size)}\n"
            f"🔄 **Processing...**",
            chat_id, status_msg.message_id,
            parse_mode='Markdown'
        )
        
        user_folder = get_user_folder(user_id)
        
        # Handle ZIP files
        if file_ext == '.zip':
            process_zip_file(downloaded_file, file_name, user_id, user_folder, message, status_msg)
        else:
            # Save regular file
            file_path, file_size, saved_name = UltimateFileManager.save_file(user_id, downloaded_file, file_name)
            
            # Update user stats
            with db_manager.get_connection() as conn:
                c = conn.cursor()
                c.execute('''UPDATE active_users 
                            SET total_uploads = total_uploads + 1,
                                last_seen = ?
                            WHERE user_id = ?''',
                         (datetime.now().isoformat(), user_id))
                conn.commit()
            
            # Create success message
            success_msg = (
                f"✅ **File Uploaded Successfully!**\n\n"
                f"📄 **Name:** `{saved_name}`\n"
                f"📦 **Size:** {format_size(file_size)}\n"
                f"📁 **Type:** {file_ext[1:].upper()}\n"
                f"📊 **Storage:** {current_files + 1} / {file_limit} files\n\n"
            )
            
            # Auto-start scripts
            if file_ext in ['.py', '.js']:
                success_msg += f"🚀 **Auto-starting script...**"
                bot.edit_message_text(success_msg, chat_id, status_msg.message_id, parse_mode='Markdown')
                
                if file_ext == '.py':
                    threading.Thread(target=run_script, args=(file_path, user_id, user_folder, saved_name, message)).start()
                else:
                    threading.Thread(target=run_js_script, args=(file_path, user_id, user_folder, saved_name, message)).start()
                
                # Show management options
                time.sleep(2)
                is_running = is_bot_running(user_id, saved_name)
                bot.send_message(
                    chat_id,
                    f"📊 **Managing:** `{saved_name}`",
                    parse_mode='Markdown',
                    reply_markup=create_file_management_buttons(user_id, saved_name, is_running)
                )
            else:
                success_msg += f"📝 **File saved successfully**"
                bot.edit_message_text(success_msg, chat_id, status_msg.message_id, parse_mode='Markdown')
                
                # Show file options
                markup = types.InlineKeyboardMarkup()
                markup.row(
                    types.InlineKeyboardButton("📂 MY FILES", callback_data='check_files'),
                    types.InlineKeyboardButton("📤 UPLOAD MORE", callback_data='upload')
                )
                bot.send_message(
                    chat_id,
                    "What would you like to do next?",
                    reply_markup=markup
                )
    
    except Exception as e:
        logger.error(f"❌ Error processing file {file_name}: {e}", exc_info=True)
        try:
            bot.edit_message_text(
                f"❌ **Upload Failed**\n\nError: `{str(e)[:100]}`\n\nPlease try again.",
                chat_id, status_msg.message_id,
                parse_mode='Markdown'
            )
        except:
            pass

def process_zip_file(downloaded_content, zip_name, user_id, user_folder, original_message, status_msg):
    """Process uploaded ZIP file"""
    temp_dir = tempfile.mkdtemp(prefix=f"marco_{user_id}_")
    
    try:
        zip_path = os.path.join(temp_dir, zip_name)
        with open(zip_path, 'wb') as f:
            f.write(downloaded_content)
        
        # Extract ZIP
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            bad_file = zip_ref.testzip()
            if bad_file:
                raise zipfile.BadZipFile(f"Corrupted file: {bad_file}")
            zip_ref.extractall(temp_dir)
        
        # Analyze project structure
        project_info = analyze_project_structure(temp_dir)
        
        if not project_info['has_scripts']:
            bot.edit_message_text(
                f"❌ **No executable scripts found**\n\n"
                f"ZIP must contain `.py` or `.js` files.\n\n"
                f"📊 **ZIP Contents:**\n{project_info['file_list']}",
                original_message.chat.id, status_msg.message_id,
                parse_mode='Markdown'
            )
            return
        
        # Install Python dependencies
        if project_info['requirements']:
            bot.edit_message_text(
                f"📦 **Installing Python dependencies...**\n"
                f"Found: `requirements.txt`",
                original_message.chat.id, status_msg.message_id,
                parse_mode='Markdown'
            )
            
            def install_pip():
                try:
                    subprocess.run(
                        [sys.executable, '-m', 'pip', 'install', '-r', project_info['requirements']],
                        capture_output=True, text=True, timeout=120
                    )
                except Exception as e:
                    logger.error(f"PIP install error: {e}")
            
            Thread(target=install_pip, daemon=True).start()
        
        # Install Node.js dependencies
        if project_info['package_json']:
            bot.edit_message_text(
                f"📦 **Installing Node.js dependencies...**\n"
                f"Found: `package.json`",
                original_message.chat.id, status_msg.message_id,
                parse_mode='Markdown'
            )
            
            def install_npm():
                pkg_dir = os.path.dirname(project_info['package_json'])
                try:
                    # Check if npm exists
                    subprocess.run(['npm', '--version'], capture_output=True, check=True)
                    subprocess.run(
                        ['npm', 'install', '--cache', NPM_CACHE_DIR],
                        cwd=pkg_dir, capture_output=True, text=True, timeout=120
                    )
                except subprocess.CalledProcessError:
                    logger.error("npm not installed, skipping")
                except Exception as e:
                    logger.error(f"NPM install error: {e}")
            
            Thread(target=install_npm, daemon=True).start()
        
        # Copy files to user folder
        copied_files = []
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), temp_dir)
                dest_path = os.path.join(user_folder, rel_path)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                
                # Handle duplicates
                if os.path.exists(dest_path):
                    base, ext = os.path.splitext(rel_path)
                    counter = 1
                    while os.path.exists(os.path.join(user_folder, f"{base}_{counter}{ext}")):
                        counter += 1
                    dest_path = os.path.join(user_folder, f"{base}_{counter}{ext}")
                    rel_path = f"{base}_{counter}{ext}"
                
                shutil.copy2(os.path.join(root, file), dest_path)
                copied_files.append(rel_path)
        
        # Determine main script
        main_script = project_info['main_script'] or copied_files[0]
        main_script_path = os.path.join(user_folder, main_script)
        file_ext = os.path.splitext(main_script)[1].lower()
        
        # Save to database
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('''INSERT OR REPLACE INTO user_files 
                         (user_id, file_name, file_type, upload_date, file_size, status)
                         VALUES (?, ?, ?, ?, ?, ?)''',
                      (user_id, os.path.basename(main_script), file_ext[1:], 
                       datetime.now().isoformat(), os.path.getsize(main_script_path), 'idle'))
            conn.commit()
        
        # Update cache
        user_files.setdefault(user_id, []).append((os.path.basename(main_script), file_ext[1:]))
        
        # Success message
        success_msg = (
            f"✅ **ZIP Extracted Successfully!**\n\n"
            f"📦 **Archive:** `{zip_name}`\n"
            f"📄 **Main Script:** `{main_script}`\n"
            f"📁 **Files Extracted:** {len(copied_files)}\n"
            f"🐍 **Python Files:** {project_info['py_count']}\n"
            f"🟨 **JS Files:** {project_info['js_count']}\n\n"
            f"🚀 **Starting main script...**"
        )
        bot.edit_message_text(
            success_msg,
            original_message.chat.id, status_msg.message_id,
            parse_mode='Markdown'
        )
        
        # Start main script
        if file_ext == '.py':
            threading.Thread(target=run_script, args=(
                main_script_path, user_id, user_folder, os.path.basename(main_script), original_message
            )).start()
        else:
            threading.Thread(target=run_js_script, args=(
                main_script_path, user_id, user_folder, os.path.basename(main_script), original_message
            )).start()
        
        # Show management options after a delay
        time.sleep(3)
        is_running = is_bot_running(user_id, os.path.basename(main_script))
        bot.send_message(
            original_message.chat.id,
            f"📊 **Managing:** `{os.path.basename(main_script)}`",
            parse_mode='Markdown',
            reply_markup=create_file_management_buttons(user_id, os.path.basename(main_script), is_running)
        )
        
    except zipfile.BadZipFile:
        bot.edit_message_text(
            "❌ **Invalid ZIP file**\n\nThe file is corrupted or not a valid ZIP archive.",
            original_message.chat.id, status_msg.message_id,
            parse_mode='Markdown'
        )
    except Exception as e:
        logger.error(f"ZIP processing error: {e}", exc_info=True)
        bot.edit_message_text(
            f"❌ **ZIP Processing Failed**\n\nError: `{str(e)[:200]}`",
            original_message.chat.id, status_msg.message_id,
            parse_mode='Markdown'
        )
    finally:
        try:
            shutil.rmtree(temp_dir)
        except:
            pass

def analyze_project_structure(project_path):
    """Analyze project structure to find main script and dependencies"""
    result = {
        'has_scripts': False,
        'py_files': [],
        'js_files': [],
        'py_count': 0,
        'js_count': 0,
        'requirements': None,
        'package_json': None,
        'main_script': None,
        'file_list': '',
        'readme': None
    }
    
    main_py_names = ['main.py', 'bot.py', 'app.py', 'index.py', 'start.py', 'run.py', 'server.py']
    main_js_names = ['index.js', 'main.js', 'bot.js', 'app.js', 'server.js', 'start.js', 'api.js']
    
    file_list_lines = []
    
    for root, dirs, files in os.walk(project_path):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), project_path)
            
            if file.endswith('.py'):
                result['py_files'].append(rel_path)
                result['py_count'] += 1
                result['has_scripts'] = True
                file_list_lines.append(f"• `{rel_path}` 🐍")
                
                if file.lower() in main_py_names and not result['main_script']:
                    result['main_script'] = rel_path
                    
            elif file.endswith('.js'):
                result['js_files'].append(rel_path)
                result['js_count'] += 1
                result['has_scripts'] = True
                file_list_lines.append(f"• `{rel_path}` 🟨")
                
                if file.lower() in main_js_names and not result['main_script']:
                    result['main_script'] = rel_path
                    
            elif file == 'requirements.txt':
                result['requirements'] = os.path.join(root, file)
                file_list_lines.append(f"• `{rel_path}` 📦 (requirements)")
                
            elif file == 'package.json':
                result['package_json'] = os.path.join(root, file)
                file_list_lines.append(f"• `{rel_path}` 📦 (npm)")
                
            elif file.lower() in ['readme.md', 'readme.txt', 'readme']:
                result['readme'] = os.path.join(root, file)
                file_list_lines.append(f"• `{rel_path}` 📖")
            else:
                file_list_lines.append(f"• `{rel_path}`")
    
    # If no main script detected, use first script found
    if not result['main_script']:
        if result['py_files']:
            # Prefer files in root directory
            root_py = [f for f in result['py_files'] if '/' not in f and '\\' not in f]
            result['main_script'] = root_py[0] if root_py else result['py_files'][0]
        elif result['js_files']:
            root_js = [f for f in result['js_files'] if '/' not in f and '\\' not in f]
            result['main_script'] = root_js[0] if root_js else result['js_files'][0]
    
    # Limit file list display
    if len(file_list_lines) > 20:
        file_list_lines = file_list_lines[:20] + [f"... and {len(file_list_lines) - 20} more files"]
    
    result['file_list'] = '\n'.join(file_list_lines)
    return result

# ======================================================================
# 🔥 CALLBACK HANDLERS
# ======================================================================

def handle_file_control_callback(call):
    """Handle file control button clicks"""
    try:
        _, owner_id_str, file_name = call.data.split('_', 2)
        owner_id = int(owner_id_str)
        user_id = call.from_user.id
        
        # Check permissions
        if user_id != owner_id and user_id not in admin_ids:
            bot.answer_callback_query(
                call.id, 
                "⛔ You don't have permission to manage this file.", 
                show_alert=True
            )
            return
        
        # Get file info
        is_running = is_bot_running(owner_id, file_name)
        
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('''SELECT file_type, file_size, upload_date, run_count 
                        FROM user_files WHERE user_id = ? AND file_name = ?''', 
                     (owner_id, file_name))
            row = c.fetchone()
            
            if row:
                file_type = row[0]
                file_size = row[1]
                upload_date = datetime.fromisoformat(row[2]).strftime("%Y-%m-%d %H:%M")
                run_count = row[3]
            else:
                file_type = "unknown"
                file_size = 0
                upload_date = "unknown"
                run_count = 0
        
        # Create detailed info message
        status_text = "🟢 RUNNING" if is_running else "🔴 STOPPED"
        
        if is_running:
            script_key = f"{owner_id}_{file_name}"
            script_info = bot_scripts.get(script_key)
            if script_info:
                uptime = datetime.now() - script_info['start_time']
                uptime_str = str(uptime).split('.')[0]
                
                info_text = (
                    f"⚙️ **FILE MANAGEMENT**\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    f"📄 **File:** `{file_name}`\n"
                    f"📁 **Type:** {file_type.upper()}\n"
                    f"📦 **Size:** {format_size(file_size)}\n"
                    f"📅 **Uploaded:** {upload_date}\n"
                    f"🔄 **Run Count:** {run_count}\n"
                    f"🔰 **Status:** {status_text}\n"
                    f"🆔 **PID:** `{script_info['pid']}`\n"
                    f"⏱️ **Uptime:** `{uptime_str}`\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                )
            else:
                info_text = (
                    f"⚙️ **FILE MANAGEMENT**\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    f"📄 **File:** `{file_name}`\n"
                    f"📁 **Type:** {file_type.upper()}\n"
                    f"📦 **Size:** {format_size(file_size)}\n"
                    f"📅 **Uploaded:** {upload_date}\n"
                    f"🔄 **Run Count:** {run_count}\n"
                    f"🔰 **Status:** {status_text}\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                )
        else:
            info_text = (
                f"⚙️ **FILE MANAGEMENT**\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"📄 **File:** `{file_name}`\n"
                f"📁 **Type:** {file_type.upper()}\n"
                f"📦 **Size:** {format_size(file_size)}\n"
                f"📅 **Uploaded:** {upload_date}\n"
                f"🔄 **Run Count:** {run_count}\n"
                f"🔰 **Status:** {status_text}\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            )
        
        # Update message
        try:
            bot.edit_message_text(
                info_text,
                call.message.chat.id,
                call.message.message_id,
                parse_mode='Markdown',
                reply_markup=create_file_management_buttons(owner_id, file_name, is_running)
            )
        except Exception as e:
            # If can't edit, send new message
            bot.send_message(
                call.message.chat.id,
                info_text,
                parse_mode='Markdown',
                reply_markup=create_file_management_buttons(owner_id, file_name, is_running)
            )
        
        bot.answer_callback_query(call.id)
        
    except Exception as e:
        logger.error(f"Error in file_control_callback: {e}")
        bot.answer_callback_query(call.id, "Error loading file controls", show_alert=True)

def handle_start_script_callback(call):
    """Handle start script button"""
    try:
        _, owner_id_str, file_name = call.data.split('_', 2)
        owner_id = int(owner_id_str)
        user_id = call.from_user.id
        
        # Check permissions
        if user_id != owner_id and user_id not in admin_ids:
            bot.answer_callback_query(call.id, "⛔ Permission denied.", show_alert=True)
            return
        
        # Check if already running
        if is_bot_running(owner_id, file_name):
            bot.answer_callback_query(call.id, "⚠️ Script already running.", show_alert=True)
            return
        
        # Get file info
        user_folder = get_user_folder(owner_id)
        file_path = os.path.join(user_folder, file_name)
        
        if not os.path.exists(file_path):
            bot.answer_callback_query(call.id, "❌ File not found.", show_alert=True)
            return
        
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('SELECT file_type FROM user_files WHERE user_id = ? AND file_name = ?', 
                     (owner_id, file_name))
            row = c.fetchone()
            
            if not row:
                bot.answer_callback_query(call.id, "❌ File not found in database.", show_alert=True)
                return
            
            file_type = row[0]
        
        # Start script
        bot.answer_callback_query(call.id, "✅ Starting script...")
        
        if file_type == 'py':
            threading.Thread(target=run_script, args=(
                file_path, owner_id, user_folder, file_name, call.message
            )).start()
        elif file_type == 'js':
            threading.Thread(target=run_js_script, args=(
                file_path, owner_id, user_folder, file_name, call.message
            )).start()
        else:
            bot.answer_callback_query(call.id, "❌ Unknown file type.", show_alert=True)
            return
        
        # Wait a bit and update message
        time.sleep(2)
        is_running = is_bot_running(owner_id, file_name)
        
        # Update the management message
        try:
            bot.edit_message_reply_markup(
                call.message.chat.id,
                call.message.message_id,
                reply_markup=create_file_management_buttons(owner_id, file_name, is_running)
            )
        except:
            pass
        
    except Exception as e:
        logger.error(f"Error in start_script_callback: {e}")
        bot.answer_callback_query(call.id, "Error starting script", show_alert=True)

def handle_stop_script_callback(call):
    """Handle stop script button"""
    try:
        _, owner_id_str, file_name = call.data.split('_', 2)
        owner_id = int(owner_id_str)
        user_id = call.from_user.id
        
        # Check permissions
        if user_id != owner_id and user_id not in admin_ids:
            bot.answer_callback_query(call.id, "⛔ Permission denied.", show_alert=True)
            return
        
        script_key = f"{owner_id}_{file_name}"
        
        if script_key not in bot_scripts:
            bot.answer_callback_query(call.id, "⚠️ Script not running.", show_alert=True)
            return
        
        # Kill process
        process_info = bot_scripts.get(script_key)
        kill_process_tree(process_info)
        
        if script_key in bot_scripts:
            del bot_scripts[script_key]
        
        # Update database
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('''UPDATE user_files 
                        SET status = 'idle', pid = NULL
                        WHERE user_id = ? AND file_name = ?''',
                     (owner_id, file_name))
            
            c.execute('''UPDATE script_runs SET end_time = ?, status = ? 
                        WHERE user_id = ? AND file_name = ? AND status = 'running' ''',
                     (datetime.now().isoformat(), 'stopped', owner_id, file_name))
            conn.commit()
        
        bot.answer_callback_query(call.id, "🛑 Script stopped.")
        
        # Update message
        try:
            bot.edit_message_reply_markup(
                call.message.chat.id,
                call.message.message_id,
                reply_markup=create_file_management_buttons(owner_id, file_name, False)
            )
        except:
            pass
        
    except Exception as e:
        logger.error(f"Error in stop_script_callback: {e}")
        bot.answer_callback_query(call.id, "Error stopping script", show_alert=True)

def handle_restart_script_callback(call):
    """Handle restart script button"""
    try:
        _, owner_id_str, file_name = call.data.split('_', 2)
        owner_id = int(owner_id_str)
        user_id = call.from_user.id
        
        # Check permissions
        if user_id != owner_id and user_id not in admin_ids:
            bot.answer_callback_query(call.id, "⛔ Permission denied.", show_alert=True)
            return
        
        # Stop if running
        script_key = f"{owner_id}_{file_name}"
        if script_key in bot_scripts:
            kill_process_tree(bot_scripts[script_key])
            if script_key in bot_scripts:
                del bot_scripts[script_key]
            time.sleep(1)
        
        # Start again
        user_folder = get_user_folder(owner_id)
        file_path = os.path.join(user_folder, file_name)
        
        if not os.path.exists(file_path):
            bot.answer_callback_query(call.id, "❌ File not found.", show_alert=True)
            return
        
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('SELECT file_type FROM user_files WHERE user_id = ? AND file_name = ?', 
                     (owner_id, file_name))
            row = c.fetchone()
            
            if not row:
                bot.answer_callback_query(call.id, "❌ File not found.", show_alert=True)
                return
            
            file_type = row[0]
        
        bot.answer_callback_query(call.id, "🔄 Restarting script...")
        
        if file_type == 'py':
            threading.Thread(target=run_script, args=(
                file_path, owner_id, user_folder, file_name, call.message
            )).start()
        elif file_type == 'js':
            threading.Thread(target=run_js_script, args=(
                file_path, owner_id, user_folder, file_name, call.message
            )).start()
        
        # Wait and update
        time.sleep(2)
        is_running = is_bot_running(owner_id, file_name)
        
        try:
            bot.edit_message_reply_markup(
                call.message.chat.id,
                call.message.message_id,
                reply_markup=create_file_management_buttons(owner_id, file_name, is_running)
            )
        except:
            pass
        
    except Exception as e:
        logger.error(f"Error in restart_script_callback: {e}")
        bot.answer_callback_query(call.id, "Error restarting script", show_alert=True)

def handle_delete_script_callback(call):
    """Handle delete script button"""
    try:
        _, owner_id_str, file_name = call.data.split('_', 2)
        owner_id = int(owner_id_str)
        user_id = call.from_user.id
        
        # Check permissions
        if user_id != owner_id and user_id not in admin_ids:
            bot.answer_callback_query(call.id, "⛔ Permission denied.", show_alert=True)
            return
        
        # Confirm deletion
        markup = types.InlineKeyboardMarkup()
        markup.row(
            types.InlineKeyboardButton("✅ YES, DELETE", callback_data=f'confirm_delete_{owner_id}_{file_name}'),
            types.InlineKeyboardButton("❌ NO, CANCEL", callback_data=f'file_{owner_id}_{file_name}')
        )
        
        bot.edit_message_text(
            f"⚠️ **Are you sure you want to delete** `{file_name}`?\n\nThis action cannot be undone!",
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=markup
        )
        
        bot.answer_callback_query(call.id)
        
    except Exception as e:
        logger.error(f"Error in delete_script_callback: {e}")
        bot.answer_callback_query(call.id, "Error", show_alert=True)

def handle_confirm_delete_callback(call):
    """Handle confirm deletion"""
    try:
        _, _, owner_id_str, file_name = call.data.split('_', 3)
        owner_id = int(owner_id_str)
        user_id = call.from_user.id
        
        # Check permissions
        if user_id != owner_id and user_id not in admin_ids:
            bot.answer_callback_query(call.id, "⛔ Permission denied.", show_alert=True)
            return
        
        # Stop if running
        script_key = f"{owner_id}_{file_name}"
        if script_key in bot_scripts:
            kill_process_tree(bot_scripts[script_key])
            if script_key in bot_scripts:
                del bot_scripts[script_key]
        
        # Delete file
        UltimateFileManager.delete_file(owner_id, file_name)
        
        bot.answer_callback_query(call.id, "🗑️ File deleted.")
        
        # Go back to files list
        handle_check_files_callback(call)
        
    except Exception as e:
        logger.error(f"Error in confirm_delete_callback: {e}")
        bot.answer_callback_query(call.id, "Error deleting file", show_alert=True)

def handle_logs_callback(call):
    """Handle view logs button"""
    try:
        _, owner_id_str, file_name = call.data.split('_', 2)
        owner_id = int(owner_id_str)
        user_id = call.from_user.id
        
        # Check permissions
        if user_id != owner_id and user_id not in admin_ids:
            bot.answer_callback_query(call.id, "⛔ Permission denied.", show_alert=True)
            return
        
        user_folder = get_user_folder(owner_id)
        
        # Find all log files for this script
        log_files = [f for f in os.listdir(user_folder) 
                    if f.startswith(os.path.splitext(file_name)[0]) and f.endswith('.log')]
        
        if not log_files:
            bot.answer_callback_query(call.id, "📜 No logs found.", show_alert=True)
            return
        
        # Get the most recent log
        latest_log = max(log_files, key=lambda f: os.path.getmtime(os.path.join(user_folder, f)))
        log_path = os.path.join(user_folder, latest_log)
        
        bot.answer_callback_query(call.id, "📜 Fetching logs...")
        
        # Read log file
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            log_content = f.read()
        
        # Truncate if too long
        if len(log_content) > 3500:
            log_content = log_content[-3500:]
            log_content = "... (truncated) ...\n" + log_content
        
        # Create log viewer markup
        markup = types.InlineKeyboardMarkup()
        markup.row(
            types.InlineKeyboardButton("🔄 REFRESH", callback_data=f'logs_{owner_id}_{file_name}'),
            types.InlineKeyboardButton("🔙 BACK", callback_data=f'file_{owner_id}_{file_name}')
        )
        
        # Send logs
        bot.send_message(
            call.message.chat.id,
            f"📜 **Logs for `{file_name}`**\n```\n{log_content}\n```",
            parse_mode='Markdown',
            reply_markup=markup
        )
        
    except Exception as e:
        logger.error(f"Error in logs_callback: {e}")
        bot.answer_callback_query(call.id, "Error reading logs", show_alert=True)

def handle_cpu_usage_callback(call):
    """Handle CPU usage button"""
    try:
        _, owner_id_str, file_name = call.data.split('_', 2)
        owner_id = int(owner_id_str)
        
        script_key = f"{owner_id}_{file_name}"
        
        if script_key not in bot_scripts:
            bot.answer_callback_query(call.id, "❌ Script not running.", show_alert=True)
            return
        
        proc_info = bot_scripts[script_key]
        
        try:
            proc = psutil.Process(proc_info['process'].pid)
            
            # Get CPU and memory info
            cpu_percent = proc.cpu_percent(interval=0.5)
            memory_info = proc.memory_info()
            memory_percent = proc.memory_percent()
            
            # Get IO counters
            try:
                io_counters = proc.io_counters()
                io_text = f"📤 Read: {format_size(io_counters.read_bytes)}\n📥 Write: {format_size(io_counters.write_bytes)}"
            except:
                io_text = "IO stats not available"
            
            # Get thread count
            threads = proc.num_threads()
            
            # Get connections
            try:
                connections = len(proc.connections())
            except:
                connections = "N/A"
            
            info_text = (
                f"📊 **Resource Monitor**\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"📄 **File:** `{file_name}`\n"
                f"🆔 **PID:** `{proc_info['pid']}`\n\n"
                f"💻 **CPU:** `{cpu_percent:.1f}%`\n"
                f"💾 **RAM:** `{format_size(memory_info.rss)}` ({memory_percent:.1f}%)\n"
                f"🧵 **Threads:** `{threads}`\n"
                f"🔌 **Connections:** `{connections}`\n\n"
                f"{io_text}\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            )
            
            # Create refresh button
            markup = types.InlineKeyboardMarkup()
            markup.row(
                types.InlineKeyboardButton("🔄 REFRESH", callback_data=f'cpu_{owner_id}_{file_name}'),
                types.InlineKeyboardButton("🔙 BACK", callback_data=f'file_{owner_id}_{file_name}')
            )
            
            # Try to edit, if not possible send new
            try:
                bot.edit_message_text(
                    info_text,
                    call.message.chat.id,
                    call.message.message_id,
                    parse_mode='Markdown',
                    reply_markup=markup
                )
                bot.answer_callback_query(call.id)
            except:
                bot.send_message(
                    call.message.chat.id,
                    info_text,
                    parse_mode='Markdown',
                    reply_markup=markup
                )
                bot.answer_callback_query(call.id)
                
        except psutil.NoSuchProcess:
            bot.answer_callback_query(call.id, "❌ Process no longer exists.", show_alert=True)
            
    except Exception as e:
        logger.error(f"Error in cpu_usage_callback: {e}")
        bot.answer_callback_query(call.id, "❌ Could not fetch resource usage.", show_alert=True)

def handle_memory_callback(call):
    """Handle memory usage button (similar to CPU)"""
    # Reuse CPU handler for now
    handle_cpu_usage_callback(call)

def handle_uptime_callback(call):
    """Handle uptime button"""
    try:
        _, owner_id_str, file_name = call.data.split('_', 2)
        owner_id = int(owner_id_str)
        
        script_key = f"{owner_id}_{file_name}"
        
        if script_key not in bot_scripts:
            bot.answer_callback_query(call.id, "❌ Script not running.", show_alert=True)
            return
        
        uptime = datetime.now() - bot_scripts[script_key]['start_time']
        uptime_str = str(uptime).split('.')[0]
        
        bot.answer_callback_query(
            call.id, 
            f"⏱️ Uptime: {uptime_str}", 
            show_alert=True
        )
        
    except Exception as e:
        logger.error(f"Error in uptime_callback: {e}")
        bot.answer_callback_query(call.id, "❌ Could not fetch uptime.", show_alert=True)

def handle_details_callback(call):
    """Handle details button - show comprehensive script info"""
    try:
        _, owner_id_str, file_name = call.data.split('_', 2)
        owner_id = int(owner_id_str)
        
        script_key = f"{owner_id}_{file_name}"
        
        if script_key not in bot_scripts:
            bot.answer_callback_query(call.id, "❌ Script not running.", show_alert=True)
            return
        
        proc_info = bot_scripts[script_key]
        
        try:
            proc = psutil.Process(proc_info['process'].pid)
            
            # Get process info
            create_time = datetime.fromtimestamp(proc.create_time())
            uptime = datetime.now() - create_time
            uptime_str = str(uptime).split('.')[0]
            
            cpu_percent = proc.cpu_percent(interval=0.2)
            memory_info = proc.memory_info()
            memory_percent = proc.memory_percent()
            
            # Get status
            status = proc.status()
            
            # Get user
            try:
                username = proc.username()
            except:
                username = "N/A"
            
            info_text = (
                f"📊 **Detailed Process Info**\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"📄 **File:** `{file_name}`\n"
                f"🆔 **PID:** `{proc_info['pid']}`\n"
                f"👤 **User:** `{username}`\n"
                f"🔰 **Status:** `{status}`\n"
                f"⏱️ **Uptime:** `{uptime_str}`\n"
                f"💻 **CPU:** `{cpu_percent:.1f}%`\n"
                f"💾 **RAM:** `{format_size(memory_info.rss)}` ({memory_percent:.1f}%)\n"
                f"📅 **Started:** {create_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            )
            
            # Create buttons
            markup = types.InlineKeyboardMarkup()
            markup.row(
                types.InlineKeyboardButton("🔄 REFRESH", callback_data=f'details_{owner_id}_{file_name}'),
                types.InlineKeyboardButton("🔙 BACK", callback_data=f'file_{owner_id}_{file_name}')
            )
            
            bot.edit_message_text(
                info_text,
                call.message.chat.id,
                call.message.message_id,
                parse_mode='Markdown',
                reply_markup=markup
            )
            bot.answer_callback_query(call.id)
            
        except psutil.NoSuchProcess:
            bot.answer_callback_query(call.id, "❌ Process no longer exists.", show_alert=True)
            
    except Exception as e:
        logger.error(f"Error in details_callback: {e}")
        bot.answer_callback_query(call.id, "❌ Error", show_alert=True)

def handle_refresh_callback(call):
    """Handle refresh button - refresh file management view"""
    try:
        _, owner_id_str, file_name = call.data.split('_', 2)
        owner_id = int(owner_id_str)
        
        # Just reload the file control view
        handle_file_control_callback(call)
        
    except Exception as e:
        logger.error(f"Error in refresh_callback: {e}")
        bot.answer_callback_query(call.id, "❌ Error", show_alert=True)

def handle_install_npm_callback(call):
    """Handle npm install button"""
    try:
        _, owner_id_str, file_name = call.data.split('_', 2)
        owner_id = int(owner_id_str)
        
        bot.answer_callback_query(call.id, "📦 Send the npm package name to install.")
        
        msg = bot.send_message(
            call.message.chat.id, 
            "📦 **Enter npm package name:**\n\nExample: `express` or `discord.js`",
            parse_mode='Markdown'
        )
        
        bot.register_next_step_handler(msg, lambda m: process_npm_install(m, owner_id, file_name))
        
    except Exception as e:
        logger.error(f"Error in install_npm_callback: {e}")
        bot.answer_callback_query(call.id, "Error", show_alert=True)

def process_npm_install(message, owner_id, file_name):
    """Process npm installation"""
    if not message.text:
        bot.reply_to(message, "❌ No package name provided.")
        return
    package = message.text.strip()
    
    if not package:
        bot.reply_to(message, "❌ No package name provided.")
        return
    
    user_folder = get_user_folder(owner_id)
    package_installer.install_package(package, owner_id, message, 'node')

def handle_install_pip_callback(call):
    """Handle pip install button"""
    try:
        _, owner_id_str, file_name = call.data.split('_', 2)
        owner_id = int(owner_id_str)
        
        bot.answer_callback_query(call.id, "🐍 Send the pip package name to install.")
        
        msg = bot.send_message(
            call.message.chat.id, 
            "🐍 **Enter Python package name:**\n\nExample: `requests` or `flask`",
            parse_mode='Markdown'
        )
        
        bot.register_next_step_handler(msg, lambda m: process_pip_install(m, owner_id, file_name))
        
    except Exception as e:
        logger.error(f"Error in install_pip_callback: {e}")
        bot.answer_callback_query(call.id, "Error", show_alert=True)

def process_pip_install(message, owner_id, file_name):
    """Process pip installation"""
    if not message.text:
        bot.reply_to(message, "❌ No package name provided.")
        return
    package = message.text.strip()
    
    if not package:
        bot.reply_to(message, "❌ No package name provided.")
        return
    
    package_installer.install_package(package, owner_id, message, 'python')

def handle_check_files_callback(call):
    """Handle check files button"""
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    
    # Get files from database
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('''SELECT file_name, file_type, file_size, upload_date 
                    FROM user_files WHERE user_id = ? ORDER BY upload_date DESC''', (user_id,))
        files = c.fetchall()
    
    if not files:
        # No files
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📤 UPLOAD NOW", callback_data='upload'))
        markup.add(types.InlineKeyboardButton("🏠 MAIN MENU", callback_data='back_to_main'))
        
        try:
            bot.edit_message_text(
                "📂 **YOUR FILES**\n\n✨ **No files uploaded yet**\n\n📤 Upload your first file now!",
                chat_id,
                call.message.message_id,
                parse_mode='Markdown',
                reply_markup=markup
            )
        except:
            bot.send_message(
                chat_id,
                "📂 **YOUR FILES**\n\n✨ **No files uploaded yet**\n\n📤 Upload your first file now!",
                parse_mode='Markdown',
                reply_markup=markup
            )
        
        bot.answer_callback_query(call.id)
        return
    
    file_count = len(files)
    limit = get_user_file_limit(user_id)
    limit_display = "∞" if limit == float('inf') else str(limit)
    
    # Build message
    message_text = f"📂 **YOUR FILES** ({file_count}/{limit_display})\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    
    for i, (fname, ftype, fsize, udate) in enumerate(files[:5], 1):  # Show first 5 in preview
        is_running = is_bot_running(user_id, fname)
        status = "🟢 RUNNING" if is_running else "🔴 STOPPED"
        icon = "🐍" if ftype == 'py' else "🟨" if ftype == 'js' else "📦"
        
        # Handle None file_size
        if fsize is None:
            fsize = 0
            
        message_text += f"\n{icon} `{fname}`\n   ├─ **Status:** {status}\n   └─ **Size:** {format_size(fsize)}\n"
    
    if len(files) > 5:
        message_text += f"\n... and {len(files) - 5} more files"
    
    message_text += "\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n👇 **Click a file to manage** 👇"
    
    # Create buttons
    markup = types.InlineKeyboardMarkup(row_width=2)
    for fname, ftype, _, _ in files[:8]:
        is_running = is_bot_running(user_id, fname)
        status_icon = "🟢" if is_running else "🔴"
        file_icon = "🐍" if ftype == 'py' else "🟨"
        btn_text = f"{file_icon} {status_icon} {fname[:15]}"
        markup.add(types.InlineKeyboardButton(
            btn_text, 
            callback_data=f'file_{user_id}_{fname}'
        ))
    
    # Navigation
    nav_row = []
    if len(files) > 8:
        nav_row.append(types.InlineKeyboardButton("▶️ NEXT", callback_data='files_next'))
    nav_row.append(types.InlineKeyboardButton("📤 UPLOAD", callback_data='upload'))
    nav_row.append(types.InlineKeyboardButton("🏠 MAIN", callback_data='back_to_main'))
    
    markup.row(*nav_row)
    
    bot.answer_callback_query(call.id)
    
    try:
        bot.edit_message_text(
            message_text,
            chat_id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=markup
        )
    except:
        bot.send_message(
            chat_id,
            message_text,
            parse_mode='Markdown',
            reply_markup=markup
        )

def handle_speed_test_callback(call):
    """Handle speed test button"""
    # Reuse the command handler
    message = call.message
    message.text = "speed"  # Fake text
    command_speed(message)
    bot.answer_callback_query(call.id)

def handle_statistics_callback(call):
    """Handle statistics button"""
    # Reuse the command handler
    message = call.message
    message.text = "stats"  # Fake text
    command_stats(message)
    bot.answer_callback_query(call.id)

def handle_back_to_main_callback(call):
    """Handle back to main menu button"""
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    
    # Get user stats
    file_limit = get_user_file_limit(user_id)
    current_files = get_user_file_count(user_id)
    limit_display = "∞" if file_limit == float('inf') else str(file_limit)
    
    # Determine status
    if user_id == OWNER_ID:
        user_status = "👑 OWNER"
    elif user_id in admin_ids:
        user_status = "🛡️ ADMIN"
    elif user_id in user_subscriptions:
        expiry = user_subscriptions[user_id].get('expiry')
        if expiry and expiry > datetime.now():
            days_left = (expiry - datetime.now()).days
            user_status = f"⭐ PREMIUM ({days_left}d)"
        else:
            user_status = "🆓 FREE"
    else:
        user_status = "🆓 FREE"
    
    welcome_text = f"""
{user_status} **MARCO HOST** {user_status}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 **User:** {call.from_user.first_name or 'User'}
🆔 **ID:** `{user_id}`
📁 **Files:** {current_files}/{limit_display}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👇 **Choose an option:** 👇
"""
    
    bot.answer_callback_query(call.id)
    
    try:
        bot.edit_message_text(
            welcome_text,
            chat_id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=create_main_menu_inline(user_id)
        )
    except:
        bot.send_message(
            chat_id,
            welcome_text,
            parse_mode='Markdown',
            reply_markup=create_main_menu_inline(user_id)
        )

def handle_premium_info_callback(call):
    """Handle premium info button"""
    user_id = call.from_user.id
    
    premium_text = f"""
💎 **PREMIUM SUBSCRIPTION**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ **PREMIUM BENEFITS**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 **MORE STORAGE**
• Free: `5` files
• Premium: `15` files
• Admin: `999` files
• Owner: `∞` Unlimited

🚀 **PRIORITY HOSTING**
• Faster script execution
• Higher CPU/RAM limits
• Priority support 24/7
• No queue system

📊 **ADVANCED FEATURES**
• Long-running scripts (24/7)
• Multiple file uploads
• Advanced analytics
• Resource monitoring

🛠️ **ADDITIONAL**
• Custom domains support
• API access
• Backup & restore
• Priority updates

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 **Price:** Contact @{YOUR_USERNAME.replace('@', '')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    if user_id in admin_ids:
        premium_text += "\n👑 **Admins have unlimited access!**"
    
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("💳 PURCHASE", url=f'https://t.me/{YOUR_USERNAME.replace("@", "")}'),
        types.InlineKeyboardButton("🔙 BACK", callback_data='back_to_main')
    )
    
    bot.answer_callback_query(call.id)
    
    try:
        bot.edit_message_text(
            premium_text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=markup
        )
    except:
        bot.send_message(
            call.message.chat.id,
            premium_text,
            parse_mode='Markdown',
            reply_markup=markup
        )

def handle_about_callback(call):
    """Handle about button"""
    about_text = f"""
ℹ️ **MARCO HOST - ULTIMATE EDITION**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 **Version:** `4.0.0` (Ultimate Premium)
📅 **Release:** January 2025
👑 **Owner:** @Zinko158
⚡ **Powered by:** Python 3.11+ & Node.js 20+

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 **ULTIMATE FEATURES**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ **Python 3.11+ Hosting**
  • Auto pip install
  • Virtual environment
  • Real-time logs

✅ **Node.js 20+ Hosting**
  • Auto npm install
  • Package.json support
  • Full npm ecosystem

✅ **ZIP Upload**
  • Auto project detection
  • requirements.txt support
  • package.json support
  • Multi-file extraction

✅ **Process Management**
  • Start/Stop/Restart
  • CPU/RAM monitoring
  • Uptime tracking
  • Auto restart on crash

✅ **Premium Features**
  • 24/7 uptime
  • Priority support
  • Higher limits
  • Advanced analytics

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📢 **Updates:** {UPDATE_CHANNEL}
📞 **Support:** @{YOUR_USERNAME.replace('@', '')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("📢 JOIN CHANNEL", url=UPDATE_CHANNEL),
        types.InlineKeyboardButton("🔙 BACK", callback_data='back_to_main')
    )
    
    bot.answer_callback_query(call.id)
    
    try:
        bot.edit_message_text(
            about_text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=markup
        )
    except:
        bot.send_message(
            call.message.chat.id,
            about_text,
            parse_mode='Markdown',
            reply_markup=markup
        )

def handle_tools_callback(call):
    """Handle tools button"""
    tools_text = """
🛠️ **TOOLS & UTILITIES**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔧 **Available Tools:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 **Package Installer**
• Install npm packages
• Install pip packages
• Auto dependency resolution

📊 **Resource Monitor**
• CPU usage per script
• RAM usage per script
• Uptime tracking

📜 **Log Viewer**
• Real-time logs
• Historical logs
• Log rotation

🔍 **File Manager**
• List all files
• Delete files
• File info

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 **More tools coming soon!**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("📦 NPM INSTALL", callback_data='tools_npm'),
        types.InlineKeyboardButton("🐍 PIP INSTALL", callback_data='tools_pip')
    )
    markup.row(
        types.InlineKeyboardButton("📊 MONITOR", callback_data='check_files'),
        types.InlineKeyboardButton("📜 LOGS", callback_data='check_files')
    )
    markup.row(
        types.InlineKeyboardButton("🔙 BACK", callback_data='back_to_main')
    )
    
    bot.answer_callback_query(call.id)
    
    try:
        bot.edit_message_text(
            tools_text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=markup
        )
    except:
        bot.send_message(
            call.message.chat.id,
            tools_text,
            parse_mode='Markdown',
            reply_markup=markup
        )

def handle_help_callback(call):
    """Handle help button"""
    help_text = """
🆘 **HELP & SUPPORT**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📤 **UPLOADING FILES**
• Send `.py`, `.js`, or `.zip` files
• Max file size: 50MB
• Bot auto-detects main script
• Auto-installs dependencies

📂 **MANAGING FILES**
• Click "📂 MY FILES" button
• Click on any file to manage
• Start/Stop/Restart/Delete
• View logs & monitor resources

🤖 **RUNNING SCRIPTS**
• Files auto-run after upload
• Monitor with CPU/RAM buttons
• View real-time logs
• Auto-restart on crash

📊 **COMMANDS**
• `/start` - Main menu
• `/help` - This help
• `/stats` - Bot statistics
• `/speed` - Speed test
• `/checkfiles` - Your files
• `/manage <file>` - Manage file

💎 **PREMIUM**
• 15 files instead of 5
• Priority support
• More resources
• Contact @Zinko158

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("📢 UPDATES", url=UPDATE_CHANNEL),
        types.InlineKeyboardButton("📞 SUPPORT", url=f'https://t.me/{YOUR_USERNAME.replace("@", "")}')
    )
    markup.row(
        types.InlineKeyboardButton("🔙 BACK", callback_data='back_to_main')
    )
    
    bot.answer_callback_query(call.id)
    
    try:
        bot.edit_message_text(
            help_text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=markup
        )
    except:
        bot.send_message(
            call.message.chat.id,
            help_text,
            parse_mode='Markdown',
            reply_markup=markup
        )

# ======================================================================
# 🔥 ADMIN CALLBACK HANDLERS
# ======================================================================

def admin_panel_callback(call):
    """Handle admin panel button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    
    admin_text = """
👑 **ADMIN CONTROL PANEL**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔰 **Administration Tools:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👥 **User Management**
• Add/Remove Admins
• List all admins
• Manage permissions

💳 **Subscription Management**
• Add Premium users
• Remove Premium
• Check subscription status
• View subscription stats

🛠️ **System Management**
• Lock/Unlock bot
• Broadcast messages
• View system stats
• Clean old logs
• Restart bot

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👇 **Select an option** 👇
"""
    
    try:
        bot.edit_message_text(
            admin_text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=create_admin_panel()
        )
    except:
        bot.send_message(
            call.message.chat.id,
            admin_text,
            parse_mode='Markdown',
            reply_markup=create_admin_panel()
        )

def handle_system_stats_callback(call):
    """Handle system stats button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    stats = get_system_stats()
    processes = len(bot_scripts)
    
    # Calculate bot memory usage
    bot_memory = 0
    for key, info in bot_scripts.items():
        try:
            proc = psutil.Process(info['process'].pid)
            bot_memory += proc.memory_info().rss
        except:
            pass
    
    # Database size
    db_size = os.path.getsize(DATABASE_PATH) if os.path.exists(DATABASE_PATH) else 0
    
    # Logs size
    log_size = 0
    if os.path.exists(LOGS_DIR):
        for f in os.listdir(LOGS_DIR):
            f_path = os.path.join(LOGS_DIR, f)
            if os.path.isfile(f_path):
                log_size += os.path.getsize(f_path)
    
    # User counts
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM active_users')
        db_users = c.fetchone()[0]
        c.execute('SELECT COUNT(*) FROM subscriptions')
        premium_users = c.fetchone()[0]
        c.execute('SELECT COUNT(*) FROM script_runs WHERE DATE(start_time) = DATE("now")')
        today_runs = c.fetchone()[0]
    
    # Boot time error ဖြေရှင်းထားသော အပိုင်း
    try:
        sys_boot_time = psutil.boot_time()
    except Exception:
        sys_boot_time = time.time()
        
    stats_text = f"""
📊 **SYSTEM STATISTICS**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💻 **HARDWARE**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🖥️ **CPU:** `{stats.get('cpu', 0)}%` ({stats.get('cpu_count', 0)} cores)
💾 **RAM:** `{format_size(stats.get('memory_used', 0))}` / `{format_size(stats.get('memory_total', 0))}` (`{stats.get('memory_percent', 0)}%`)
💿 **DISK:** `{format_size(stats.get('disk_used', 0))}` / `{format_size(stats.get('disk_total', 0))}` (`{stats.get('disk_percent', 0)}%`)
🌐 **Network:** ↑`{format_size(stats.get('net_sent', 0))}` ↓`{format_size(stats.get('net_recv', 0))}`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 **BOT PROCESSES**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🟢 **Active Scripts:** `{processes}`
📊 **Bot Memory:** `{format_size(bot_memory)}`
📁 **DB Size:** `{format_size(db_size)}`
📝 **Logs Size:** `{format_size(log_size)}`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 **DATABASE STATS**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👥 **Active Users:** `{db_users:,}`
💎 **Premium Users:** `{premium_users:,}`
📈 **Today's Runs:** `{today_runs:,}`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏱️ **System Uptime:** `{format_time(time.time() - sys_boot_time)}`
🤖 **Bot Uptime:** `{format_time(time.time() - start_time)}`
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    bot.answer_callback_query(call.id)
    
    try:
        bot.edit_message_text(
            stats_text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=create_admin_panel()
        )
    except:
        bot.send_message(
            call.message.chat.id,
            stats_text,
            parse_mode='Markdown',
            reply_markup=create_admin_panel()
        )


def handle_broadcast_init_callback(call):
    """Handle broadcast button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    
    msg = bot.send_message(
        call.message.chat.id, 
        "📢 **Send the message to broadcast to all users:**\n\n"
        "You can use Markdown formatting.",
        parse_mode='Markdown'
    )
    
    bot.register_next_step_handler(msg, process_broadcast)

def process_broadcast(message):
    if message.from_user.id not in admin_ids:
        return
    
    text = message.text or message.caption or "Broadcast message"
    
    # 📌 Admin ရိုက်လိုက်တဲ့စာကို ယာယီသိမ်းပါမယ်
    global broadcast_temp_data
    broadcast_temp_data[message.from_user.id] = text
    
    # Ask for confirmation
    markup = types.InlineKeyboardMarkup()

    markup.row(
        types.InlineKeyboardButton("✅ YES, SEND", callback_data='confirm_broadcast'),
        types.InlineKeyboardButton("❌ CANCEL", callback_data='admin_panel')
    )
    
    preview = text[:100] + "..." if len(text) > 100 else text
    
    bot.reply_to(
        message,
        f"📢 **Broadcast Preview:**\n\n{preview}\n\n"
        f"**Total recipients:** {len(active_users)} users\n\n"
        f"Send this broadcast?",
        parse_mode='Markdown',
        reply_markup=markup
    )

def process_broadcast(message):
    """Process broadcast message"""
    if message.from_user.id not in admin_ids:
        return
    
    text = message.text or message.caption or "Broadcast message"
    
    # 📌 Admin ရိုက်လိုက်တဲ့စာကို ယာယီသိမ်းပါမယ်
    global broadcast_temp_data
    broadcast_temp_data[message.from_user.id] = text
    
    # Ask for confirmation
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("✅ YES, SEND", callback_data='confirm_broadcast'),
        types.InlineKeyboardButton("❌ CANCEL", callback_data='admin_panel')
    )
    
    preview = text[:100] + "..." if len(text) > 100 else text
    
    bot.reply_to(
        message,
        f"📢 **Broadcast Preview:**\n\n{preview}\n\n"
        f"**Total recipients:** {len(active_users)} users\n\n"
        f"Send this broadcast?",
        parse_mode='Markdown',
        reply_markup=markup
    )


def handle_confirm_broadcast_callback(call):
    """Confirm and send broadcast"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    bot.answer_callback_query(call.id, "📢 Sending broadcast...")
    
    # 📌 သိမ်းထားတဲ့စာကို ပြန်ယူပါမယ်
    global broadcast_temp_data
    text = broadcast_temp_data.get(call.from_user.id, "Empty Message")
    
    success = 0
    fail = 0
    
    for uid in active_users:
        try:
            bot.send_message(
                uid, 
                f"📢 **BROADCAST**\n\n{text}", 
                parse_mode='Markdown'
            )
            success += 1
        except Exception as e:
            fail += 1
            logger.error(f"Broadcast failed to {uid}: {e}")
        
        time.sleep(0.3)  # Rate limiting
    
    # Send result
    bot.send_message(
        call.message.chat.id,
        f"📊 **Broadcast Complete**\n\n"
        f"✅ **Success:** {success} users\n"
        f"❌ **Failed:** {fail} users",
        parse_mode='Markdown'
    )


def handle_lock_bot_callback(call):
    """Handle lock bot button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    global bot_locked
    bot_locked = True
    
    # Update database (removed updated_at)
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('UPDATE settings SET value = ? WHERE key = ?', 
                  ('true', 'bot_locked'))
        conn.commit()
    
    bot.answer_callback_query(call.id, "🔒 Bot locked.")
    
    # Update message
    try:
        bot.edit_message_reply_markup(
            call.message.chat.id,
            call.message.message_id,
            reply_markup=create_admin_panel()
        )
    except:
        pass

def handle_unlock_bot_callback(call):
    """Handle unlock bot button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    global bot_locked
    bot_locked = False
    
    # Update database (removed updated_at)
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('UPDATE settings SET value = ? WHERE key = ?', 
                  ('false', 'bot_locked'))
        conn.commit()
    
    bot.answer_callback_query(call.id, "🔓 Bot unlocked.")
    
    # Update message
    try:
        bot.edit_message_reply_markup(
            call.message.chat.id,
            call.message.message_id,
            reply_markup=create_admin_panel()
        )
    except:
        pass

def handle_run_all_scripts_callback(call):
    """Handle run all scripts button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    bot.answer_callback_query(call.id, "🔄 Running all scripts...")
    
    count = 0
    for uid, files in user_files.items():
        for fname, ftype in files:
            if not is_bot_running(uid, fname):
                user_folder = get_user_folder(uid)
                file_path = os.path.join(user_folder, fname)
                
                if os.path.exists(file_path):
                    if ftype == 'py':
                        threading.Thread(target=run_script, args=(
                            file_path, uid, user_folder, fname, call.message
                        )).start()
                    else:
                        threading.Thread(target=run_js_script, args=(
                            file_path, uid, user_folder, fname, call.message
                        )).start()
                    count += 1
                    time.sleep(0.5)
    
    bot.send_message(
        call.message.chat.id,
        f"✅ **Started {count} scripts**\n\n"
        f"All available scripts have been started.",
        parse_mode='Markdown'
    )

def handle_stop_all_scripts_callback(call):
    """Handle stop all scripts button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    # Confirm action
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("✅ YES, STOP ALL", callback_data='confirm_stop_all'),
        types.InlineKeyboardButton("❌ CANCEL", callback_data='admin_panel')
    )
    
    bot.edit_message_text(
        f"⚠️ **Are you sure you want to stop ALL running scripts?**\n\n"
        f"Currently running: `{len(bot_scripts)}` scripts",
        call.message.chat.id,
        call.message.message_id,
        parse_mode='Markdown',
        reply_markup=markup
    )
    
    bot.answer_callback_query(call.id)

def handle_confirm_stop_all_callback(call):
    """Confirm and stop all scripts"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    bot.answer_callback_query(call.id, "🛑 Stopping all scripts...")
    
    count = 0
    for key, info in list(bot_scripts.items()):
        try:
            kill_process_tree(info)
            if key in bot_scripts:
                del bot_scripts[key]
            count += 1
        except Exception as e:
            logger.error(f"Error stopping script {key}: {e}")
    
    # Update database
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('''UPDATE user_files SET status = 'idle', pid = NULL 
                    WHERE status = 'running' ''')
        c.execute('''UPDATE script_runs SET end_time = ?, status = ? 
                    WHERE status = 'running' ''',
                 (datetime.now().isoformat(), 'stopped_by_admin'))
        conn.commit()
    
    bot.send_message(
        call.message.chat.id,
        f"✅ **Stopped {count} scripts**\n\nAll running processes have been terminated.",
        parse_mode='Markdown',
        reply_markup=create_admin_panel()
    )

def handle_clean_logs_callback(call):
    """Handle clean logs button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    bot.answer_callback_query(call.id, "🧹 Cleaning logs...")
    
    deleted = 0
    size_freed = 0
    cutoff = time.time() - (7 * 24 * 60 * 60)  # 7 days old
    
    # Clean main logs directory
    if os.path.exists(LOGS_DIR):
        for f in os.listdir(LOGS_DIR):
            f_path = os.path.join(LOGS_DIR, f)
            if os.path.isfile(f_path):
                if os.path.getmtime(f_path) < cutoff:
                    size_freed += os.path.getsize(f_path)
                    os.remove(f_path)
                    deleted += 1
    
    # Clean user log files
    for user_id_str in os.listdir(UPLOAD_BOTS_DIR):
        user_log_dir = os.path.join(UPLOAD_BOTS_DIR, user_id_str)
        if os.path.isdir(user_log_dir):
            for f in os.listdir(user_log_dir):
                if f.endswith('.log'):
                    f_path = os.path.join(user_log_dir, f)
                    if os.path.getmtime(f_path) < cutoff:
                        size_freed += os.path.getsize(f_path)
                        os.remove(f_path)
                        deleted += 1
    
    # Send result
    bot.send_message(
        call.message.chat.id,
        f"🧹 **Log Cleanup Complete**\n\n"
        f"📝 **Files Deleted:** `{deleted}`\n"
        f"💾 **Space Freed:** `{format_size(size_freed)}`\n\n"
        f"✅ Logs older than 7 days have been removed.",
        parse_mode='Markdown',
        reply_markup=create_admin_panel()
    )

def handle_restart_bot_callback(call):
    """Handle restart bot button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    # Confirm restart
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("✅ YES, RESTART", callback_data='confirm_restart'),
        types.InlineKeyboardButton("❌ CANCEL", callback_data='admin_panel')
    )
    
    bot.edit_message_text(
        "⚠️ **Are you sure you want to restart the bot?**\n\n"
        "This will temporarily disconnect all users.",
        call.message.chat.id,
        call.message.message_id,
        parse_mode='Markdown',
        reply_markup=markup
    )
    
    bot.answer_callback_query(call.id)

def handle_confirm_restart_callback(call):
    """Confirm and restart bot"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    bot.answer_callback_query(call.id, "🔄 Restarting bot...")
    
    try:
        bot.edit_message_text(
            "🔄 **Restarting Bot**\n\nPlease wait...",
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown'
        )
    except:
        pass
    
    # Cleanup before restart
    cleanup()
    
    # Restart process
    python = sys.executable
    os.execl(python, python, *sys.argv)

def handle_maintenance_mode_callback(call):
    """Handle maintenance mode button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    global bot_locked, maintenance_mode
    bot_locked = not bot_locked
    maintenance_mode = bot_locked
    
    status = "🔴 **ENABLED**" if bot_locked else "🟢 **DISABLED**"
    
    # Update database (removed updated_at)
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('UPDATE settings SET value = ? WHERE key = ?', 
                  (str(bot_locked).lower(), 'bot_locked'))
        conn.commit()
    
    bot.answer_callback_query(call.id, f"Maintenance: {'ON' if bot_locked else 'OFF'}")
    
    try:
        bot.edit_message_text(
            f"⚠️ **Maintenance Mode {status}**\n\n"
            f"{'🔒 Bot is now locked. Only admins can use it.' if bot_locked else '🔓 Bot is now unlocked. All users can access.'}",
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=create_admin_panel()
        )
    except:
        pass

def handle_add_admin_init_callback(call):
    """Handle add admin button"""
    if call.from_user.id != OWNER_ID:
        bot.answer_callback_query(call.id, "⛔ Owner only!", show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    
    msg = bot.send_message(
        call.message.chat.id,
        "👑 **Add New Admin**\n\n"
        "Enter the user ID to promote to admin:\n\n"
        "Format: `123456789`",
        parse_mode='Markdown'
    )
    
    bot.register_next_step_handler(msg, process_add_admin)

def process_add_admin(message):
    """Process add admin"""
    if message.from_user.id != OWNER_ID:
        return
    
    try:
        uid = int(message.text.strip())
        
        if uid == OWNER_ID:
            bot.reply_to(message, "⚠️ The owner is already an admin.")
            return
        
        if uid in admin_ids:
            bot.reply_to(message, "⚠️ This user is already an admin.")
            return
        
        # Add to admin set
        admin_ids.add(uid)
        
        # Add to database
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('''INSERT OR IGNORE INTO admins 
                        (user_id, added_by, added_date, permissions) 
                        VALUES (?, ?, ?, ?)''',
                      (uid, OWNER_ID, datetime.now().isoformat(), 'standard'))
            conn.commit()
        
        # Notify the new admin
        try:
            bot.send_message(
                uid,
                "👑 **Congratulations!**\n\n"
                "You have been promoted to **Admin** in Marco Host.\n\n"
                "You now have access to all admin features.",
                parse_mode='Markdown'
            )
        except:
            pass
        
        bot.reply_to(
            message, 
            f"✅ **Admin Added Successfully!**\n\n"
            f"👤 User ID: `{uid}`\n"
            f"🛡️ Permissions: `standard`",
            parse_mode='Markdown'
        )
        
    except ValueError:
        bot.reply_to(message, "❌ Invalid user ID. Please enter a number.")
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

def handle_remove_admin_init_callback(call):
    """Handle remove admin button"""
    if call.from_user.id != OWNER_ID:
        bot.answer_callback_query(call.id, "⛔ Owner only!", show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    
    # List current admins
    admin_list = []
    for aid in sorted(admin_ids):
        if aid != OWNER_ID:
            try:
                user_info = bot.get_chat(aid)
                name = user_info.first_name or "Unknown"
                username = f"(@{user_info.username})" if user_info.username else ""
                admin_list.append(f"• `{aid}` - {name} {username}")
            except:
                admin_list.append(f"• `{aid}`")
    
    if not admin_list:
        admin_list_text = "No other admins."
    else:
        admin_list_text = "\n".join(admin_list)
    
    msg = bot.send_message(
        call.message.chat.id,
        f"👑 **Remove Admin**\n\n"
        f"**Current Admins:**\n{admin_list_text}\n\n"
        f"Enter the user ID to remove from admin:\n\n"
        f"Format: `123456789`",
        parse_mode='Markdown'
    )
    
    bot.register_next_step_handler(msg, process_remove_admin)

def process_remove_admin(message):
    """Process remove admin"""
    if message.from_user.id != OWNER_ID:
        return
    
    try:
        uid = int(message.text.strip())
        
        if uid == OWNER_ID:
            bot.reply_to(message, "⚠️ Cannot remove the owner.")
            return
        
        if uid not in admin_ids:
            bot.reply_to(message, "⚠️ This user is not an admin.")
            return
        
        # Remove from admin set
        admin_ids.discard(uid)
        
        # Remove from database
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('DELETE FROM admins WHERE user_id = ?', (uid,))
            conn.commit()
        
        # Notify the removed admin
        try:
            bot.send_message(
                uid,
                "👑 **Admin Status Removed**\n\n"
                "Your admin privileges in Marco Host have been removed.",
                parse_mode='Markdown'
            )
        except:
            pass
        
        bot.reply_to(
            message, 
            f"✅ **Admin Removed Successfully!**\n\n"
            f"👤 User ID: `{uid}`",
            parse_mode='Markdown'
        )
        
    except ValueError:
        bot.reply_to(message, "❌ Invalid user ID. Please enter a number.")
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

def handle_list_admins_callback(call):
    """Handle list admins button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    # Get admin details
    admin_list = []
    for aid in sorted(admin_ids):
        try:
            user_info = bot.get_chat(aid)
            name = user_info.first_name or "Unknown"
            username = f"(@{user_info.username})" if user_info.username else ""
            role = "👑 Owner" if aid == OWNER_ID else "🛡️ Admin"
            admin_list.append(f"{role} • `{aid}` - {name} {username}")
        except:
            role = "👑 Owner" if aid == OWNER_ID else "🛡️ Admin"
            admin_list.append(f"{role} • `{aid}`")
    
    admin_text = "👑 **Admin List**\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    admin_text += "\n".join(admin_list)
    admin_text += f"\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nTotal: `{len(admin_ids)}` admins"
    
    bot.answer_callback_query(call.id)
    
    try:
        bot.edit_message_text(
            admin_text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=create_admin_panel()
        )
    except:
        bot.send_message(
            call.message.chat.id,
            admin_text,
            parse_mode='Markdown',
            reply_markup=create_admin_panel()
        )

def handle_admin_permissions_callback(call):
    """Handle admin permissions button"""
    if call.from_user.id != OWNER_ID:
        bot.answer_callback_query(call.id, "⛔ Owner only!", show_alert=True)
        return
    
    permissions_text = f"""
👑 **Admin Permissions Management**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 **Admin Levels:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👑 **Owner** (ID: {OWNER_ID})
• Full system access
• Can add/remove admins
• Can modify all settings
• Can manage subscriptions
• Can restart bot

🛡️ **Admin** (Standard)
• Manage user files
• View statistics
• Broadcast messages
• Lock/unlock bot
• View system stats
• Clean logs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔧 **Permission Levels:**
• `standard` - Basic admin access
• `super` - Extended access (coming soon)
• `owner` - Full access (owner only)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use the buttons below to manage admins.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    bot.answer_callback_query(call.id)
    
    try:
        bot.edit_message_text(
            permissions_text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=create_admin_panel()
        )
    except:
        bot.send_message(
            call.message.chat.id,
            permissions_text,
            parse_mode='Markdown',
            reply_markup=create_admin_panel()
        )

def handle_add_subscription_init_callback(call):
    """Handle add subscription button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    
    msg = bot.send_message(
        call.message.chat.id,
        "💳 **Add Premium Subscription**\n\n"
        "Enter user ID and days (e.g., `12345678 30`)\n\n"
        "Format: `<user_id> <days>`\n"
        "Example: `123456789 30`",
        parse_mode='Markdown'
    )
    
    bot.register_next_step_handler(msg, process_add_subscription)

def process_add_subscription(message):
    """Process add subscription"""
    if message.from_user.id not in admin_ids:
        return
    
    try:
        parts = message.text.split()
        if len(parts) != 2:
            raise ValueError("Invalid format")
        
        uid = int(parts[0])
        days = int(parts[1])
        
        if days <= 0:
            raise ValueError("Days must be positive")
        
        expiry = datetime.now() + timedelta(days=days)
        
        # Save subscription
        save_subscription(uid, expiry)
        
        # Notify user
        try:
            bot.send_message(
                uid,
                f"⭐ **Premium Subscription Activated!**\n\n"
                f"✅ You are now a Premium user!\n"
                f"📅 Expires: {expiry.strftime('%Y-%m-%d')}\n"
                f"⏱️ Duration: {days} days\n\n"
                f"Enjoy your premium benefits! 🚀",
                parse_mode='Markdown'
            )
        except:
            pass
        
        bot.reply_to(
            message,
            f"✅ **Premium Subscription Added!**\n\n"
            f"👤 User ID: `{uid}`\n"
            f"📅 Expires: {expiry.strftime('%Y-%m-%d')}\n"
            f"⏱️ Duration: {days} days",
            parse_mode='Markdown'
        )
        
    except ValueError as e:
        bot.reply_to(
            message, 
            f"❌ Invalid format. Use: `<user_id> <days>`\n\nExample: `123456789 30`",
            parse_mode='Markdown'
        )
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

def handle_remove_subscription_init_callback(call):
    """Handle remove subscription button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    
    msg = bot.send_message(
        call.message.chat.id,
        "💳 **Remove Premium Subscription**\n\n"
        "Enter user ID to remove subscription:\n\n"
        "Format: `123456789`",
        parse_mode='Markdown'
    )
    
    bot.register_next_step_handler(msg, process_remove_subscription)

def process_remove_subscription(message):
    """Process remove subscription"""
    if message.from_user.id not in admin_ids:
        return
    
    try:
        uid = int(message.text.strip())
        
        if uid not in user_subscriptions:
            bot.reply_to(message, "⚠️ This user doesn't have an active subscription.")
            return
        
        # Remove subscription
        remove_subscription_db(uid)
        
        # Notify user
        try:
            bot.send_message(
                uid,
                "💳 **Premium Subscription Removed**\n\n"
                "Your premium subscription has been removed.\n\n"
                "You are now back to free user status.",
                parse_mode='Markdown'
            )
        except:
            pass
        
        bot.reply_to(
            message,
            f"✅ **Subscription Removed!**\n\n"
            f"👤 User ID: `{uid}`",
            parse_mode='Markdown'
        )
        
    except ValueError:
        bot.reply_to(message, "❌ Invalid user ID. Please enter a number.")
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

def handle_check_subscription_init_callback(call):
    """Handle check subscription button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    
    msg = bot.send_message(
        call.message.chat.id,
        "💳 **Check Subscription**\n\n"
        "Enter user ID to check subscription status:\n\n"
        "Format: `123456789`",
        parse_mode='Markdown'
    )
    
    bot.register_next_step_handler(msg, process_check_subscription)

def process_check_subscription(message):
    """Process check subscription"""
    if message.from_user.id not in admin_ids:
        return
    
    try:
        uid = int(message.text.strip())
        
        # Get user info
        try:
            user_info = bot.get_chat(uid)
            name = user_info.first_name or "Unknown"
            username = f"(@{user_info.username})" if user_info.username else ""
        except:
            name = "Unknown"
            username = ""
        
        # Check subscription
        if uid in user_subscriptions:
            expiry = user_subscriptions[uid]['expiry']
            tier = user_subscriptions[uid].get('tier', 'premium')
            
            if expiry > datetime.now():
                days_left = (expiry - datetime.now()).days
                hours_left = ((expiry - datetime.now()).seconds // 3600)
                status = "✅ **ACTIVE**"
                expiry_text = f"📅 Expires: {expiry.strftime('%Y-%m-%d')}\n⏱️ Time left: {days_left} days, {hours_left} hours"
            else:
                status = "❌ **EXPIRED**"
                expiry_text = f"📅 Expired on: {expiry.strftime('%Y-%m-%d')}"
                # Auto remove expired
                remove_subscription_db(uid)
        else:
            status = "🆓 **FREE USER**"
            expiry_text = "No active subscription"
            tier = "free"
        
        # Get user stats
        file_count = get_user_file_count(uid)
        file_limit = get_user_file_limit(uid)
        limit_display = "∞" if file_limit == float('inf') else str(file_limit)
        
        # Check if admin
        is_admin = "✅ Yes" if uid in admin_ids else "❌ No"
        
        result_text = f"""
📊 **Subscription Details**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👤 **User:** {name} {username}
🆔 **ID:** `{uid}`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔰 **Status:** {status}
💎 **Tier:** `{tier.upper()}`
{expiry_text}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 **Storage:**
• Used: `{file_count}` / `{limit_display}` files
• Limit: `{limit_display}`

🛡️ **Admin:** {is_admin}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        
        bot.reply_to(message, result_text, parse_mode='Markdown')
        
    except ValueError:
        bot.reply_to(message, "❌ Invalid user ID. Please enter a number.")
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

def handle_subscription_stats_callback(call):
    """Handle subscription stats button"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "⛔ Admin only!", show_alert=True)
        return
    
    # Get subscription stats
    total_premium = len(user_subscriptions)
    active_premium = 0
    expired_premium = 0
    
    for uid, sub in user_subscriptions.items():
        if sub['expiry'] > datetime.now():
            active_premium += 1
        else:
            expired_premium += 1
    
    # Get tier distribution
    tiers = {}
    for sub in user_subscriptions.values():
        tier = sub.get('tier', 'premium')
        tiers[tier] = tiers.get(tier, 0) + 1
    
    tier_text = "\n".join([f"  • {tier.title()}: {count}" for tier, count in tiers.items()]) if tiers else "  • No premium users"
    
    # Calculate revenue (placeholder)
    premium_price = 10  # $10 per month
    estimated_revenue = active_premium * premium_price
    
    stats_text = f"""
📊 **Subscription Statistics**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💎 **Premium Users:**
• Total: `{total_premium}`
• Active: `{active_premium}`
• Expired: `{expired_premium}`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 **Tier Distribution:**
{tier_text}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 **Estimated Revenue:**
• Monthly: `${estimated_revenue}`
• Yearly: `${estimated_revenue * 12}`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📈 **Conversion Rate:**
• Free Users: `{len(active_users) - active_premium}`
• Premium Rate: `{(active_premium/len(active_users)*100):.1f}%` of active users

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    bot.answer_callback_query(call.id)
    
    try:
        bot.edit_message_text(
            stats_text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=create_admin_panel()
        )
    except:
        bot.send_message(
            call.message.chat.id,
            stats_text,
            parse_mode='Markdown',
            reply_markup=create_admin_panel()
        )

# ======================================================================
# 🔥 TOOLS CALLBACK HANDLERS
# ======================================================================

def handle_tools_npm_callback(call):
    """Handle tools npm install"""
    user_id = call.from_user.id
    
    bot.answer_callback_query(call.id, "📦 Enter npm package name")
    
    msg = bot.send_message(
        call.message.chat.id,
        "📦 **NPM Package Installer**\n\n"
        "Enter the npm package name to install:\n\n"
        "Example: `express` or `discord.js`\n\n"
        "This will be installed in your current directory.",
        parse_mode='Markdown'
    )
    
    bot.register_next_step_handler(msg, lambda m: process_tools_npm(m, user_id))

def process_tools_npm(message, user_id):
    """Process tools npm install"""
    if not message.text:
        bot.reply_to(message, "❌ No package name provided.")
        return
    package = message.text.strip()
    
    if not package:
        bot.reply_to(message, "❌ No package name provided.")
        return
    
    user_folder = get_user_folder(user_id)
    
    status_msg = bot.reply_to(
        message,
        f"📦 **Installing npm package:** `{package}`...",
        parse_mode='Markdown'
    )
    
    try:
        # Check if npm exists
        try:
            subprocess.run(['npm', '--version'], capture_output=True, check=True)
        except:
            bot.edit_message_text(
                f"❌ **npm is not installed** on the server.\n\nCannot install Node packages.",
                message.chat.id, status_msg.message_id,
                parse_mode='Markdown'
            )
            return
        
        result = subprocess.run(
            ['npm', 'install', '--cache', NPM_CACHE_DIR, package],
            cwd=user_folder,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0:
            bot.edit_message_text(
                f"✅ **npm Package Installed!**\n\n"
                f"📦 Package: `{package}`\n"
                f"📍 Location: `{user_folder}`",
                message.chat.id,
                status_msg.message_id,
                parse_mode='Markdown'
            )
        else:
            error = result.stderr[:500]
            bot.edit_message_text(
                f"❌ **Installation Failed**\n\n"
                f"📦 Package: `{package}`\n"
                f"⚠️ Error:\n`{error}`",
                message.chat.id,
                status_msg.message_id,
                parse_mode='Markdown'
            )
    except subprocess.TimeoutExpired:
        bot.edit_message_text(
            f"⚠️ **Installation Timeout**\n\n"
            f"📦 Package: `{package}`\n"
            f"⏱️ Time: 120s",
            message.chat.id,
            status_msg.message_id,
            parse_mode='Markdown'
        )
    except Exception as e:
        bot.edit_message_text(
            f"❌ **Error:** {e}",
            message.chat.id,
            status_msg.message_id,
            parse_mode='Markdown'
        )

def handle_tools_pip_callback(call):
    """Handle tools pip install"""
    user_id = call.from_user.id
    
    bot.answer_callback_query(call.id, "🐍 Enter pip package name")
    
    msg = bot.send_message(
        call.message.chat.id,
        "🐍 **PIP Package Installer**\n\n"
        "Enter the Python package name to install:\n\n"
        "Example: `requests` or `flask`\n\n"
        "This will be installed globally.",
        parse_mode='Markdown'
    )
    
    bot.register_next_step_handler(msg, lambda m: process_tools_pip(m, user_id))

def process_tools_pip(message, user_id):
    """Process tools pip install"""
    if not message.text:
        bot.reply_to(message, "❌ No package name provided.")
        return
    package = message.text.strip()
    
    if not package:
        bot.reply_to(message, "❌ No package name provided.")
        return
    
    status_msg = bot.reply_to(
        message,
        f"🐍 **Installing Python package:** `{package}`...",
        parse_mode='Markdown'
    )
    
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'install', '--cache-dir', PIP_CACHE_DIR, package],
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0:
            bot.edit_message_text(
                f"✅ **pip Package Installed!**\n\n"
                f"🐍 Package: `{package}`",
                message.chat.id,
                status_msg.message_id,
                parse_mode='Markdown'
            )
        else:
            error = result.stderr[:500]
            bot.edit_message_text(
                f"❌ **Installation Failed**\n\n"
                f"🐍 Package: `{package}`\n"
                f"⚠️ Error:\n`{error}`",
                message.chat.id,
                status_msg.message_id,
                parse_mode='Markdown'
            )
    except subprocess.TimeoutExpired:
        bot.edit_message_text(
            f"⚠️ **Installation Timeout**\n\n"
            f"🐍 Package: `{package}`\n"
            f"⏱️ Time: 120s",
            message.chat.id,
            status_msg.message_id,
            parse_mode='Markdown'
        )
    except Exception as e:
        bot.edit_message_text(
            f"❌ **Error:** {e}",
            message.chat.id,
            status_msg.message_id,
            parse_mode='Markdown'
        )

# ======================================================================
# 🔥 MAIN CALLBACK DISPATCHER
# ======================================================================

@bot.callback_query_handler(func=lambda call: True)
def handle_all_callbacks(call):
    """Main callback dispatcher for all inline buttons"""
    data = call.data
    
    try:
        # File management callbacks
        if data.startswith('file_'):
            handle_file_control_callback(call)
        elif data.startswith('start_'):
            handle_start_script_callback(call)
        elif data.startswith('stop_'):
            handle_stop_script_callback(call)
        elif data.startswith('restart_'):
            handle_restart_script_callback(call)
        elif data.startswith('delete_'):
            handle_delete_script_callback(call)
        elif data.startswith('confirm_delete_'):
            handle_confirm_delete_callback(call)
        elif data.startswith('logs_'):
            handle_logs_callback(call)
        elif data.startswith('cpu_'):
            handle_cpu_usage_callback(call)
        elif data.startswith('memory_'):
            handle_memory_callback(call)
        elif data.startswith('uptime_'):
            handle_uptime_callback(call)
        elif data.startswith('details_'):
            handle_details_callback(call)
        elif data.startswith('refresh_'):
            handle_refresh_callback(call)
        elif data.startswith('install_npm_'):
            handle_install_npm_callback(call)
        elif data.startswith('install_pip_'):
            handle_install_pip_callback(call)
        
        # Main menu callbacks
        elif data == 'upload':
            bot.answer_callback_query(call.id)
            bot.send_message(
                call.message.chat.id,
                "📤 **Upload Your File**\n\n"
                "Send me your `.py`, `.js`, or `.zip` file.\n\n"
                "**Supported formats:**\n"
                "• Python scripts (.py)\n"
                "• JavaScript files (.js)\n"
                "• ZIP archives (.zip)\n\n"
                "**Max file size:** 50MB",
                parse_mode='Markdown'
            )
        elif data == 'check_files':
            handle_check_files_callback(call)
        elif data == 'speed':
            handle_speed_test_callback(call)
        elif data == 'stats':
            handle_statistics_callback(call)
        elif data == 'back_to_main':
            handle_back_to_main_callback(call)
        elif data == 'premium_info':
            handle_premium_info_callback(call)
        elif data == 'about':
            handle_about_callback(call)
        elif data == 'tools':
            handle_tools_callback(call)
        elif data == 'help':
            handle_help_callback(call)
        
        # Tools callbacks
        elif data == 'tools_npm':
            handle_tools_npm_callback(call)
        elif data == 'tools_pip':
            handle_tools_pip_callback(call)
        
        # Admin panel callbacks
        elif data == 'admin_panel':
            admin_panel_callback(call)
        elif data == 'system_stats':
            handle_system_stats_callback(call)
        elif data == 'broadcast':
            handle_broadcast_init_callback(call)
        elif data == 'confirm_broadcast':
            handle_confirm_broadcast_callback(call)
        elif data == 'lock_bot':
            handle_lock_bot_callback(call)
        elif data == 'unlock_bot':
            handle_unlock_bot_callback(call)
        elif data == 'run_all_scripts':
            handle_run_all_scripts_callback(call)
        elif data == 'stop_all_scripts':
            handle_stop_all_scripts_callback(call)
        elif data == 'confirm_stop_all':
            handle_confirm_stop_all_callback(call)
        elif data == 'clean_logs':
            handle_clean_logs_callback(call)
        elif data == 'restart_bot':
            handle_restart_bot_callback(call)
        elif data == 'confirm_restart':
            handle_confirm_restart_callback(call)
        elif data == 'maintenance_mode':
            handle_maintenance_mode_callback(call)
        
        # Admin management callbacks
        elif data == 'add_admin':
            handle_add_admin_init_callback(call)
        elif data == 'remove_admin':
            handle_remove_admin_init_callback(call)
        elif data == 'list_admins':
            handle_list_admins_callback(call)
        elif data == 'admin_permissions':
            handle_admin_permissions_callback(call)
        
        # Subscription management callbacks
        elif data == 'add_subscription':
            handle_add_subscription_init_callback(call)
        elif data == 'remove_subscription':
            handle_remove_subscription_init_callback(call)
        elif data == 'check_subscription':
            handle_check_subscription_init_callback(call)
        elif data == 'subscription_stats':
            handle_subscription_stats_callback(call)
        
        # Unknown callback
        else:
            bot.answer_callback_query(call.id, "Unknown action")
            
    except Exception as e:
        logger.error(f"Callback error: {e}", exc_info=True)
        try:
            bot.answer_callback_query(call.id, "❌ Error occurred", show_alert=True)
        except:
            pass

# ======================================================================
# 🔥 ULTIMATE BANNER
# ======================================================================

ULTIMATE_BANNER = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║     ███╗   ███╗ █████╗ ██████╗  ██████╗ ██████╗      ██╗  ██╗ ██████╗ ███████╗████████╗
║     ████╗ ████║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗     ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
║     ██╔████╔██║███████║██████╔╝██║   ██║██████╔╝     ███████║██║   ██║███████╗   ██║   
║     ██║╚██╔╝██║██╔══██║██╔══██╗██║   ██║██╔══██╗     ██╔══██║██║   ██║╚════██║   ██║   
║     ██║ ╚═╝ ██║██║  ██║██║  ██║╚██████╔╝██║  ██║     ██║  ██║╚██████╔╝███████║   ██║   
║     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   
║                                                                              ║
║                    🔥 ULTIMATE PREMIUM HOSTING SOLUTION 🔥                   ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  📦 Python: {:<15}    🟨 Node.js: {:<15}                   ║
║  📁 Base: {:<15}    👑 Owner: {:<15}                   ║
║  🛡️ Admins: {:<15}    ⚡ Uptime: {:<15}                   ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  ✨ ULTIMATE FEATURES LOADED:                                                ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║  ✅ Python 3.11+ Hosting        ✅ Node.js 20+ Hosting                       ║
║  ✅ Auto pip install             ✅ Auto npm install                         ║
║  ✅ ZIP Auto-extract             ✅ Multi-file support                       ║
║  ✅ Real-time Process Monitor    ✅ CPU/RAM per script                       ║
║  ✅ PM2-style Management         ✅ Auto restart on crash                    ║
║  ✅ Premium Subscription System  ✅ Admin Control Panel                      ║
║  ✅ Broadcast System             ✅ Log Management                           ║
║  ✅ Web Dashboard                ✅ REST API                                 ║
║  ✅ 24/7 Auto-Restart            ✅ Enterprise Grade Security                ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

# ======================================================================
# 🔥 CLEANUP FUNCTION
# ======================================================================

def cleanup():
    """Cleanup function - kill all processes on exit"""
    logger.info("🧹 Cleaning up processes...")
    
    count = 0
    for key, info in list(bot_scripts.items()):
        try:
            kill_process_tree(info)
            logger.info(f"✓ Stopped {key}")
            count += 1
        except Exception as e:
            logger.error(f"✗ Error stopping {key}: {e}")
    
    # Update database
    try:
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('''UPDATE user_files SET status = 'idle', pid = NULL 
                        WHERE status = 'running' ''')
            c.execute('''UPDATE script_runs SET end_time = ?, status = ? 
                        WHERE status = 'running' ''',
                     (datetime.now().isoformat(), 'terminated'))
            conn.commit()
    except Exception as e:
        logger.error(f"Database cleanup error: {e}")
    
    logger.info(f"✅ Cleanup complete. Stopped {count} processes.")

# Register cleanup
atexit.register(cleanup)
signal.signal(signal.SIGTERM, lambda sig, frame: cleanup())

# ======================================================================
# 🔥 MAIN EXECUTION
# ======================================================================

if __name__ == '__main__':
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print ultimate banner
    print(ULTIMATE_BANNER.format(
        sys.version.split()[0],
        get_node_version(),
        os.path.basename(BASE_DIR)[:15],
        str(OWNER_ID)[:15],
        str(len(admin_ids))[:15],
        format_time(time.time() - start_time)[:15]
    ))
    
    logger.info("🚀 Starting ULTIMATE PREMIUM HOSTING BOT...")
    
    # Start web dashboard
    keep_alive()
    logger.info(f"🌐 Ultimate Web Dashboard: http://localhost:{os.environ.get('PORT', 8080)}")
    
    # Log system info
    logger.info(f"📊 Python Version: {sys.version}")
    logger.info(f"📊 Node.js Version: {get_node_version()}")
    logger.info(f"📊 npm Version: {get_npm_version()}")
    logger.info(f"📊 Platform: {platform.platform()}")
    logger.info(f"📊 Hostname: {socket.gethostname()}")
    
    # Log database stats
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM user_files')
        total_files = c.fetchone()[0]
        c.execute('SELECT COUNT(*) FROM script_runs')
        total_runs = c.fetchone()[0]
    
    logger.info(f"📊 Total Files: {total_files}")
    logger.info(f"📊 Total Script Runs: {total_runs}")
    logger.info(f"📊 Active Users: {len(active_users)}")
    logger.info(f"📊 Premium Users: {len(user_subscriptions)}")
    logger.info(f"📊 Admins: {len(admin_ids)}")
    
    logger.info("✅ Bot is ready! Starting polling...")
    
    # Main polling loop with auto-restart
    while True:
        try:
            logger.info("🔄 Starting polling...")
            bot.infinity_polling(timeout=60, long_polling_timeout=30)
        except requests.exceptions.ReadTimeout:
            logger.warning("⏰ Read timeout, restarting polling in 5 seconds...")
            time.sleep(5)
        except requests.exceptions.ConnectionError:
            logger.warning("🔌 Connection error, restarting in 15 seconds...")
            time.sleep(15)
        except Exception as e:
            logger.error(f"💥 Critical polling error: {e}", exc_info=True)
            logger.info("🔄 Restarting in 30 seconds...")
            time.sleep(30)

# ======================================================================
# 🔥 END OF ULTIMATE MARCO HOST BOT
# ======================================================================
print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║     ███████╗███╗   ██╗██████╗     ██████╗ ███████╗                         ║
║     ██╔════╝████╗  ██║██╔══██╗    ██╔══██╗██╔════╝                         ║
║     █████╗  ██╔██╗ ██║██║  ██║    ██║  ██║█████╗                           ║
║     ██╔══╝  ██║╚██╗██║██║  ██║    ██║  ██║██╔══╝                           ║
║     ███████╗██║ ╚████║██████╔╝    ██████╔╝███████╗                         ║
║     ╚══════╝╚═╝  ╚═══╝╚═════╝     ╚═════╝ ╚══════╝                         ║
║                                                                              ║
║     ███╗   ███╗ █████╗ ██████╗  ██████╗ ██████╗      ██╗  ██╗ ██████╗ ███████╗████████╗
║     ████╗ ████║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗     ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
║     ██╔████╔██║███████║██████╔╝██║   ██║██████╔╝     ███████║██║   ██║███████╗   ██║   
║     ██║╚██╔╝██║██╔══██║██╔══██╗██║   ██║██╔══██╗     ██╔══██║██║   ██║╚════██║   ██║   
║     ██║ ╚═╝ ██║██║  ██║██║  ██║╚██████╔╝██║  ██║     ██║  ██║╚██████╔╝███████║   ██║   
║     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   
║                                                                              ║
║                          🔥 BOT STARTED SUCCESSFULLY! 🔥                      ║
║                                                                              ║
║                      ✅ ALL ERRORS FIXED • READY FOR PRODUCTION              ║
║                                                                              ║
║                      🤖 Join: @Zinko158 • Channel: @NLb-9NFUSiY1YjVl         ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
""")
