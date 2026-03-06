# TradeAID Ghana Website

A Django 5.0.6 web application for TradeAID Integrated (tradeaidgh.org), a non-profit organization in Bolgatanga, Ghana supporting small-scale producers and women entrepreneurs.

## Features

- Corporate information pages
- Project showcase (BAWEMAS, COSLEC, SHINE, IEOW, etc.)
- Blog/News section
- Photo gallery
- Contact form with email notification
- File download system

## Tech Stack

- **Backend:** Django 5.0.6 (Python 3.8+)
- **Database:** SQLite
- **Static Files:** WhiteNoise

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/eyingurah/tradeaidgh.git
cd tradeaidgh
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
cd myshop
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000

## Project Structure

```
tradeaidgh/
├── myshop/                  # Django project
│   ├── manage.py
│   ├── myshop/              # Django settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── shop/                # Main application
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── admin.py
│   │   ├── templates/
│   │   └── static/
│   └── requirements.txt
└── README.md
```

## Admin Panel

Access at http://127.0.0.1:8000/admin

## Deployment

For production deployment:

1. Set `DEBUG=False` in settings.py
2. Configure ALLOWED_HOSTS
3. Run `python manage.py collectstatic`
4. Use WhiteNoise or configure a web server (nginx, Apache)

## License

Proprietary - TradeAID Integrated
