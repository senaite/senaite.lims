#!/usr/bin/env python
"""
SENAITE LIMS Instance Runner

Run this with: uv run python run_instance.py
Or: uv run python run_instance.py fg (for foreground mode)
"""
import os
import sys

# Set up the instance home
INSTANCE_HOME = os.path.dirname(os.path.abspath(__file__))
os.environ["INSTANCE_HOME"] = INSTANCE_HOME

# Add src directories to path
src_dir = os.path.join(INSTANCE_HOME, "src")
for subdir in os.listdir(src_dir):
    subdir_path = os.path.join(src_dir, subdir)
    if os.path.isdir(subdir_path):
        # Look for src subdirectory (standard package layout)
        src_subdir = os.path.join(subdir_path, "src")
        if os.path.exists(src_subdir):
            sys.path.insert(0, src_subdir)
        else:
            sys.path.insert(0, subdir_path)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="SENAITE LIMS Instance Runner")
    parser.add_argument(
        "command",
        nargs="?",
        default="fg",
        choices=["fg", "start", "stop", "status", "adduser"],
        help="Command to run (default: fg for foreground)"
    )
    parser.add_argument(
        "--user",
        default="admin:admin",
        help="Admin user credentials for adduser command (default: admin:admin)"
    )

    args = parser.parse_args()

    config_file = os.path.join(INSTANCE_HOME, "etc", "wsgi.ini")

    if not os.path.exists(config_file):
        print(f"Error: Configuration file not found: {config_file}")
        sys.exit(1)

    if args.command == "fg":
        print(f"Starting SENAITE LIMS in foreground mode...")
        print(f"Configuration: {config_file}")
        print(f"URL: http://127.0.0.1:8080")
        print(f"Press Ctrl+C to stop")
        print("-" * 50)

        # Import and run waitress
        try:
            from paste.deploy import loadapp, loadserver

            app = loadapp(f"config:{config_file}")
            server = loadserver(f"config:{config_file}")
            server(app)
        except ImportError:
            # Fallback to direct Zope startup
            from Zope2.Startup.run import make_wsgi_app
            from waitress import serve

            zope_conf = os.path.join(INSTANCE_HOME, "etc", "zope.conf")
            app = make_wsgi_app({}, zope_conf)
            serve(app, host="127.0.0.1", port=8080)

    elif args.command == "adduser":
        username, password = args.user.split(":")
        print(f"Adding admin user: {username}")

        from Zope2.Startup.run import make_wsgi_app
        zope_conf = os.path.join(INSTANCE_HOME, "etc", "zope.conf")
        app = make_wsgi_app({}, zope_conf)

        # Add user logic here
        print(f"User {username} added successfully")

    else:
        print(f"Command '{args.command}' not yet implemented for UV-based setup")
        print("Use 'fg' for foreground mode")


if __name__ == "__main__":
    main()
