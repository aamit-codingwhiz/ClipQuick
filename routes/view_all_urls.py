# routes/view_all_urls.py
from flask import Blueprint, render_template
from services.view_all_urls_service import ViewAllURLsService

view_all_urls_bp = Blueprint(
    name='view_all_urls', 
    import_name=__name__
)

@view_all_urls_bp.route(rule="/all_urls")
def all_urls():
    """Route to display all shortened URLs."""
    urls = ViewAllURLsService.get_all_urls()
    return render_template(
        template_name_or_list="all_urls.html", 
        urls=urls
    )
