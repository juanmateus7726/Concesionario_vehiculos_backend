import logging
import time

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    """
    Registra cada petición HTTP que llega al backend.
    Muestra: método, ruta, status, tiempo de respuesta, y quién lo hizo.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()

        response = self.get_response(request)

        duration = round((time.time() - start) * 1000, 2)

        # Si el usuario está autenticado mostramos su nombre y rol
        if hasattr(request, 'user') and request.user.is_authenticated:
            user_info = f"{request.user.username} (rol: {request.user.role})"
        else:
            user_info = "anónimo"

        logger.info(
            f"{request.method} {request.path} "
            f"→ {response.status_code} | {duration}ms | {user_info}"
        )

        return response