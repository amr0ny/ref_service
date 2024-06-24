## Ref service

A service allows one to сombine a bundle of links (called refs) into one. When a link is visited, IP address is assigned with a ref which goes in turn.

## Architechure

There are four components:
+ FastAPI server
  + Built on FastAPI, SQLAlchemy
  + Serves GET requests on /<link_id:uuid> and returns HTTP 307 Redirect to the corresponding ref.
  + Operates via uvicorn.
+ Django Admin
  + Built on Django
  + Allows admins to perform CRUD operations on links and refs.
  + Operates via uwsgi.
+ Postgres: Just a database which contains tables: link, ref, link_ref, link_access.
+ Nginx: set up as reverse-proxy.
  
The solution is conainerized by docker-compose.

## Deployment
To deploy the service and enjoy it, you have to follow next steps:
1. Clone the repository and Follow the root.
3. you must add next variables to .env file:
   ```bash
    POSTGRES_DB = YOUR DB NAME HERE
    POSTGRES_USER = YOUR USER USER HERE
    POSTGRES_PASSWORD = YOUR DB USER PASSWORD HERE
    POSTGRES_HOST=postgres # DO NOT CHANGE IT
    POSTGRES_PORT = YOUR DB PORT HERE
    LOG_PATH = YOUR PATH TO .LOG FILE
    LOG_LEVEL = YOUR CHOICE OF LOG MODE (DEBUG/INFO, for example)
    
    DEBUG = SET False IN PRODUCTION MODE, ELSE True 
    SECRET_KEY = YOUR DJANGO SECRET KEY

   # DO NOT CHANGE FOLLOWING
    ALLOWED_HOSTS = *
    STATIC_ROOT = /var/www/static 
    STATIC_URL = static/
    MEDIA_ROOT = /var/www/media
    MEDIA_URL = media/
    UVICORN_HOST=0.0.0.0
    UVICORN_PORT=80
    UVICORN_WORKERS=4
    UVICORN_LOG_LEVEL=debug
   ```
4. Run the service by: ```docker-compose up -d --build```
5. You must create an admin superuser by ```docker-compose exec -it admin python manage.py createsuperuser```, then fill the fields and proceed.
6. Finally, you got it.
   
NOTICE: In case you rebuild your postgres container, all the data will be lost,
        if this contradicts your expectations, you can add next line to postgres container in docker-compose.yml:
   ```yaml
   volumes:
     - $HOME/postgresql/data:/var/lib/postgresql/data
   ```
## How to use
If you want to create new link, follow admin panel, then links->new link,
Name it the way you want and add refs.
IMPORTANT: Ref URL must look like this: https://yourdomain.com/, in other words, it should include procotol name.
To use the link, you should simply follow /<link_id>, for example: https://yourdomain.com/c07087f8-d0aa-46de-befd-ed93e405216c




