# -*- coding: utf-8 -*-
"""
███████ ██   ██ ███████ ███████ ████████ 
██      ██   ██ ██      ██         ██    
█████   ███████ █████   █████      ██    
██      ██   ██ ██      ██         ██    
███████ ██   ██ ███████ ███████    ██    

🤖 MARCO FILE HOST - ULTIMATE EDITION v5.0
✨ ZERO SLASH COMMANDS - 100% Reply Keyboard + Inline Buttons
📦 Advanced Python & Node.js Hosting with Auto Dependencies
🔥 Enhanced Features: Multi-Script Support, Resource Monitoring, Auto Backup
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
from threading import Thread, Lock

# Optional imports - handle gracefully if not available
try:
    import croniter
    CRONITER_AVAILABLE = True
except ImportError:
    CRONITER_AVAILABLE = False
    print("⚠️ croniter not installed - scheduled tasks disabled")

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False
    print("⚠️ yaml not installed - YAML support disabled")

# --- Flask Keep Alive ---
from flask import Flask, jsonify, render_template_string, request, send_file

app = Flask('')

@app.route('/favicon.ico')
def favicon():
    return '', 204
    import os
from dotenv import load_dotenv

# Load .env file if exists (for local development)
load_dotenv()

HTML_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
    <title>🔥 Marco File Host - Ultimate Status</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0; padding: 0; min-height: 100vh;
            display: flex; justify-content: center; align-items: center; color: white;
        }
        .container {
            background: rgba(255,255,255,0.95); border-radius: 20px; padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3); max-width: 900px; width: 90%; color: #333;
        }
        h1 { color: #764ba2; border-bottom: 3px solid #667eea; padding-bottom: 10px; margin-bottom: 30px; }
        .status-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 20px; }
        .status-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;
            padding: 20px; border-radius: 15px; box-shadow: 0 10px 30px rgba(102,126,234,0.3);
        }
        .status-card h3 { margin-top: 0; font-size: 1.2em; }
        .status-value { font-size: 2em; font-weight: bold; margin: 10px 0; }
        .badge { display: inline-block; padding: 5px 15px; border-radius: 20px; font-size: 0.9em; font-weight: bold; }
        .badge-success { background: #10b981; color: white; }
        .badge-warning { background: #f59e0b; color: white; }
        .badge-danger { background: #ef4444; color: white; }
        .footer { margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee; text-align: center; color: #666; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background: #667eea; color: white; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔥 MARCO FILE HOST ULTIMATE</h1>
        <div class="badge badge-success" style="margin-bottom: 20px;">🟢 SYSTEM ONLINE</div>
        <div class="status-grid">
            <div class="status-card"><h3>⏰ Uptime</h3><div class="status-value">{{ uptime }}</div><small>Running smoothly</small></div>
            <div class="status-card"><h3>📊 Active Scripts</h3><div class="status-value">{{ active_scripts }}</div><small>Running processes</small></div>
            <div class="status-card"><h3>👥 Total Users</h3><div class="status-value">{{ total_users }}</div><small>Active users</small></div>
            <div class="status-card"><h3>💾 Memory</h3><div class="status-value">{{ memory_usage }}%</div><small>RAM usage</small></div>
        </div>
        
        <div style="margin-top: 30px;">
            <h3>📁 System Info</h3>
            <table>
                <tr><th>Hostname</th><td>{{ hostname }}</td></tr>
                <tr><th>Platform</th><td>{{ platform }}</td></tr>
                <tr><th>Python</th><td>{{ python_version }}</td></tr>
                <tr><th>Node.js</th><td>{{ node_version }}</td></tr>
                <tr><th>IP Address</th><td>{{ ip_address }}</td></tr>
                <tr><th>CPU Cores</th><td>{{ cpu_cores }}</td></tr>
                <tr><th>Disk Usage</th><td>{{ disk_usage }}%</td></tr>
            </table>
        </div>
        
        <div style="margin-top: 30px;">
            <h3>📊 Active Processes</h3>
            <table>
                <tr><th>User</th><th>Script</th><th>PID</th><th>CPU%</th><th>MEM%</th><th>Uptime</th></tr>
                {% for proc in processes %}
                <tr>
                    <td>{{ proc.user_id }}</td>
                    <td>{{ proc.file_name }}</td>
                    <td>{{ proc.pid }}</td>
                    <td>{{ proc.cpu }}%</td>
                    <td>{{ proc.mem }}%</td>
                    <td>{{ proc.uptime }}</td>
                </tr>
                {% endfor %}
            </table>
        </div>
        
        <div class="footer">
            <p>🤖 Powered by @Zinko158 • Ultimate Hosting Solution v5.0</p>
            <p>📢 <a href="{{ update_channel }}" style="color: #667eea;">Join Updates Channel</a></p>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    try:
        uptime_seconds = time.time() - start_time
        uptime_str = str(timedelta(seconds=int(uptime_seconds)))
        
        try:
            memory_usage = psutil.virtual_memory().percent
            hostname = socket.gethostname()
            platform_info = platform.platform()
            ip_address = socket.gethostbyname(socket.gethostname())
            cpu_cores = psutil.cpu_count()
            disk_usage = psutil.disk_usage('/').percent
        except:
            memory_usage = 0
            hostname = 'N/A'
            platform_info = 'N/A'
            ip_address = 'N/A'
            cpu_cores = 'N/A'
            disk_usage = 'N/A'
        
        node_ver = get_node_version()
        
        # Get process info
        processes = []
        for key, info in list(bot_scripts.items()):
            try:
                proc = psutil.Process(info['pid'])
                cpu = proc.cpu_percent(interval=0.1)
                mem = proc.memory_percent()
                uptime_proc = str(timedelta(seconds=int(time.time() - info['start_time'].timestamp())))
                processes.append({
                    'user_id': info['user_id'],
                    'file_name': info['file_name'],
                    'pid': info['pid'],
                    'cpu': round(cpu, 1),
                    'mem': round(mem, 1),
                    'uptime': uptime_proc
                })
            except:
                pass
        
        return render_template_string(
            HTML_TEMPLATE,
            uptime=uptime_str,
            active_scripts=len(bot_scripts),
            total_users=len(active_users),
            memory_usage=memory_usage,
            hostname=hostname,
            platform=platform_info,
            python_version=sys.version.split()[0],
            node_version=node_ver,
            ip_address=ip_address,
            update_channel=UPDATE_CHANNEL,
            cpu_cores=cpu_cores,
            disk_usage=disk_usage,
            processes=processes
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
        'maintenance': maintenance_mode
    })

@app.route('/download/<user_id>/<filename>')
def download_file(user_id, filename):
    """Allow file download via web"""
    try:
        user_folder = get_user_folder(int(user_id))
        file_path = os.path.join(user_folder, filename)
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        return "File not found", 404
    except:
        return "Error", 500

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False, threaded=True)

def keep_alive():
    t = threading.Thread(target=run_flask, daemon=True)
    t.start()
    print(f"✨ Flask Status Server started on port {os.environ.get('PORT', 8080)}")

# --- Configuration ---
TOKEN = os.getenv('TOKEN')  # Default for local testing
OWNER_ID = int(os.getenv('OWNER_ID'))
YOUR_USERNAME = os.getenv('YOUR_USERNAME')
UPDATE_CHANNEL = 'https://t.me/+NLb-9NFUSiY1YjVl'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_BOTS_DIR = os.path.join(BASE_DIR, 'upload_bots')
IROTECH_DIR = os.path.join(BASE_DIR, 'inf')
DATABASE_PATH = os.path.join(IROTECH_DIR, 'bot_data.db')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
NPM_CACHE_DIR = os.path.join(BASE_DIR, 'npm_cache')
PIP_CACHE_DIR = os.path.join(BASE_DIR, 'pip_cache')
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')
TEMP_DIR = os.path.join(BASE_DIR, 'temp')

for dir_path in [UPLOAD_BOTS_DIR, IROTECH_DIR, LOGS_DIR, NPM_CACHE_DIR, PIP_CACHE_DIR, BACKUP_DIR, TEMP_DIR]:
    os.makedirs(dir_path, exist_ok=True)

FREE_USER_LIMIT = 5
SUBSCRIBED_USER_LIMIT = 15
ADMIN_LIMIT = 999
OWNER_LIMIT = float('inf')
PREMIUM_USER_LIMIT = 30
MAX_SCRIPT_SIZE = 100 * 1024 * 1024  # 100MB
MAX_RAM_PER_SCRIPT = 500 * 1024 * 1024  # 500MB
MAX_CPU_PER_SCRIPT = 50  # 50% CPU limit

bot = telebot.TeleBot(TOKEN)

bot_scripts = {}  # script_key: info
user_subscriptions = {}  # user_id: {'expiry': datetime}
user_files = {}  # user_id: [(filename, filetype)]
active_users = set()
admin_ids = {OWNER_ID}
bot_locked = False
maintenance_mode = False
start_time = time.time()

script_executor = ThreadPoolExecutor(max_workers=20)
broadcast_queue = Queue()
log_cleanup_queue = Queue()
backup_lock = Lock()

# --- Logging Setup ---
class ColoredFormatter(logging.Formatter):
    grey = "\x1b[38;21m"
    blue = "\x1b[38;5;39m"
    yellow = "\x1b[38;5;226m"
    red = "\x1b[38;5;196m"
    bold_red = "\x1b[31;1m"
    green = "\x1b[38;5;40m"
    cyan = "\x1b[38;5;51m"
    reset = "\x1b[0m"
    
    FORMATS = {
        logging.DEBUG: grey + "[DEBUG] %(message)s" + reset,
        logging.INFO: green + "[INFO] %(message)s" + reset,
        logging.WARNING: yellow + "[WARNING] %(message)s" + reset,
        logging.ERROR: red + "[ERROR] %(message)s" + reset,
        logging.CRITICAL: bold_red + "[CRITICAL] %(message)s" + reset
    }
    
    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%Y-%m-%d %H:%M:%S')
        return formatter.format(record)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(ColoredFormatter())
logger.addHandler(console_handler)

log_file = os.path.join(LOGS_DIR, f'bot_{datetime.now().strftime("%Y%m%d")}.log')
file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# --- Database Manager ---
class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self._init_db()
    
    def get_connection(self):
        return sqlite3.connect(self.db_path, timeout=30)
    
    def _init_db(self):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS subscriptions
                         (user_id INTEGER PRIMARY KEY, expiry TEXT, tier TEXT DEFAULT 'basic',
                          added_by INTEGER, added_date TEXT)''')
            c.execute('''CREATE TABLE IF NOT EXISTS user_files
                         (user_id INTEGER, file_name TEXT, file_type TEXT, file_size INTEGER,
                          upload_date TEXT, last_run TEXT, run_count INTEGER DEFAULT 0,
                          PRIMARY KEY (user_id, file_name))''')  # Removed download_url column
            c.execute('''CREATE TABLE IF NOT EXISTS active_users
                         (user_id INTEGER PRIMARY KEY, username TEXT, first_name TEXT,
                          last_seen TEXT, join_date TEXT, total_uploads INTEGER DEFAULT 0,
                          total_runs INTEGER DEFAULT 0)''')
            c.execute('''CREATE TABLE IF NOT EXISTS admins
                         (user_id INTEGER PRIMARY KEY, added_by INTEGER, added_date TEXT,
                          permissions TEXT DEFAULT 'standard')''')
            c.execute('''CREATE TABLE IF NOT EXISTS script_runs
                         (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, file_name TEXT,
                          start_time TEXT, end_time TEXT, status TEXT, pid INTEGER,
                          cpu_usage REAL, memory_usage REAL)''')
            c.execute('''CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT)''')
            c.execute('''CREATE TABLE IF NOT EXISTS scheduled_tasks
                         (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, file_name TEXT,
                          cron_pattern TEXT, next_run TEXT, enabled INTEGER DEFAULT 1)''')
            c.execute('''CREATE TABLE IF NOT EXISTS backups
                         (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, file_name TEXT,
                          backup_path TEXT, backup_date TEXT)''')
            c.execute('INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)', ('bot_locked', 'false'))
            c.execute('INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)', ('maintenance_mode', 'false'))
            conn.commit()
        logger.info("✅ Database initialized")

db_manager = DatabaseManager(DATABASE_PATH)

# --- Load data from DB at startup ---
def load_all_data():
    global user_subscriptions, user_files, active_users, admin_ids, bot_locked, maintenance_mode
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT user_id, expiry FROM subscriptions')
        for row in c.fetchall():
            try:
                expiry = datetime.fromisoformat(row[1])
                if expiry > datetime.now():
                    user_subscriptions[row[0]] = {'expiry': expiry}
            except:
                pass
        
        c.execute('SELECT user_id, file_name, file_type FROM user_files')
        for user_id, fname, ftype in c.fetchall():
            if user_id not in user_files:
                user_files[user_id] = []
            user_files[user_id].append((fname, ftype))
            
        c.execute('SELECT user_id FROM active_users')
        for row in c.fetchall():
            active_users.add(row[0])
            
        c.execute('SELECT user_id FROM admins')
        for row in c.fetchall():
            admin_ids.add(row[0])
        admin_ids.add(OWNER_ID)
        
        c.execute('SELECT value FROM settings WHERE key = "bot_locked"')
        row = c.fetchone()
        if row:
            bot_locked = row[0] == 'true'
        
        c.execute('SELECT value FROM settings WHERE key = "maintenance_mode"')
        row = c.fetchone()
        if row:
            maintenance_mode = row[0] == 'true'
            
    logger.info(f"📊 Loaded: {len(user_subscriptions)} subscriptions, {len(active_users)} active users, {len(admin_ids)} admins")

load_all_data()

# --- Helper Functions ---
def get_user_folder(user_id):
    user_folder = os.path.join(UPLOAD_BOTS_DIR, str(user_id))
    os.makedirs(user_folder, exist_ok=True)
    return user_folder

def get_user_file_limit(user_id):
    if user_id == OWNER_ID:
        return float('inf')
    if user_id in admin_ids:
        return ADMIN_LIMIT
    if user_id in user_subscriptions and user_subscriptions[user_id].get('expiry', datetime.min) > datetime.now():
        return SUBSCRIBED_USER_LIMIT
    return FREE_USER_LIMIT

def get_user_file_count(user_id):
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM user_files WHERE user_id = ?', (user_id,))
        return c.fetchone()[0]

def get_node_version():
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True, timeout=5)
        return result.stdout.strip() or 'Not installed'
    except:
        return 'Not installed'

def format_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024.0:
            return f"{bytes:.1f} {unit}"
        bytes /= 1024.0
    return f"{bytes:.1f} TB"

def format_time(seconds):
    return str(timedelta(seconds=int(seconds)))

def generate_unique_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def get_system_stats():
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        try:
            net = psutil.net_io_counters()
            bytes_sent = net.bytes_sent
            bytes_recv = net.bytes_recv
        except:
            bytes_sent = 0
            bytes_recv = 0
        
        return {
            'cpu': cpu_percent,
            'memory_used': memory.used,
            'memory_total': memory.total,
            'memory_percent': memory.percent,
            'disk_used': disk.used,
            'disk_total': disk.total,
            'disk_percent': disk.percent,
            'processes': len(psutil.pids()),
            'bytes_sent': bytes_sent,
            'bytes_recv': bytes_recv
        }
    except:
        return {
            'cpu': 0,
            'memory_percent': 0,
            'disk_percent': 0,
            'processes': 0,
            'bytes_sent': 0,
            'bytes_recv': 0
        }

def is_bot_running(owner_id, file_name):
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
    try:
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
                for child in children:
                    try:
                        child.terminate()
                    except:
                        try:
                            child.kill()
                        except:
                            pass
                parent.terminate()
                try:
                    parent.wait(timeout=1)
                except:
                    parent.kill()
            except:
                pass
    except Exception as e:
        logger.error(f"Error killing process: {e}")

# --- Resource Monitor ---
def resource_monitor():
    """Monitor running scripts and kill if they exceed limits"""
    while True:
        try:
            for key, info in list(bot_scripts.items()):
                if not info.get('process'):
                    continue
                try:
                    proc = psutil.Process(info['process'].pid)
                    mem_usage = proc.memory_info().rss
                    cpu_usage = proc.cpu_percent(interval=0.1)
                    
                    # Log resource usage
                    with db_manager.get_connection() as conn:
                        c = conn.cursor()
                        c.execute('''UPDATE script_runs SET cpu_usage = ?, memory_usage = ? 
                                     WHERE user_id = ? AND file_name = ? AND status = 'running' ''',
                                  (cpu_usage, mem_usage, info['user_id'], info['file_name']))
                        conn.commit()
                    
                    # Kill if exceeds limits
                    if mem_usage > MAX_RAM_PER_SCRIPT:
                        logger.warning(f"🔥 Process {key} exceeded RAM limit ({mem_usage/1024/1024:.2f}MB). Killing...")
                        kill_process_tree(info)
                        try:
                            bot.send_message(info['user_id'], f"⚠️ Script `{info['file_name']}` killed: RAM limit exceeded")
                        except:
                            pass
                        if key in bot_scripts:
                            del bot_scripts[key]
                    
                    elif cpu_usage > MAX_CPU_PER_SCRIPT:
                        logger.warning(f"🔥 Process {key} exceeded CPU limit ({cpu_usage}%). Killing...")
                        kill_process_tree(info)
                        try:
                            bot.send_message(info['user_id'], f"⚠️ Script `{info['file_name']}` killed: CPU limit exceeded")
                        except:
                            pass
                        if key in bot_scripts:
                            del bot_scripts[key]
                        
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    if key in bot_scripts:
                        del bot_scripts[key]
        except Exception as e:
            logger.error(f"Resource monitor error: {e}")
        time.sleep(5)

Thread(target=resource_monitor, daemon=True).start()

# --- Backup System ---
def create_backup(user_id, file_name):
    """Create a backup of a file"""
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    if not os.path.exists(file_path):
        return None
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{user_id}_{file_name}_{timestamp}.backup"
    backup_path = os.path.join(BACKUP_DIR, backup_name)
    
    shutil.copy2(file_path, backup_path)
    
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('''INSERT INTO backups (user_id, file_name, backup_path, backup_date)
                     VALUES (?, ?, ?, ?)''',
                  (user_id, file_name, backup_path, datetime.now().isoformat()))
        conn.commit()
    
    return backup_path

def list_backups(user_id, file_name=None):
    """List backups for a user"""
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        if file_name:
            c.execute('''SELECT id, file_name, backup_date FROM backups 
                         WHERE user_id = ? AND file_name = ? ORDER BY backup_date DESC''',
                      (user_id, file_name))
        else:
            c.execute('''SELECT id, file_name, backup_date FROM backups 
                         WHERE user_id = ? ORDER BY backup_date DESC''', (user_id,))
        return c.fetchall()

def restore_backup(backup_id):
    """Restore a backup"""
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT user_id, file_name, backup_path FROM backups WHERE id = ?', (backup_id,))
        row = c.fetchone()
        if not row:
            return None
        user_id, file_name, backup_path = row
    
    if not os.path.exists(backup_path):
        return None
    
    user_folder = get_user_folder(user_id)
    dest_path = os.path.join(user_folder, file_name)
    shutil.copy2(backup_path, dest_path)
    
    return file_name

# --- Scheduled Tasks (only if croniter is available) ---
if CRONITER_AVAILABLE:
    def schedule_checker():
        """Check and run scheduled tasks"""
        while True:
            try:
                now = datetime.now()
                with db_manager.get_connection() as conn:
                    c = conn.cursor()
                    c.execute('''SELECT id, user_id, file_name, cron_pattern FROM scheduled_tasks 
                                 WHERE enabled = 1 AND next_run <= ?''', (now.isoformat(),))
                    tasks = c.fetchall()
                    
                    for task_id, user_id, file_name, cron_pattern in tasks:
                        # Run the script
                        user_folder = get_user_folder(user_id)
                        file_path = os.path.join(user_folder, file_name)
                        
                        with db_manager.get_connection() as conn2:
                            c2 = conn2.cursor()
                            c2.execute('SELECT file_type FROM user_files WHERE user_id = ? AND file_name = ?', (user_id, file_name))
                            row = c2.fetchone()
                            if row:
                                file_type = row[0]
                                # Run in background
                                class FakeMessage:
                                    def __init__(self):
                                        self.chat = type('obj', (object,), {'id': user_id})
                                        self.from_user = type('obj', (object,), {'id': user_id})
                                        self.text = ""
                                
                                fake_msg = FakeMessage()
                                threading.Thread(
                                    target=script_runner.run_script,
                                    args=(file_path, user_id, user_folder, file_name, fake_msg, file_type)
                                ).start()
                        
                        # Calculate next run
                        cron = croniter.croniter(cron_pattern, now)
                        next_run = cron.get_next(datetime)
                        
                        with db_manager.get_connection() as conn2:
                            c2 = conn2.cursor()
                            c2.execute('UPDATE scheduled_tasks SET next_run = ? WHERE id = ?', (next_run.isoformat(), task_id))
                            conn2.commit()
            except Exception as e:
                logger.error(f"Schedule checker error: {e}")
            time.sleep(60)

    Thread(target=schedule_checker, daemon=True).start()

# --- File Management ---
class FileManager:
    @staticmethod
    def save_file(user_id, file_content, file_name):
        user_folder = get_user_folder(user_id)
        file_path = os.path.join(user_folder, file_name)
        file_size = len(file_content)
        
        if os.path.exists(file_path):
            base, ext = os.path.splitext(file_name)
            counter = 1
            while os.path.exists(os.path.join(user_folder, f"{base}_{counter}{ext}")):
                counter += 1
            file_name = f"{base}_{counter}{ext}"
            file_path = os.path.join(user_folder, file_name)
            
        with open(file_path, 'wb') as f:
            f.write(file_content)
        
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('''INSERT OR REPLACE INTO user_files 
                         (user_id, file_name, file_type, file_size, upload_date)
                         VALUES (?, ?, ?, ?, ?)''',
                      (user_id, file_name, os.path.splitext(file_name)[1][1:].lower(),
                       file_size, datetime.now().isoformat()))
            conn.commit()
            
        if user_id not in user_files:
            user_files[user_id] = []
        user_files[user_id] = [(f, t) for f, t in user_files[user_id] if f != file_name]
        user_files[user_id].append((file_name, os.path.splitext(file_name)[1][1:].lower()))
        
        # Create backup
        create_backup(user_id, file_name)
        
        return file_path, file_size

    @staticmethod
    def delete_file(user_id, file_name):
        user_folder = get_user_folder(user_id)
        file_path = os.path.join(user_folder, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        
        for f in os.listdir(user_folder):
            if f.startswith(os.path.splitext(file_name)[0]) and f.endswith('.log'):
                try:
                    os.remove(os.path.join(user_folder, f))
                except:
                    pass
                
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('DELETE FROM user_files WHERE user_id = ? AND file_name = ?', (user_id, file_name))
            c.execute('DELETE FROM scheduled_tasks WHERE user_id = ? AND file_name = ?', (user_id, file_name))
            conn.commit()
            
        if user_id in user_files:
            user_files[user_id] = [f for f in user_files[user_id] if f[0] != file_name]
            if not user_files[user_id]:
                del user_files[user_id]
        return True

# --- Script Runner (Enhanced) ---
class ScriptRunner:
    def __init__(self):
        self.running_scripts = {}
        self.script_queue = Queue()
        self.start_worker()
    
    def start_worker(self):
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
    
    def _execute_script(self, script_info):
        script_path, user_id, user_folder, file_name, message, file_type = script_info
        script_key = f"{user_id}_{file_name}"
        chat_id = None
        if message and hasattr(message, 'chat') and hasattr(message.chat, 'id'):
            chat_id = message.chat.id
        else:
            chat_id = user_id
        
        # Check if already running
        if is_bot_running(user_id, file_name):
            if chat_id:
                try:
                    bot.send_message(chat_id, f"⚠️ Script `{file_name}` is already running.")
                except:
                    pass
            return
        
        if file_type == 'js':
            if not self._check_node(chat_id):
                return
            self._run_npm_install_if_needed(user_folder, chat_id)
        elif file_type == 'py':
            self._run_pip_install_if_needed(user_folder, chat_id)
        
        try:
            env = os.environ.copy()
            env['PYTHONUNBUFFERED'] = '1'
            env['NODE_ENV'] = 'production'
            env['USER_ID'] = str(user_id)
            env['SCRIPT_NAME'] = file_name
            
            if file_type == 'js':
                node_modules = os.path.join(user_folder, 'node_modules')
                if os.path.exists(node_modules):
                    env['NODE_PATH'] = node_modules + (':' + env.get('NODE_PATH', '') if 'NODE_PATH' in env else '')
            
            log_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}_{generate_unique_id()}.log")
            log_file = open(log_path, 'w', encoding='utf-8')
            
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
            else:
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
            
            def wait_and_close():
                process.wait()
                try:
                    if not log_file.closed:
                        log_file.close()
                except:
                    pass
                
                # Update run count
                with db_manager.get_connection() as conn:
                    c = conn.cursor()
                    c.execute('''UPDATE user_files SET run_count = run_count + 1, last_run = ? 
                                 WHERE user_id = ? AND file_name = ?''',
                              (datetime.now().isoformat(), user_id, file_name))
                    c.execute('''UPDATE script_runs SET end_time = ?, status = ? 
                                 WHERE user_id = ? AND file_name = ? AND status = 'running' ''',
                              (datetime.now().isoformat(), 'finished', user_id, file_name))
                    conn.commit()
                    
                if script_key in bot_scripts:
                    del bot_scripts[script_key]
                
                # Notify if crashed
                if process.returncode != 0 and chat_id:
                    try:
                        bot.send_message(chat_id, f"⚠️ Script `{file_name}` crashed with code {process.returncode}")
                    except:
                        pass
            
            Thread(target=wait_and_close, daemon=True).start()
            
            with db_manager.get_connection() as conn:
                c = conn.cursor()
                c.execute('''INSERT INTO script_runs (user_id, file_name, start_time, status, pid)
                            VALUES (?, ?, ?, ?, ?)''',
                         (user_id, file_name, datetime.now().isoformat(), 'running', process.pid))
                conn.commit()
                
            logger.info(f"✅ Started {file_type.upper()} script: {file_name} (PID: {process.pid})")
            
            if chat_id:
                try:
                    bot.send_message(chat_id, f"🚀 Script `{file_name}` started successfully.", parse_mode='Markdown')
                except:
                    pass
                
        except Exception as e:
            logger.error(f"❌ Failed to start script {file_name}: {e}")
            if chat_id:
                try:
                    bot.send_message(chat_id, f"❌ Failed to start script: {e}")
                except:
                    pass
    
    def _check_node(self, chat_id):
        try:
            subprocess.run(['node', '--version'], capture_output=True, check=True, timeout=5)
            return True
        except:
            if chat_id:
                try:
                    bot.send_message(chat_id, "❌ **Node.js is not installed** on the server.", parse_mode='Markdown')
                except:
                    pass
            return False
    
    def _run_npm_install_if_needed(self, user_folder, chat_id):
        package_json = os.path.join(user_folder, 'package.json')
        if os.path.exists(package_json):
            def install():
                try:
                    bot.send_message(chat_id, "📦 **Found package.json, running npm install...**", parse_mode='Markdown')
                    result = subprocess.run(
                        ['npm', 'install', '--cache', NPM_CACHE_DIR],
                        cwd=user_folder,
                        capture_output=True,
                        text=True,
                        timeout=300
                    )
                    if result.returncode == 0:
                        bot.send_message(chat_id, "✅ **npm install completed successfully.**", parse_mode='Markdown')
                    else:
                        error = result.stderr[:500]
                        bot.send_message(chat_id, f"⚠️ **npm install had issues:**\n`{error}`", parse_mode='Markdown')
                except subprocess.TimeoutExpired:
                    bot.send_message(chat_id, "⚠️ **npm install timed out.**", parse_mode='Markdown')
                except Exception as e:
                    bot.send_message(chat_id, f"❌ **npm install error:** {e}", parse_mode='Markdown')
            Thread(target=install, daemon=True).start()
    
    def _run_pip_install_if_needed(self, user_folder, chat_id):
        requirements_txt = os.path.join(user_folder, 'requirements.txt')
        if os.path.exists(requirements_txt):
            def install():
                try:
                    bot.send_message(chat_id, "🐍 **Found requirements.txt, running pip install...**", parse_mode='Markdown')
                    result = subprocess.run(
                        [sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt', '--cache-dir', PIP_CACHE_DIR],
                        cwd=user_folder,
                        capture_output=True,
                        text=True,
                        timeout=300
                    )
                    if result.returncode == 0:
                        bot.send_message(chat_id, "✅ **pip install completed successfully.**", parse_mode='Markdown')
                    else:
                        error = result.stderr[:500]
                        bot.send_message(chat_id, f"⚠️ **pip install had issues:**\n`{error}`", parse_mode='Markdown')
                except subprocess.TimeoutExpired:
                    bot.send_message(chat_id, "⚠️ **pip install timed out.**", parse_mode='Markdown')
                except Exception as e:
                    bot.send_message(chat_id, f"❌ **pip install error:** {e}", parse_mode='Markdown')
            Thread(target=install, daemon=True).start()
    
    def run_script(self, script_path, user_id, user_folder, file_name, message, file_type='py'):
        self.script_queue.put((script_path, user_id, user_folder, file_name, message, file_type))
        return f"🔄 Script '{file_name}' queued for execution"

script_runner = ScriptRunner()

def run_script(script_path, user_id, user_folder, file_name, message):
    script_runner.run_script(script_path, user_id, user_folder, file_name, message, 'py')

def run_js_script(script_path, user_id, user_folder, file_name, message):
    script_runner.run_script(script_path, user_id, user_folder, file_name, message, 'js')

# --- Package Installer (Enhanced) ---
class PackageInstaller:
    def __init__(self):
        self.install_lock = Lock()
        self.install_queue = Queue()
        self.start_installer()
    
    def start_installer(self):
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
    
    def _install_package(self, pkg_info):
        package, user_id, message, pkg_type = pkg_info
        with self.install_lock:
            try:
                if pkg_type == 'python':
                    status_msg = bot.reply_to(message, f"🐍 Installing Python package: `{package}`...")
                    result = subprocess.run(
                        [sys.executable, '-m', 'pip', 'install', '--cache-dir', PIP_CACHE_DIR, package],
                        capture_output=True,
                        text=True,
                        timeout=300
                    )
                else:
                    status_msg = bot.reply_to(message, f"📦 Installing Node package: `{package}`...")
                    user_folder = get_user_folder(user_id)
                    result = subprocess.run(
                        ['npm', 'install', '--cache', NPM_CACHE_DIR, package],
                        cwd=user_folder,
                        capture_output=True,
                        text=True,
                        timeout=300
                    )
                    
                if result.returncode == 0:
                    bot.edit_message_text(
                        f"✅ Package `{package}` installed successfully!",
                        message.chat.id,
                        status_msg.message_id
                    )
                else:
                    error_msg = result.stderr[:500] if result.stderr else "Unknown error"
                    bot.edit_message_text(
                        f"❌ Failed to install `{package}`:\n`{error_msg}`",
                        message.chat.id,
                        status_msg.message_id
                    )
            except subprocess.TimeoutExpired:
                bot.edit_message_text(
                    f"⚠️ Installation timeout for `{package}`",
                    message.chat.id,
                    status_msg.message_id
                )
            except Exception as e:
                bot.edit_message_text(
                    f"❌ Installation error: {e}",
                    message.chat.id,
                    status_msg.message_id
                )
    
    def install_package(self, package, user_id, message, pkg_type='python'):
        self.install_queue.put((package, user_id, message, pkg_type))

package_installer = PackageInstaller()

# --- GitHub Clone Feature (Enhanced) ---
def clone_github_repo(url, user_id, message):
    """Clone a GitHub repo into user's folder and detect main script"""
    user_folder = get_user_folder(user_id)
    repo_name = url.split('/')[-1].replace('.git', '')
    dest = os.path.join(user_folder, repo_name)
    
    if os.path.exists(dest):
        shutil.rmtree(dest)
    
    status_msg = bot.reply_to(message, "📥 Cloning repository...")
    try:
        result = subprocess.run(['git', 'clone', '--depth', '1', url, dest],
                               capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            bot.edit_message_text(
                f"❌ Clone failed:\n`{result.stderr[:500]}`",
                message.chat.id,
                status_msg.message_id,
                parse_mode='Markdown'
            )
            return
        
        bot.edit_message_text(
            "✅ Cloned! Scanning for main script...",
            message.chat.id,
            status_msg.message_id
        )
        
        # Detect main script
        main_script = None
        file_type = None
        
        # Check for common entry points
        for root, dirs, files in os.walk(dest):
            for file in files:
                if file.endswith('.py'):
                    if file in ['main.py', 'bot.py', 'app.py', 'run.py', 'server.py']:
                        main_script = os.path.relpath(os.path.join(root, file), dest)
                        file_type = 'py'
                        break
                elif file.endswith('.js'):
                    if file in ['index.js', 'main.js', 'app.js', 'server.js', 'bot.js']:
                        main_script = os.path.relpath(os.path.join(root, file), dest)
                        file_type = 'js'
                        break
            if main_script:
                break
        
        if not main_script:
            # Just take first .py or .js
            py_files = []
            js_files = []
            for root, dirs, files in os.walk(dest):
                for file in files:
                    if file.endswith('.py'):
                        py_files.append(os.path.relpath(os.path.join(root, file), dest))
                    elif file.endswith('.js'):
                        js_files.append(os.path.relpath(os.path.join(root, file), dest))
            if py_files:
                main_script = py_files[0]
                file_type = 'py'
            elif js_files:
                main_script = js_files[0]
                file_type = 'js'
        
        if not main_script:
            bot.edit_message_text(
                "⚠️ Cloned, but no Python or JavaScript script found.",
                message.chat.id,
                status_msg.message_id
            )
            return
        
        # Check for requirements.txt or package.json
        req_path = os.path.join(dest, 'requirements.txt')
        pkg_path = os.path.join(dest, 'package.json')
        
        if os.path.exists(req_path):
            bot.send_message(message.chat.id, "📦 Found requirements.txt - will install dependencies on start")
        
        if os.path.exists(pkg_path):
            bot.send_message(message.chat.id, "📦 Found package.json - will install dependencies on start")
        
        # Register in DB
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('''INSERT OR REPLACE INTO user_files 
                         (user_id, file_name, file_type, upload_date)
                         VALUES (?, ?, ?, ?)''',
                      (user_id, main_script, file_type, datetime.now().isoformat()))
            conn.commit()
            
        if user_id not in user_files:
            user_files[user_id] = []
        user_files[user_id].append((main_script, file_type))
        
        bot.edit_message_text(
            f"✅ Found main script: `{main_script}`\nUse file management to start.",
            message.chat.id,
            status_msg.message_id,
            parse_mode='Markdown'
        )
        
    except subprocess.TimeoutExpired:
        bot.edit_message_text("❌ Clone timed out.", message.chat.id, status_msg.message_id)
    except Exception as e:
        bot.edit_message_text(f"❌ Error: {e}", message.chat.id, status_msg.message_id)

# --- Keyboards (Enhanced) ---
USER_COMMAND_BUTTONS = [
    ["📢 Updates", "📤 Upload", "📂 My Files"],
    ["🌐 Clone GitHub", "📊 Stats", "💳 Premium"],
    ["📜 Logs", "📞 Support", "ℹ️ About"],
    ["🆘 Help", "🔧 Tools", "💾 Backup"]
]

ADMIN_COMMAND_BUTTONS = [
    ["📢 Updates", "📤 Upload", "📂 All Files"],
    ["🌐 Clone GitHub", "📊 Admin Stats", "💳 Manage Subs"],
    ["🔒 Lock Bot", "👑 Admin Panel", "📢 Broadcast"],
    ["📦 NPM Install", "🐍 PIP Install", "🔄 Restart"],
    ["📞 Support", "ℹ️ About", "🔧 System"],
    ["💾 Backups", "⏰ Schedule", "📊 Monitor"]
]

def create_main_menu_keyboard(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons_list = ADMIN_COMMAND_BUTTONS if user_id in admin_ids else USER_COMMAND_BUTTONS
    for row in buttons_list:
        markup.add(*[types.KeyboardButton(text) for text in row])
    return markup

# --- Database helpers for subscriptions ---
def save_subscription(user_id, expiry):
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('INSERT OR REPLACE INTO subscriptions (user_id, expiry) VALUES (?, ?)',
                 (user_id, expiry.isoformat()))
        conn.commit()
    user_subscriptions[user_id] = {'expiry': expiry}

def remove_subscription_db(user_id):
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('DELETE FROM subscriptions WHERE user_id = ?', (user_id,))
        conn.commit()
    if user_id in user_subscriptions:
        del user_subscriptions[user_id]

# --- Message Handlers (No slash commands) ---

@bot.message_handler(func=lambda m: m.text == "📢 Updates")
def handle_updates(message):
    bot.reply_to(message, f"📢 **Join our updates channel:**\n{UPDATE_CHANNEL}", parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "📤 Upload")
def handle_upload(message):
    bot.reply_to(message, "📤 **Send your file**\n\nSupported: `.py`, `.js`, `.zip`\nMax size: 100MB", parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text in ["📂 My Files", "📂 All Files"])
def handle_my_files(message):
    user_id = message.from_user.id
    is_admin = message.text == "📂 All Files" and user_id in admin_ids

    with db_manager.get_connection() as conn:
        c = conn.cursor()
        if is_admin:
            c.execute('SELECT user_id, file_name, file_type FROM user_files ORDER BY user_id')
            rows = c.fetchall()
            files = [(row[0], row[1], row[2]) for row in rows]
        else:
            c.execute('SELECT file_name, file_type FROM user_files WHERE user_id = ?', (user_id,))
            rows = c.fetchall()
            files = [(user_id, row[0], row[1]) for row in rows]
    
    if not files:
        bot.send_message(message.chat.id, "📂 **Your Files**\n\n✨ **No files uploaded yet**", parse_mode='Markdown')
        return
    
    # Group by user for admin view
    if is_admin:
        text = "📂 **All Files**\n\n"
        markup = types.InlineKeyboardMarkup(row_width=1)
        current_user = None
        for uid, fname, ftype in files:
            if uid != current_user:
                current_user = uid
                text += f"\n👤 User: `{uid}`\n"
            status = "🟢 Running" if is_bot_running(uid, fname) else "🔴 Stopped"
            icon = "🐍" if ftype == 'py' else "🟨"
            text += f"  {icon} `{fname}` - {status}\n"
            btn_text = f"{icon} {str(uid)[:6]}.../{fname[:15]}"
            markup.add(types.InlineKeyboardButton(btn_text, callback_data=f"manage_{uid}_{fname}"))
    else:
        text = f"📂 **Your Files** ({len(files)}/{get_user_file_limit(user_id)})\n\n"
        markup = types.InlineKeyboardMarkup(row_width=1)
        for uid, fname, ftype in files:
            status = "🟢 Running" if is_bot_running(uid, fname) else "🔴 Stopped"
            icon = "🐍" if ftype == 'py' else "🟨"
            text += f"{icon} `{fname}` - {status}\n"
            btn_text = f"{icon} {fname[:20]}"
            markup.add(types.InlineKeyboardButton(btn_text, callback_data=f"manage_{uid}_{fname}"))
    
    markup.add(types.InlineKeyboardButton("🔄 Refresh", callback_data="refresh_files"))
    bot.send_message(message.chat.id, text, reply_markup=markup)  # Changed from reply_to to send_message

@bot.callback_query_handler(func=lambda c: c.data == "refresh_files")
def refresh_files_callback(call):
    # Create proper message object with message_id
    class ProperMessage:
        def __init__(self, chat, from_user, text, message_id):
            self.chat = chat
            self.from_user = from_user
            self.text = text
            self.message_id = message_id
            self.id = message_id
            self.date = int(time.time())
    
    proper_msg = ProperMessage(
        chat=call.message.chat,
        from_user=call.from_user,
        text="📂 My Files",
        message_id=call.message.message_id + 1  # Increment to avoid conflict
    )
    handle_my_files(proper_msg)

@bot.callback_query_handler(func=lambda c: c.data.startswith("manage_"))
def manage_file_callback(call):
    parts = call.data.split('_')
    if len(parts) < 3:
        bot.answer_callback_query(call.id, "Invalid data")
        return
    
    user_id = int(parts[1])
    file_name = '_'.join(parts[2:])
    
    if call.from_user.id != user_id and call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "❌ Not your file!")
        return  
    
    file_type = None
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT file_type FROM user_files WHERE user_id = ? AND file_name = ?', (user_id, file_name))
        row = c.fetchone()
        if row:
            file_type = row[0]
    
    if not file_type:
        bot.answer_callback_query(call.id, "File not found.")
        return
    
    running = is_bot_running(user_id, file_name)
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Row 1: Start/Stop
    if running:
        markup.add(types.InlineKeyboardButton("🛑 Stop", callback_data=f"stop_{user_id}_{file_name}"))
    else:
        markup.add(types.InlineKeyboardButton("▶️ Start", callback_data=f"start_{user_id}_{file_name}"))
    
    # Row 2: Logs and Info
    markup.add(
        types.InlineKeyboardButton("📜 Logs", callback_data=f"logs_{user_id}_{file_name}"),
        types.InlineKeyboardButton("ℹ️ Info", callback_data=f"info_{user_id}_{file_name}")
    )
    
    # Row 3: Backup and Download
    markup.add(
        types.InlineKeyboardButton("💾 Backup", callback_data=f"backup_{user_id}_{file_name}"),
        types.InlineKeyboardButton("📥 Download", callback_data=f"download_{user_id}_{file_name}")
    )
    
    # Row 4: Schedule and Delete
    if CRONITER_AVAILABLE:
        markup.add(
            types.InlineKeyboardButton("⏰ Schedule", callback_data=f"schedule_{user_id}_{file_name}"),
            types.InlineKeyboardButton("🗑️ Delete", callback_data=f"delete_{user_id}_{file_name}")
        )
    else:
        markup.add(types.InlineKeyboardButton("🗑️ Delete", callback_data=f"delete_{user_id}_{file_name}"))
    
    # Row 5: Back
    markup.add(types.InlineKeyboardButton("🔙 Back", callback_data="back_to_files"))
    
    # Get run count
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT run_count, upload_date FROM user_files WHERE user_id = ? AND file_name = ?',
                 (user_id, file_name))
        row = c.fetchone()
        run_count = row[0] if row else 0
        upload_date = row[1] if row else "Unknown"
    
    status = "🟢 Running" if running else "🔴 Stopped"
    text = f"""
⚙️ **Manage File**

📁 **File:** `{file_name}`
🔰 **Type:** {file_type.upper()}
🔰 **Status:** {status}
📊 **Runs:** {run_count}
📅 **Uploaded:** {upload_date[:10] if upload_date != "Unknown" else "Unknown"}

**Actions:**
• Start/Stop the script
• View logs and info
• Create backup/download
• Schedule auto-run
• Delete file
    """
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                         parse_mode='Markdown', reply_markup=markup)

