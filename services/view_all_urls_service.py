# services/view_all_urls_service.py
from models.url import ShortURL

class ViewAllURLsService:

    @staticmethod
    def get_all_urls():
        """Retrieve all shortened URLs from the database."""
        return ShortURL.query.all()
