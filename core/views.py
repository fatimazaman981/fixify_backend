from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health(request):
    """Run a real SELECT 1 so a 200 proves the database is reachable."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
    except Exception:
        return Response({"status": "error", "db": "unreachable"}, status=503)
    return Response({"status": "ok", "db": "connected"})
