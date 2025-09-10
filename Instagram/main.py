from fastapi import FastAPI
from Instagram.db import models
from Instagram.db.database import engine
from Instagram.routes import user, ig_post, comment
from Instagram.auth import authentication
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

###
app = FastAPI()


###
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(ig_post.router)
app.include_router(comment.router)

@app.get('/')
def home():
    return {"message" : 'Instagram App in Developement.'}


# Ensure the directory exists
os.makedirs("Instagram/images", exist_ok=True)

###
app.mount("/images", StaticFiles(directory="Instagram/images"), name="images")
'''
app.mount() is also commonly used with StaticFiles 
to serve static assets like HTML, CSS, JavaScript, 
or images from a specified directory.
'''

### Create DB Tables.
models.Base.metadata.create_all(engine)


### CORS 

origin = [
    'http://localhost:3000',
    'http://localhost:8000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)
