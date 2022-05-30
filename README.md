# **Lab: Permissions & Postgresql**

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

# **Feature Tasks and Requirements**

## **Features - Django REST Framework**

- run this command to install Django and restframwork: 
```poetry add django djangorestframework ```

- Add  ``` 'rest_framework',``` to ```INSTALLED_APPS```.
in ```settings.py```

- Create an ```api``` folder inside the app folder ```music```

- Create a ```urls.py``` file inside the ```api``` folder

- Create a ```viewsets.py``` & ```serializers.py``` files inside the ```api``` folder

### **Requirements**

- Adjust project’s permissions so that only authenticated user’s have access to API.
- Add a custom permission so that only author of blog post can update or delete it.
- Add ability to switch user’s directly from browsable API.


<br>

## **Features - Permissions**

- Create a ```permissions.py``` file inside the ```api``` folder

- Import as such in ```viewsets.py```:
 
    ```from .premissions import IsOwnerReadOnly```

- Fix the Class in ```viewsets.py```:

    ```
    class MusicsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Music.objects.all()
        serializer_class = MusicSerializer
        permission_classes = (IsOwnerOrReadOnly, )
    ```

- Add the following to ```settings.py```:

    ```
    REST_FRAMEWORK = {
        "DEFAULT_PERMISSION_CLASSES":[
            "rest_framework.permissions.IsAuthenticated",
        ]
    }
    ```


<br>

## **Features - Docker**

- Create a ```Dockerfile```
- Run: ```poetry export -f requirements.txt --output requirements.txt```
- Create ```docker-compose.yml``` 
- Run ```docker-compose build```
- Run ```docker-compose up```

<br>

## **Features - Postgresql**

- Install ```poetry add psycopg2-binary```

- Run ```poetry export -f requirements.txt --output requirements.txt``` again 

- Go to ```settings.py``` and change ```DATABASES``` to 
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'music',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

- Run: ``` docker-compose run web python manage.py migrate ```

- Run: ``` docker-compose run web python manage.py createsuperuser ```

- Run: ``` docker-compose up -d ```
