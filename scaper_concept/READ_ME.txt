By Sam Ehlers

To use this scraper concept, you must have RabbitMQ installed

Visit the RabbitMQ site to download using the official documentation (https://www.rabbitmq.com/)

Celery, the queuing library used in this project, relies on having RabbitMQ installed.

To use this application, do the following:
    1. Open a new terminal tab
    2. Move to the scraper_concept folder
    3. Activate the virtual environment (source venv/bin/activate)
    4. Close any existing RabbitMQ servers ('sudo rabbitmqctl shutdown')
    5. Start a RabbitMQ server with 'sudo rabbitmq-server'
    6. Open another new terminal tab
    7. Move to the scraper_concept folder
    8. Activate the virtual environment (source venv/bin/activate)
    9. Start a celery worker with 'celery -A tasks worker -B --loglevel=INFO'

Thank you for checking this out, and good luck!