#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_trapezaria.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

     # Adicione o argumento --port seguido pelo número da porta desejada
    sys.argv.append('--noreload')  # Opcional: Desativa o recarregamento automático para evitar problemas com algumas alterações na porta
    sys.argv.append('--port=8001')  # Substitua 8001 pelo número da porta desejada

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