@bot.callback_query_handler(func=lambda c: c.data == "back_to_files")
def back_to_files_callback(call):
    # Create a proper message object
    class ProperMessage:
        def __init__(self, chat, from_user, text, message_id):
            self.chat = chat
            self.from_user = from_user
            self.text = text
            self.message_id = message_id
            self.id = message_id
            self.date = int(time.time())
    
    proper_msg = ProperMessage(
        chat=call.message.chat,
        from_user=call.from_user,
        text="📂 My Files",
        message_id=call.message.message_id + 1  # Increment to avoid conflict
    )
    handle_my_files(proper_msg)

@bot.callback_query_handler(func=lambda c: c.data.startswith("start_"))
def start_script_callback(call):
    parts = call.data.split('_')
    if len(parts) < 3:
        bot.answer_callback_query(call.id, "Invalid data")
        return
    
    user_id = int(parts[1])
    file_name = '_'.join(parts[2:])
    
    if call.from_user.id != user_id and call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "❌ Not your file!")
        return
    
    if is_bot_running(user_id, file_name):
        bot.answer_callback_query(call.id, "Already running.")
        return
    
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT file_type FROM user_files WHERE user_id = ? AND file_name = ?', (user_id, file_name))
        row = c.fetchone()
        if not row:
            bot.answer_callback_query(call.id, "File not found.")
            return
        file_type = row[0]
    
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    
    # Run in background
    threading.Thread(target=script_runner.run_script,
                    args=(file_path, user_id, user_folder, file_name, call.message, file_type)).start()
    
    bot.answer_callback_query(call.id, "Starting...")
    time.sleep(1)
    manage_file_callback(call)  # Refresh

