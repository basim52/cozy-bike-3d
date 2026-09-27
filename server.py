import http.server
import socketserver
import socket
import webbrowser
import os
import sys

PORT = 8080

# Determine local IP address for mobile access
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

local_ip = get_local_ip()

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Keep terminal output clean
        pass

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Find available port
while PORT < 8095:
    try:
        with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
            print("=" * 60)
            print("🚴💨 جولة دراجة الضاحية | Cozy Downhill Bike 3D")
            print("=" * 60)
            print(f"💻 للعب على الكمبيوتر مباشرة:")
            print(f"   http://localhost:{PORT}")
            print()
            print(f"📱 للعب على الجوال (نفس شبكة الواي فاي Wi-Fi):")
            print(f"   http://{local_ip}:{PORT}")
            print("=" * 60)
            print("اضغط Ctrl+C لإيقاف الخادم")
            print("=" * 60)
            sys.stdout.flush()
            
            # Auto-open in PC browser
            try:
                webbrowser.open(f"http://localhost:{PORT}")
            except Exception:
                pass
                
            httpd.serve_forever()
            break
    except OSError:
        PORT += 1
