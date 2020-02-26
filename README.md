http://www.nmahser.com
# portfolio
This website is over-engineered by design to showcase skills with range of tools. The application is built using Django Web Framework. There is a also Postgres database which stores project details and contact data. Having a database enables the use of the Django admin interface, where new projects can be directly added and removed without modifying HTML files. All of the media and static files are hosted in Amazon S3. The last piece of the application is Celery and SQS (Message Broker) which are used for the contact form. Celery enables asynchronous task execution, and message broker is needed to maintain the task list and signal the status of finished tasks. This facilitates concurrent use of the contact form, thereby removing any lag or wait time.
Tools Used

## Installation/Preparation
Coming soon...