@bot.callback_query_handler(func=lambda c: c.data.startswith("stop_"))
def stop_script_callback(call):
    parts = call.data.split('_')
    if len(parts) < 3:
        bot.answer_callback_query(call.id, "Invalid data")
        return
    
    user_id = int(parts[1])
    file_name = '_'.join(parts[2:])
    
    if call.from_user.id != user_id and call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "❌ Not your file!")
        return
    
    script_key = f"{user_id}_{file_name}"
    if script_key in bot_scripts:
        kill_process_tree(bot_scripts[script_key])
        if script_key in bot_scripts:
            del bot_scripts[script_key]
        bot.answer_callback_query(call.id, "Stopped.")
    else:
        bot.answer_callback_query(call.id, "Not running.")
    
    time.sleep(1)
    manage_file_callback(call)  # Refresh

@bot.callback_query_handler(func=lambda c: c.data.startswith("logs_"))
def logs_script_callback(call):
    parts = call.data.split('_')
    if len(parts) < 3:
        bot.answer_callback_query(call.id, "Invalid data")
        return
    
    user_id = int(parts[1])
    file_name = '_'.join(parts[2:])
    
    if call.from_user.id != user_id and call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "❌ Not your file!")
        return
    
    user_folder = get_user_folder(user_id)
    log_files = [f for f in os.listdir(user_folder)
                if f.startswith(os.path.splitext(file_name)[0]) and f.endswith('.log')]
    
    if not log_files:
        bot.answer_callback_query(call.id, "No logs found.")
        return
    
    # Show list of logs
    markup = types.InlineKeyboardMarkup(row_width=1)
    for log in sorted(log_files, reverse=True)[:5]:  # Last 5 logs
        log_time = os.path.getmtime(os.path.join(user_folder, log))
        time_str = datetime.fromtimestamp(log_time).strftime("%Y-%m-%d %H:%M")
        markup.add(types.InlineKeyboardButton(
            f"📄 {time_str}",
            callback_data=f"viewlog_{user_id}_{file_name}_{log}"
        ))
    markup.add(types.InlineKeyboardButton("🔙 Back", callback_data=f"manage_{user_id}_{file_name}"))
    
    bot.edit_message_text(
        f"📜 **Logs for `{file_name}`**\nSelect a log to view:",
        call.message.chat.id,
        call.message.message_id,
        parse_mode='Markdown',
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda c: c.data.startswith("viewlog_"))
def view_log_callback(call):
    parts = call.data.split('_')
    if len(parts) < 4:
        bot.answer_callback_query(call.id, "Invalid data")
        return
    
    user_id = int(parts[1])
    file_name = parts[2]
    log_file = '_'.join(parts[3:])
    
    user_folder = get_user_folder(user_id)
    log_path = os.path.join(user_folder, log_file)
    
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()[-3500:]
        
        # Split if too long
        if len(content) > 3500:
            content = content[-3500:]
        
        bot.send_message(
            call.message.chat.id,
            f"📜 **Logs for `{file_name}`:**\n```\n{content}\n```",
            parse_mode='Markdown'
        )
    except Exception as e:
        bot.send_message(call.message.chat.id, f"❌ Error reading logs: {e}")
    
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda c: c.data.startswith("info_"))
def info_script_callback(call):
    parts = call.data.split('_')
    if len(parts) < 3:
        bot.answer_callback_query(call.id, "Invalid data")
        return
    
    user_id = int(parts[1])
    file_name = '_'.join(parts[2:])
    
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    
    if not os.path.exists(file_path):
        bot.answer_callback_query(call.id, "File not found")
        return
    
    file_size = os.path.getsize(file_path)
    modified = datetime.fromtimestamp(os.path.getmtime(file_path))
    
    # Get run history
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('''SELECT COUNT(*), MAX(start_time) FROM script_runs 
                     WHERE user_id = ? AND file_name = ?''', (user_id, file_name))
        row = c.fetchone()
        total_runs = row[0] if row else 0
        last_run = row[1] if row else None
        
        c.execute('''SELECT start_time, end_time, status, cpu_usage, memory_usage 
                     FROM script_runs WHERE user_id = ? AND file_name = ? 
                     ORDER BY start_time DESC LIMIT 5''', (user_id, file_name))
        recent_runs = c.fetchall()
    
    text = f"""
ℹ️ **File Info: `{file_name}`**

📁 **Size:** {format_size(file_size)}
📅 **Modified:** {modified.strftime('%Y-%m-%d %H:%M:%S')}
📊 **Total Runs:** {total_runs}
🕐 **Last Run:** {last_run[:16] if last_run else 'Never'}

**Recent Runs:**
"""
    for start, end, status, cpu, mem in recent_runs:
        duration = "?"
        if end:
            try:
                start_dt = datetime.fromisoformat(start)
                end_dt = datetime.fromisoformat(end)
                duration = str(timedelta(seconds=int((end_dt - start_dt).total_seconds())))
            except:
                pass
        text += f"• {start[:16]} - {status} ({duration})\n"
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 Back", callback_data=f"manage_{user_id}_{file_name}"))
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                         parse_mode='Markdown', reply_markup=markup)

