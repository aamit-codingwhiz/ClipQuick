# routes/shorten_url.py
from flask import Blueprint, request, redirect, url_for, flash, render_template
from services.shorten_url_service import ShortenURLService

shorten_url_bp = Blueprint(
    name='shorten_url', 
    import_name=__name__
)

# Route to handle URL shortening
@shorten_url_bp.route(rule="/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        original_url = request.form.get(
            key="original_url"
        )
        
        # custom_code = request.form.get(
        #     key="custom_code"
        # )

        # Inside your route where the URL is saved
        password = request.form.get(key="password")
        
        print(f"password: {password} || type: {type(password)}")
        if password is None:
            print(f"Password not provided: {password}")

        if len(password) == 0:
            password = None
            print("password is empty")

        is_checked_generate_qr = "generate_qr" in request.form
        print(f"is_checked_generate_qr: {is_checked_generate_qr} || type: {type(is_checked_generate_qr)}")

        if not original_url:
            flash(
                message="URL is required!", 
                category="warning"
            )
            return redirect(
                location=url_for(endpoint="shorten_url.home")
            )

        short_code, qr_filename = ShortenURLService.shorten_url(
            original_url=original_url,
            password=password
        )
        short_url = request.host_url + short_code

        if is_checked_generate_qr:
            return render_template(
                template_name_or_list="index.html", 
                short_url=short_url, 
                qr_filename=qr_filename
            )
        else:
            return render_template(
                template_name_or_list="index.html", 
                short_url=short_url
            )


    return render_template(
        template_name_or_list="index.html"
    )

# New route to handle redirection from short URL to original URL
@shorten_url_bp.route(rule="/<string:short_code>", methods=["GET", "POST"])
def redirect_to_url(short_code):
    if request.method == "POST":
        password = request.form.get(
            key="password"
        )

        original_url = ShortenURLService.get_original_url(short_code, password)
        if original_url:
            return redirect(original_url)
        else:
            flash(message="Wrong Password!", category="error")
            return redirect(url_for("shorten_url.redirect_to_url", short_code=short_code))


    if short_code:
        # print(f"short code: {short_code} || type: {type(short_code)}")
        if short_code == "favicon.ico":
            return "", 204  # Ignore favicon request

        if ShortenURLService.is_password_protected(short_code=short_code):
            return render_template(
                template_name_or_list="password_entry.html",
                short_code=short_code
            )

        # Fetch the original URL using the short code
        original_url = ShortenURLService.get_original_url(short_code)
        if original_url:
            return redirect(original_url)  # Redirect to the original URL
        else:
            flash(message="Invalid URL!", category="error")
            return redirect(url_for("shorten_url.home"))
