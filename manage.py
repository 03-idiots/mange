import os
import subprocess
import sys


def activate_virtualenv():
    """Activate virtual environment."""
      # Windows
    # activate_script = '/path/to/your/virtualenv/bin/activate'  # Unix-based systems
    if os.name == 'nt':
        subprocess.call(activate_script, shell=True)
    else:
        subprocess.call(f'source {activate_script}', shell=True, executable='/bin/bash')

def main():
    #activate_virtualenv()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_system_facial_recognition.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