@bot.callback_query_handler(func=lambda c: c.data.startswith("backup_"))
def backup_script_callback(call):
    parts = call.data.split('_')
    if len(parts) < 3:
        bot.answer_callback_query(call.id, "Invalid data")
        return
    
    user_id = int(parts[1])
    file_name = '_'.join(parts[2:])
    
    backup_path = create_backup(user_id, file_name)
    if backup_path:
        bot.answer_callback_query(call.id, "✅ Backup created!")
    else:
        bot.answer_callback_query(call.id, "❌ Backup failed")
    
    manage_file_callback(call)

@bot.callback_query_handler(func=lambda c: c.data.startswith("download_"))
def download_script_callback(call):
    parts = call.data.split('_')
    if len(parts) < 3:
        bot.answer_callback_query(call.id, "Invalid data")
        return
    
    user_id = int(parts[1])
    file_name = '_'.join(parts[2:])
    
    user_folder = get_user_folder(user_id)
    file_path = os.path.join(user_folder, file_name)
    
    if os.path.exists(file_path):
        try:
            with open(file_path, 'rb') as f:
                bot.send_document(call.message.chat.id, f, caption=f"📥 `{file_name}`", parse_mode='Markdown')
            bot.answer_callback_query(call.id, "✅ File sent")
        except Exception as e:
            bot.answer_callback_query(call.id, f"❌ Error: {e}")
    else:
        bot.answer_callback_query(call.id, "❌ File not found")

