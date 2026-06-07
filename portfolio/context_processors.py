from django.conf import settings


def social_links(request):
    """Expose SOCIAL_LINKS to templates as `SOCIAL_LINKS`."""
    return {"SOCIAL_LINKS": getattr(settings, "SOCIAL_LINKS", {})}
