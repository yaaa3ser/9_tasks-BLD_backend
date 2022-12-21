## **_*Running Asynchronous Tasks using Celery*_**
----------------------------------------

1. Installed redis-server

2. Installed celery as a project dependency

3. Installed redis as a project dependency

4. Integrated celery with the project

5. Setup a gmail email to use for this project to send emails from

6. Used django-environ to import secure environment variables like the redis server address or email credentials

7. Defined a task in albums/tasks.py 

8. Defined a task that receives the artist and album data as arguments and send the artist a congratulation email.
    - [see tasks.py](/albums/tasks.py)

    - [edit views](/albums/views.py)
        ```py
        if serializer.is_valid():
            serializer.save()
         -->send_congratulation_email(data,user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ```


## **_*Finished*_**