@bot.callback_query_handler(func=lambda c: c.data.startswith("schedule_") and CRONITER_AVAILABLE)
def schedule_script_callback(call):
    parts = call.data.split('_')
    if len(parts) < 3:
        bot.answer_callback_query(call.id, "Invalid data")
        return
    
    user_id = int(parts[1])
    file_name = '_'.join(parts[2:])
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("⏰ Every hour", callback_data=f"cron_{user_id}_{file_name}_0 * * * *"),
        types.InlineKeyboardButton("⏰ Every day", callback_data=f"cron_{user_id}_{file_name}_0 0 * * *"),
        types.InlineKeyboardButton("⏰ Every week", callback_data=f"cron_{user_id}_{file_name}_0 0 * * 0"),
        types.InlineKeyboardButton("⏰ Every month", callback_data=f"cron_{user_id}_{file_name}_0 0 1 * *"),
        types.InlineKeyboardButton("🔙 Back", callback_data=f"manage_{user_id}_{file_name}")
    )
    
    bot.edit_message_text(
        f"⏰ **Schedule for `{file_name}`**\nSelect frequency:",
        call.message.chat.id,
        call.message.message_id,
        parse_mode='Markdown',
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda c: c.data.startswith("cron_") and CRONITER_AVAILABLE)
def set_cron_callback(call):
    parts = call.data.split('_')
    if len(parts) < 4:
        bot.answer_callback_query(call.id, "Invalid data")
        return
    
    user_id = int(parts[1])
    file_name = parts[2]
    cron_pattern = '_'.join(parts[3:])
    
    next_run = datetime.now() + timedelta(minutes=1)  # Temporary
    
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('''INSERT INTO scheduled_tasks (user_id, file_name, cron_pattern, next_run)
                     VALUES (?, ?, ?, ?)''',
                  (user_id, file_name, cron_pattern, next_run.isoformat()))
        conn.commit()
    
    bot.answer_callback_query(call.id, "✅ Schedule set!")
    manage_file_callback(call)

