# small-flask-project

## How to run

### Production
Go to http://localhost:5000 to see the development environment (which is similar if not the same as development atm)
To run production of this use: 
```
docker-compose up production
```

### Development
Go to http://localhost:5001 to see the development environment (which is similar if not the same as production atm)
To run development of this use: 
```
docker-compose up development 
```

### Unit tests
To run the unit tests without any external dependencies: 
```
docker-compose up unit
```

### Integration tests
To run the integration tests which has the database as external dependency: 
```
docker-compose up integration
```


##What is this?
This is a small quiz websites where you can do some simple things. Here are some of my thought about the features when I started making it: 
- So you need to be able to create quizzes which contain questions which each have multiple answers and one of them is the right one. 
- So quizzes need to be made
- The quizzes need to be able to retrieve without the right answer
- Do I want them to be created in a single go or can they also be updated? 
- You also need to be able to check your answers, at the end?
- We should also log it when someone finished a quiz

