# Install requirements
    pip install -r requirements.txt

# Configure environment

Set enviroment variables with your sqs credentials

    AWS_USER_ID=your user id
    AWS_USER_KEY=your key
    AWS_REGION=us-east-1

# Run Fast API
    python runserver.py
    # check route at localhost:8000/docs

# Run Celery worker
    celery --app=runcelery worker