@bot.callback_query_handler(func=lambda c: c.data.startswith("delete_"))
def delete_script_callback(call):
    parts = call.data.split('_')
    if len(parts) < 3:
        bot.answer_callback_query(call.id, "Invalid data")
        return
    
    user_id = int(parts[1])
    file_name = '_'.join(parts[2:])
    
    if call.from_user.id != user_id and call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, "❌ Not your file!")
        return
    
    # Confirm deletion
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("✅ Yes", callback_data=f"confirm_delete_{user_id}_{file_name}"),
        types.InlineKeyboardButton("❌ No", callback_data=f"manage_{user_id}_{file_name}")
    )
    
    bot.edit_message_text(
        f"⚠️ **Confirm Delete**\n\nAre you sure you want to delete `{file_name}`?",
        call.message.chat.id,
        call.message.message_id,
        parse_mode='Markdown',
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda c: c.data.startswith("confirm_delete_"))
def confirm_delete_callback(call):
    parts = call.data.split('_')
    if len(parts) < 4:
        bot.answer_callback_query(call.id, "Invalid data")
        return
    
    user_id = int(parts[2])
    file_name = '_'.join(parts[3:])
    
    script_key = f"{user_id}_{file_name}"
    if script_key in bot_scripts:
        kill_process_tree(bot_scripts[script_key])
        if script_key in bot_scripts:
            del bot_scripts[script_key]
    
    FileManager.delete_file(user_id, file_name)
    bot.answer_callback_query(call.id, "✅ Deleted.")
    
    # Go back to files list
    # Create a proper callback for back_to_files
    class FakeCall:
        def __init__(self, message, from_user):
            self.message = message
            self.from_user = from_user
            self.data = "back_to_files"
            self.id = call.id
    
    fake_call = FakeCall(call.message, call.from_user)
    back_to_files_callback(fake_call)

@bot.message_handler(func=lambda m: m.text == "🌐 Clone GitHub")
def handle_clone_github(message):
    msg = bot.reply_to(
        message,
        "📥 **Send the GitHub repository URL**\nExample: `https://github.com/user/repo`",
        parse_mode='Markdown'
    )
    bot.register_next_step_handler(msg, process_github_clone)

def process_github_clone(message):
    url = message.text.strip()
    if not url.startswith(('https://github.com/', 'http://github.com/')):
        bot.reply_to(message, "❌ Invalid GitHub URL.")
        return
    user_id = message.from_user.id
    threading.Thread(target=clone_github_repo, args=(url, user_id, message)).start()

@bot.message_handler(func=lambda m: m.text == "📊 Stats")
def handle_stats(message):
    user_id = message.from_user.id
    system_stats = get_system_stats()
    total_users = len(active_users)
    
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM user_files')
        total_files = c.fetchone()[0]
        
        c.execute('SELECT COUNT(*) FROM script_runs WHERE status = "running"')
        running_result = c.fetchone()
        running_scripts_db = running_result[0] if running_result else 0  # Fixed here
    
    running_scripts = len(bot_scripts)
    user_scripts = sum(1 for key in bot_scripts if key.startswith(str(user_id)))
    
    uptime_str = format_time(time.time() - start_time)
    
    # Network stats
    try:
        net = psutil.net_io_counters()
        sent_mb = net.bytes_sent / (1024*1024)
        recv_mb = net.bytes_recv / (1024*1024)
        network_text = f"• Sent: {sent_mb:.1f} MB\n• Recv: {recv_mb:.1f} MB"
    except:
        network_text = "• Network: Permission denied"
    
    stats_text = f"""
📊 **BOT STATISTICS**
━━━━━━━━━━━━━━━━━━━━━
👥 **Users:** {total_users:,}
📁 **Files:** {total_files:,}
🤖 **Active Scripts:** {running_scripts} / {running_scripts_db}
⏱️ **Uptime:** {uptime_str}

📌 **Your Stats:**
• Files: {get_user_file_count(user_id)}
• Running: {user_scripts}

💻 **System:**
• CPU: {system_stats.get('cpu', 0)}%
• RAM: {system_stats.get('memory_percent', 0)}%
• Disk: {system_stats.get('disk_percent', 0)}%
{network_text}
"""
    bot.reply_to(message, stats_text, parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "📊 Admin Stats")
def handle_admin_stats(message):
    if message.from_user.id in admin_ids:
        handle_stats(message)

@bot.message_handler(func=lambda m: m.text == "📊 Monitor" and m.from_user.id in admin_ids)
def handle_monitor(message):
    """Show detailed monitoring"""
    text = "📊 **Process Monitor**\n\n"
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    for key, info in list(bot_scripts.items()):
        try:
            proc = psutil.Process(info['pid'])
            cpu = proc.cpu_percent(interval=0.1)
            mem = proc.memory_percent()
            uptime = str(timedelta(seconds=int(time.time() - info['start_time'].timestamp())))
            
            status = "🟢" if proc.is_running() else "🔴"
            text += f"{status} `{info['file_name']}` (PID: {info['pid']})\n"
            text += f"   CPU: {cpu:.1f}% | MEM: {mem:.1f}% | Uptime: {uptime}\n"
            
            btn_text = f"🛑 Stop {info['file_name'][:15]}"
            markup.add(types.InlineKeyboardButton(
                btn_text,
                callback_data=f"stop_{info['user_id']}_{info['file_name']}"
            ))
        except:
            pass
    
    if not bot_scripts:
        text += "No running processes.\n"
    
    markup.add(types.InlineKeyboardButton("🔄 Refresh", callback_data="refresh_monitor"))
    bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

@bot.callback_query_handler(func=lambda c: c.data == "refresh_monitor")
def refresh_monitor_callback(call):
    handle_monitor(call.message)

@bot.message_handler(func=lambda m: m.text == "💳 Premium")
def handle_premium_info(message):
    text = """
💎 **PREMIUM SUBSCRIPTION**
━━━━━━━━━━━━━━━━━━━━━
✨ **Premium Benefits:**
📁 **More Storage:** 15 files (Free: 5)
🚀 **Priority Hosting**
💾 **Auto Backups**
⏰ **Scheduled Runs**
💰 **Price:** Contact Owner

To subscribe, contact @Zinko158
"""
    bot.reply_to(message, text, parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "💳 Manage Subs")
def handle_manage_subs(message):
    if message.from_user.id in admin_ids:
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton("➕ Add Premium", callback_data="sub_add"),
            types.InlineKeyboardButton("➖ Remove Premium", callback_data="sub_remove"),
            types.InlineKeyboardButton("📋 List Premium", callback_data="sub_list"),
            types.InlineKeyboardButton("⏱️ Extend", callback_data="sub_extend")
        )
        bot.send_message(message.chat.id, "👑 **Manage Subscriptions**", reply_markup=markup)

@bot.callback_query_handler(func=lambda c: c.data == "sub_add" and c.from_user.id in admin_ids)
def sub_add_callback(call):
    msg = bot.send_message(call.message.chat.id, "Send user ID to add premium (default 30 days):")
    bot.register_next_step_handler(msg, process_sub_add)

def process_sub_add(message):
    try:
        user_id = int(message.text.strip())
        expiry = datetime.now() + timedelta(days=30)
        save_subscription(user_id, expiry)
        bot.reply_to(
            message,
            f"✅ Added premium for user `{user_id}` until {expiry.strftime('%Y-%m-%d')}",
            parse_mode='Markdown'
        )
    except:
        bot.reply_to(message, "❌ Invalid user ID.")

@bot.callback_query_handler(func=lambda c: c.data == "sub_remove" and c.from_user.id in admin_ids)
def sub_remove_callback(call):
    msg = bot.send_message(call.message.chat.id, "Send user ID to remove premium:")
    bot.register_next_step_handler(msg, process_sub_remove)

def process_sub_remove(message):
    try:
        user_id = int(message.text.strip())
        remove_subscription_db(user_id)
        bot.reply_to(message, f"✅ Removed premium for user `{user_id}`", parse_mode='Markdown')
    except:
        bot.reply_to(message, "❌ Invalid user ID.")

@bot.callback_query_handler(func=lambda c: c.data == "sub_extend" and c.from_user.id in admin_ids)
def sub_extend_callback(call):
    msg = bot.send_message(call.message.chat.id, "Send: `user_id days` to extend (e.g., `12345 60`):")
    bot.register_next_step_handler(msg, process_sub_extend)

