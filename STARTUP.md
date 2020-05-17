# Steps to start your local instance
1. docker-compose build
2. docker-compose up
3. docker exec fs /bin/bash -c "fs_createdb.sh"
4. docker-compose down
5. docker-compose up
6. go to http://localhost:5050/browser to check db admin page
    - Check the docker-compose.yml for the user/pwd
7. go to http://localhost:8080 for the project page
