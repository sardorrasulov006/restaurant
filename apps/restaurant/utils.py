from pickle import FRAME

from msgpack.fallback import BytesIO
from datetime import date
from weasyprint import HTML


def generate_pdf(user, reservation):
    try:
        output = BytesIO()
        issue_date = reservation.start_time.strftime('%Y-%m-%d')

        html = f"""
        <h1>Band qilindi</h1>
        <p>Foydalanuvchi raqami: {user.phone_number, user.username}</p>
        <p> Restaron nomi: {reservation.restaurant}</p>
        <p>Sana: {issue_date}</p>
        """
        html_content = HTML(string=html)
        html_content.write_pdf(output)
        output.seek(0)
        return output.getvalue()
    except Exception as e:
        raise RuntimeError(f"Xatolik {str(e)}")
