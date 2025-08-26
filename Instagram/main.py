from fastapi import FastAPI
from database import models
from database.database import engine
from routes import user, ig_post, comment
from auth import authentication
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

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



###
app.mount("/images", StaticFiles(directory="images"), name="images")
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
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)
