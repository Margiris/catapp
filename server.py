from app import app
from cheroot.wsgi import Server as WSGIServer, PathInfoDispatcher

d = PathInfoDispatcher({'/': app})
server = WSGIServer(('0.0.0.0', 8080), d)

if __name__ == '__main__':
    try:
        print("Starting server...")
        print("Server started")
        server.start()

    except KeyboardInterrupt:
        print("\nStopping...")
        server.stop()
        print("Stopped")
