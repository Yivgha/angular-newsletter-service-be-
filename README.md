# Newsletter Service Backend

![https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![https://img.shields.io/badge/Docker-black?style=for-the-badge&logo=docker](https://img.shields.io/badge/Docker-black?style=for-the-badge&logo=docker)

## About

This backend service made on Python/FASTapi. It contains dummy data, deployed via Docker on Google Cloud, so this data can be reached on frontend if host url is in the list of friendly origins.

Environment and Docker can work in development, production or stading modes.

After opening backend's url, you can see default message. To see posts, add "/posts" endpoint. On this endpoint you can get all posts or filter them by inculding tags "/posts/?tag=tagValue".

Also you can reach data from one post by "post/:id" endpoint.