def process_sub_extend(message):
    try:
        parts = message.text.strip().split()
        if len(parts) != 2:
            raise ValueError
        user_id = int(parts[0])
        days = int(parts[1])
        
        if user_id in user_subscriptions:
            current_expiry = user_subscriptions[user_id]['expiry']
            new_expiry = current_expiry + timedelta(days=days)
        else:
            new_expiry = datetime.now() + timedelta(days=days)
        
        save_subscription(user_id, new_expiry)
        bot.reply_to(
            message,
            f"✅ Extended user `{user_id}` until {new_expiry.strftime('%Y-%m-%d')}",
            parse_mode='Markdown'
        )
    except:
        bot.reply_to(message, "❌ Invalid format. Use: `user_id days`")

@bot.callback_query_handler(func=lambda c: c.data == "sub_list" and c.from_user.id in admin_ids)
def sub_list_callback(call):
    if not user_subscriptions:
        bot.send_message(call.message.chat.id, "No premium users.")
        return
    text = "📋 **Premium Users:**\n"
    for uid, data in user_subscriptions.items():
        expiry = data['expiry'].strftime('%Y-%m-%d')
        days_left = (data['expiry'] - datetime.now()).days
        text += f"• `{uid}` until {expiry} ({days_left} days left)\n"
    bot.send_message(call.message.chat.id, text, parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "📜 Logs")
def handle_my_logs(message):
    user_id = message.from_user.id
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT file_name FROM user_files WHERE user_id = ?', (user_id,))
        files = [row[0] for row in c.fetchall()]
    
    if not files:
        bot.reply_to(message, "No files.")
        return
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    for fname in files:
        markup.add(types.InlineKeyboardButton(f"📜 {fname}", callback_data=f"logs_{user_id}_{fname}"))
    bot.send_message(message.chat.id, "Select script to view logs:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "💾 Backup")
def handle_backup(message):
    user_id = message.from_user.id
    backups = list_backups(user_id)
    
    if not backups:
        bot.reply_to(message, "No backups found.")
        return
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    for bid, fname, bdate in backups[:10]:  # Last 10
        date_str = datetime.fromisoformat(bdate).strftime('%Y-%m-%d %H:%M')
        markup.add(types.InlineKeyboardButton(
            f"💾 {fname} ({date_str})",
            callback_data=f"restore_{bid}"
        ))
    
    bot.send_message(message.chat.id, "Select backup to restore:", reply_markup=markup)

@bot.callback_query_handler(func=lambda c: c.data.startswith("restore_"))
def restore_backup_callback(call):
    backup_id = int(call.data.split('_')[1])
    
    result = restore_backup(backup_id)
    if result:
        bot.answer_callback_query(call.id, f"✅ Restored: {result}")
    else:
        bot.answer_callback_query(call.id, "❌ Restore failed")

@bot.message_handler(func=lambda m: m.text == "📞 Support")
def handle_support(message):
    bot.reply_to(message, f"📞 **Contact support:** @{YOUR_USERNAME.replace('@', '')}", parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "ℹ️ About")
def handle_about(message):
    text = f"""
ℹ️ **MARCO FILE HOST ULTIMATE v5.0**
━━━━━━━━━━━━━━━━━━━━━
🤖 **Version:** 5.0 (Ultimate)
👑 **Owner:** @Zinko158
📢 **Updates:** {UPDATE_CHANNEL}

✨ **Features:**
• Zero slash commands
• Full inline management
• Auto dependency install
• GitHub clone
• Resource monitoring
• Auto backups
• Scheduled tasks
• Multi-script support
"""
    bot.reply_to(message, text, parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "🆘 Help")
def handle_help(message):
    text = """
🆘 **HELP MENU**
━━━━━━━━━━━━━━━━━━━━━
📤 **Upload Files:** Send .py, .js, or .zip
🌐 **Clone GitHub:** Use button, paste URL
📂 **My Files:** Manage scripts (inline)
📊 **Stats:** View bot stats
💳 **Premium:** Subscription info
📜 **Logs:** View script logs
💾 **Backup:** Restore previous versions
━━━━━━━━━━━━━━━━━━━━━
"""
    bot.reply_to(message, text, parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "🔧 Tools")
def handle_tools(message):
    user_id = message.from_user.id
    is_admin = user_id in admin_ids
    
    text = """
🔧 **Tools Menu**
━━━━━━━━━━━━━━━━━━━━━
"""
    if is_admin:
        text += """
Admin Tools:
• 📦 Install Python packages
• 📦 Install Node packages
• 🔒 Lock/unlock bot
• 📢 Broadcast messages
• 🔄 Restart bot
• 📊 Monitor processes
"""
    else:
        text += """
User Tools:
• View your file stats
• Check system status
• Get support
"""
    bot.reply_to(message, text, parse_mode='Markdown')

# --- Admin Handlers ---
@bot.message_handler(func=lambda m: m.text == "📦 NPM Install" and m.from_user.id in admin_ids)
def handle_npm_install(message):
    msg = bot.reply_to(message, "📦 Send package name to install via npm:")
    bot.register_next_step_handler(msg, lambda m: process_package_install(m, 'node'))

@bot.message_handler(func=lambda m: m.text == "🐍 PIP Install" and m.from_user.id in admin_ids)
def handle_pip_install(message):
    msg = bot.reply_to(message, "🐍 Send package name to install via pip:")
    bot.register_next_step_handler(msg, lambda m: process_package_install(m, 'python'))

def process_package_install(message, pkg_type):
    package = message.text.strip()
    user_id = message.from_user.id
    package_installer.install_package(package, user_id, message, pkg_type)

@bot.message_handler(func=lambda m: m.text == "🔒 Lock Bot" and m.from_user.id in admin_ids)
def handle_lock_bot(message):
    global bot_locked
    bot_locked = not bot_locked
    status = "locked" if bot_locked else "unlocked"
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('UPDATE settings SET value = ? WHERE key = ?', (str(bot_locked).lower(), 'bot_locked'))
        conn.commit()
    bot.reply_to(message, f"🔒 **Bot has been {status}.**", parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "👑 Admin Panel" and m.from_user.id in admin_ids)
def handle_admin_panel(message):
    text = "👑 **ADMIN PANEL**\nUse the buttons above for admin functions."
    bot.reply_to(message, text, parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "📢 Broadcast" and m.from_user.id in admin_ids)
def handle_broadcast(message):
    msg = bot.reply_to(message, "📢 **Send the message to broadcast:**", parse_mode='Markdown')
    bot.register_next_step_handler(msg, process_broadcast)

def process_broadcast(message):
    if message.from_user.id not in admin_ids:
        return
    text = message.text or "Broadcast"
    success = 0
    fail = 0
    
    status_msg = bot.reply_to(message, "📢 Broadcasting...")
    
    for uid in list(active_users):
        try:
            bot.send_message(uid, f"📢 **Broadcast**\n\n{text}", parse_mode='Markdown')
            success += 1
        except:
            fail += 1
        time.sleep(0.05)
    
    bot.edit_message_text(
        f"✅ Sent to {success} users.\n❌ Failed: {fail}",
        message.chat.id,
        status_msg.message_id
    )

@bot.message_handler(func=lambda m: m.text == "🔄 Restart" and m.from_user.id in admin_ids)
def handle_restart_bot(message):
    bot.reply_to(message, "🔄 **Restarting bot...**", parse_mode='Markdown')
    cleanup()
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.message_handler(func=lambda m: m.text == "🔧 System" and m.from_user.id in admin_ids)
def handle_system_stats(message):
    stats = get_system_stats()
    text = f"""
🔧 **SYSTEM STATS**
CPU: {stats.get('cpu', 0)}%
RAM: {stats.get('memory_percent', 0)}%
Disk: {stats.get('disk_percent', 0)}%
Processes: {stats.get('processes', 0)}
"""
    bot.reply_to(message, text, parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "⏰ Schedule" and m.from_user.id in admin_ids and CRONITER_AVAILABLE)
def handle_schedule_list(message):
    """List all scheduled tasks"""
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('''SELECT id, user_id, file_name, cron_pattern, next_run, enabled 
                     FROM scheduled_tasks ORDER BY next_run''')
        tasks = c.fetchall()
    
    if not tasks:
        bot.reply_to(message, "No scheduled tasks.")
        return
    
    text = "⏰ **Scheduled Tasks**\n\n"
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    for tid, uid, fname, cron, next_run, enabled in tasks:
        status = "🟢" if enabled else "🔴"
        next_dt = datetime.fromisoformat(next_run).strftime('%Y-%m-%d %H:%M')
        text += f"{status} `{fname}` (User: {uid})\n   Next: {next_dt}\n"
        markup.add(types.InlineKeyboardButton(
            f"{'Disable' if enabled else 'Enable'} {fname[:15]}",
            callback_data=f"toggle_task_{tid}"
        ))
    
    bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=markup)

@bot.callback_query_handler(func=lambda c: c.data.startswith("toggle_task_") and CRONITER_AVAILABLE)
def toggle_task_callback(call):
    task_id = int(call.data.split('_')[2])
    
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('SELECT enabled FROM scheduled_tasks WHERE id = ?', (task_id,))
        row = c.fetchone()
        if row:
            enabled = 0 if row[0] else 1
            c.execute('UPDATE scheduled_tasks SET enabled = ? WHERE id = ?', (enabled, task_id))
            conn.commit()
            bot.answer_callback_query(call.id, "✅ Toggled")
    
    handle_schedule_list(call.message)

