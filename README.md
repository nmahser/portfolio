http://www.nmahser.com
# portfolio
Why not building over-engineered portfolio web app? The application is built using Django Web Framework. There is also Postgres database which stores project details and contact data. Having a database enables us to use Django admin interface, where we can directly add/remove new project without modifying HTML files. The application is deployed to AWS Elastic Beanstalk, and all of the media and static files are hosted in Amazon S3. The last piece of the application is Celery and SQS (Message Broker) which are used for the contact form. Celery enables asynchronous task execution. SQS is used to maintain the task list and signal the status of finished task. In this case, users don’t need to wait for the application to sequentially handle other submitted contact forms.
Tools Used

## Installation/Preparation
Coming soon...
