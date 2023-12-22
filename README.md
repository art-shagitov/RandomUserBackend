## Random name generator

###
1. Run docker compose up -d within this directory
2. Navigate to http://localhost:8081/get_random_users to get a list of randomly generated users and their quantity
3. Navigate to http://localhost:8081/get_database_users?skip=0&limit=100 to verify that previously generated users are stored in random_users table in a PostgreSQL database

## Notes
###
1. .env file contains basic PostgreSQL credentials as well as MIN_N, MAX_N variables that determine the lower and upper bounds of the number of randomly generated users 