# --- File Upload Handler ---
@bot.message_handler(content_types=['document'])
def handle_file_upload(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    doc = message.document
    
    if bot_locked and user_id not in admin_ids:
        bot.reply_to(message, "⚠️ **Bot is locked**")
        return
    
    file_limit = get_user_file_limit(user_id)
    current_files = get_user_file_count(user_id)
    
    if current_files >= file_limit:
        bot.reply_to(
            message,
            f"⚠️ **Limit Reached!**\nUsed: {current_files}/{file_limit}",
            parse_mode='Markdown'
        )
        return
    
    file_name = doc.file_name
    file_ext = os.path.splitext(file_name)[1].lower()
    
    if file_ext not in ['.py', '.js', '.zip', '.json', '.txt', '.yml', '.yaml']:
        bot.reply_to(message, "❌ **Unsupported file type**", parse_mode='Markdown')
        return
    
    if doc.file_size > MAX_SCRIPT_SIZE:
        bot.reply_to(
            message,
            f"❌ **File too large (Max {MAX_SCRIPT_SIZE/1024/1024}MB)**",
            parse_mode='Markdown'
        )
        return
    
    status_msg = bot.reply_to(message, f"📥 **Downloading** `{file_name}`...", parse_mode='Markdown')
    
    try:
        file_info = bot.get_file(doc.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        user_folder = get_user_folder(user_id)
        
        if file_ext == '.zip':
            process_zip_file(downloaded_file, file_name, user_id, user_folder, message, status_msg)
        else:
            file_path, file_size = FileManager.save_file(user_id, downloaded_file, file_name)
            bot.edit_message_text(
                f"✅ **Saved:** `{file_name}`\n🚀 **Starting...**",
                chat_id,
                status_msg.message_id,
                parse_mode='Markdown'
            )
            
            if file_ext == '.py':
                threading.Thread(target=run_script, args=(file_path, user_id, user_folder, file_name, message)).start()
            elif file_ext == '.js':
                threading.Thread(target=run_js_script, args=(file_path, user_id, user_folder, file_name, message)).start()
            else:
                bot.edit_message_text(
                    f"✅ **Saved:** `{file_name}`",
                    chat_id,
                    status_msg.message_id,
                    parse_mode='Markdown'
                )
                
    except Exception as e:
        logger.error(f"Upload error: {e}")
        bot.edit_message_text(
            f"❌ **Error:** `{str(e)[:100]}`",
            chat_id,
            status_msg.message_id,
            parse_mode='Markdown'
        )

def process_zip_file(downloaded_content, zip_name, user_id, user_folder, original_message, status_msg):
    temp_dir = tempfile.mkdtemp(prefix=f"marco_{user_id}_")
    try:
        zip_path = os.path.join(temp_dir, zip_name)
        with open(zip_path, 'wb') as f:
            f.write(downloaded_content)
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            bad_file = zip_ref.testzip()
            if bad_file:
                raise zipfile.BadZipFile(f"Corrupted: {bad_file}")
            zip_ref.extractall(temp_dir)
        
        # Analyze
        py_files = []
        js_files = []
        main_script = None
        
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), temp_dir)
                if file.endswith('.py'):
                    py_files.append(rel_path)
                elif file.endswith('.js'):
                    js_files.append(rel_path)
        
        if py_files:
            # Priority to main.py, bot.py
            for name in ['main.py', 'bot.py', 'app.py', 'run.py']:
                found = next((f for f in py_files if f.endswith(name)), None)
                if found:
                    main_script = found
                    break
            if not main_script:
                main_script = py_files[0]
        elif js_files:
            for name in ['index.js', 'main.js', 'app.js', 'server.js']:
                found = next((f for f in js_files if f.endswith(name)), None)
                if found:
                    main_script = found
                    break
            if not main_script:
                main_script = js_files[0]
        
        if not main_script:
            bot.edit_message_text(
                "❌ **No script found in ZIP**",
                original_message.chat.id,
                status_msg.message_id,
                parse_mode='Markdown'
            )
            return

        # Copy files
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), temp_dir)
                dest_path = os.path.join(user_folder, rel_path)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy2(os.path.join(root, file), dest_path)
        
        main_path = os.path.join(user_folder, main_script)
        file_ext = os.path.splitext(main_script)[1].lower()
        
        # Save to DB
        with db_manager.get_connection() as conn:
            c = conn.cursor()
            c.execute('''INSERT OR REPLACE INTO user_files 
                         (user_id, file_name, file_type, upload_date)
                         VALUES (?, ?, ?, ?)''',
                      (user_id, main_script, file_ext[1:], datetime.now().isoformat()))
            conn.commit()
            
        if user_id not in user_files:
            user_files[user_id] = []
        user_files[user_id].append((main_script, file_ext[1:]))
        
        bot.edit_message_text(
            f"✅ **ZIP Extracted**\n🚀 **Starting:** `{main_script}`",
            original_message.chat.id,
            status_msg.message_id,
            parse_mode='Markdown'
        )
        
        if file_ext == '.py':
            threading.Thread(target=run_script, args=(main_path, user_id, user_folder, main_script, original_message)).start()
        else:
            threading.Thread(target=run_js_script, args=(main_path, user_id, user_folder, main_script, original_message)).start()
        
    except Exception as e:
        logger.error(f"ZIP Error: {e}")
        bot.edit_message_text(
            f"❌ **ZIP Error:** `{str(e)[:100]}`",
            original_message.chat.id,
            status_msg.message_id,
            parse_mode='Markdown'
        )
    finally:
        try:
            shutil.rmtree(temp_dir)
        except:
            pass

# --- Welcome Handler (No slash commands) ---
@bot.message_handler(func=lambda m: True)
def welcome_handler(message):
    """Handle any text message - show main menu"""
    user_id = message.from_user.id
    chat_id = message.chat.id
    user_name = message.from_user.first_name or "User"
    user_username = message.from_user.username
    
    if bot_locked and user_id not in admin_ids:
        bot.send_message(
            chat_id,
            "⚠️ **Bot is currently under maintenance**\nPlease try again later.",
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
                      (user_id, user_username, user_name, datetime.now().isoformat(), datetime.now().isoformat()))
            conn.commit()
        
        # Notify owner
        try:
            notification = (f"🎉 **New User Joined!**\n\n"
                           f"👤 **Name:** {user_name}\n"
                           f"🆔 **ID:** `{user_id}`\n"
                           f"✳️ **Username:** @{user_username or 'N/A'}\n"
                           f"📅 **Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            bot.send_message(OWNER_ID, notification, parse_mode='Markdown')
        except Exception as e:
            logger.error(f"Failed to notify owner: {e}")
    
    # Update last seen
    with db_manager.get_connection() as conn:
        c = conn.cursor()
        c.execute('UPDATE active_users SET last_seen = ? WHERE user_id = ?',
                 (datetime.now().isoformat(), user_id))
        conn.commit()
    
    file_limit = get_user_file_limit(user_id)
    current_files = get_user_file_count(user_id)
    limit_display = "∞" if file_limit == float('inf') else str(file_limit)
    
    # Determine user status
    if user_id == OWNER_ID:
        user_status = "👑 OWNER"
        status_emoji = "👑"
    elif user_id in admin_ids:
        user_status = "🛡️ ADMIN"
        status_emoji = "🛡️"
    elif user_id in user_subscriptions:
        expiry = user_subscriptions[user_id].get('expiry')
        if expiry and expiry > datetime.now():
            days_left = (expiry - datetime.now()).days
            user_status = f"⭐ PREMIUM ({days_left} days)"
            status_emoji = "⭐"
        else:
            user_status = "🆓 FREE USER"
            status_emoji = "🆓"
            if expiry and expiry < datetime.now():
                remove_subscription_db(user_id)
    else:
        user_status = "🆓 FREE USER"
        status_emoji = "🆓"
    
    welcome_text = f"""
{status_emoji} **WELCOME TO MARCO FILE HOST ULTIMATE!** {status_emoji}

━━━━━━━━━━━━━━━━━━━━━
👤 **User:** {user_name}
🆔 **ID:** `{user_id}`
✳️ **Username:** @{user_username or 'N/A'}
🔰 **Status:** {user_status}
━━━━━━━━━━━━━━━━━━━━━

📁 **Your Storage**
• Used: {current_files} / {limit_display} files
• Limit: {'Unlimited' if file_limit == float('inf') else f'{file_limit} files'}

🚀 **Features Available**
✅ Python Script Hosting (.py)
✅ Node.js Script Hosting (.js)
✅ ZIP Archive Support
✅ Auto Dependency Installation
✅ GitHub Clone
✅ Auto Backups
✅ Scheduled Tasks
✅ Resource Monitoring

💡 **Quick Start**
1️⃣ Upload your .py, .js, or .zip file
2️⃣ Bot automatically detects main script
3️⃣ Runs your script 24/7

━━━━━━━━━━━━━━━━━━━━━
🎯 **Use buttons below**
    """
    
    try:
        photos = bot.get_user_profile_photos(user_id, limit=1)
        if photos.total_count > 0:
            file_id = photos.photos[0][-1].file_id
            bot.send_photo(
                chat_id,
                file_id,
                caption=welcome_text,
                parse_mode='Markdown',
                reply_markup=create_main_menu_keyboard(user_id)
            )
        else:
            raise Exception("No photo")
    except Exception:
        bot.send_message(
            chat_id,
            welcome_text,
            parse_mode='Markdown',
            reply_markup=create_main_menu_keyboard(user_id)
        )

# --- Cleanup ---
def cleanup():
    logger.info("🧹 Cleaning up...")
    for key, info in list(bot_scripts.items()):
        try:
            kill_process_tree(info)
        except:
            pass
    logger.info("✅ Cleanup complete")

atexit.register(cleanup)
signal.signal(signal.SIGTERM, lambda sig, frame: cleanup())

# --- Main Execution ---
if __name__ == '__main__':
    banner = """
╔══════════════════════════════════════════════════════════╗
║     🤖 MARCO FILE HOST ULTIMATE v5.0                     ║
║     ✨ Zero Slash Commands - Pure Reply Keyboard         ║
╚══════════════════════════════════════════════════════════╝
    """
    print(banner)
    logger.info("🚀 Starting bot...")
    keep_alive()
    
    # Remove webhook to avoid 409 error
    try:
        bot.remove_webhook()
        logger.info("✅ Webhook removed successfully")
        time.sleep(1)
    except Exception as e:
        logger.warning(f"Could not remove webhook: {e}")
    
    # Start polling with retry logic
    while True:
        try:
            logger.info("🔄 Starting polling...")
            bot.infinity_polling(timeout=60, long_polling_timeout=60, skip_pending=True)
        except requests.exceptions.ReadTimeout:
            logger.warning("⏰ Read timeout, restarting...")
            time.sleep(5)
        except requests.exceptions.ConnectionError:
            logger.warning("🔌 Connection error, restarting in 15s...")
            time.sleep(15)
        except telebot.apihelper.ApiTelegramException as e:
            if e.error_code == 409:
                logger.error("🚨 Conflict detected (Error 409). Retrying in 30s...")
                time.sleep(30)
            else:
                logger.error(f"💥 API Error: {e}")
                time.sleep(10)
        except Exception as e:
            logger.error(f"💥 Polling error: {e}")
            time.sleep(30)
