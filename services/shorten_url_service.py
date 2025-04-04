# services/shorten_url_service.py
from datetime import datetime, timedelta, timezone
from models.url import db, ShortURL
from utils.qr_code import generate_qr_code

class ShortenURLService:

    @staticmethod
    def shorten_url(original_url, password=None, expire_in_days=7):
        """Generate a short URL and store it in the database."""
        short_code = ShortURL.generate_short_code()
        password_hash = ShortURL.set_password(password=password) if password is not None else None

        new_url = ShortURL(
            original_url=original_url, 
            short_code=short_code,
            password_hash=password_hash,
            expires_at = datetime.now(timezone.utc) + timedelta(days=expire_in_days)
        )
        db.session.add(new_url)
        db.session.commit()

        qr_filename = generate_qr_code(
            short_code=new_url.short_code
        )
        return new_url.short_code, qr_filename
    
    
    @staticmethod
    def is_expired(url):
        return url.expires_at and datetime.now(timezone.utc) > url.expires_at
    

    @staticmethod
    def is_password_protected(short_code):
        url = ShortURL.query.filter_by(short_code=short_code).first()
        print(f"is_password_protected: > {url.password_hash} || type: > {type(url.password_hash)}")
        return True if url.password_hash is not None else False


    @staticmethod
    def get_original_url(short_code, password=None):
        """Get the original URL for a given short code."""
        url = ShortURL.query.filter_by(short_code=short_code).first()

        if password is not None:
            return url.original_url if ShortURL.check_password(url=url, password=password) else None

        return url.original_url if url else None
