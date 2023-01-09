# API-Project #
## Omschrijving van het project
In dit project heb ik ervoor gekozen om een api te maken waarin iemand zich kan registreren. Vervolgens kan deze dan zijn of haar oefeningen en persoonlijke records bijhouden, gelinkt aan het profiel.

## link naar okteto hosted api ##
https://useritem-api-service-matthiastheys.cloud.okteto.net/docs


# Screenshots OpenAPI-docs #

## authorize ##

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/auth1.png?raw=true)
![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/auth2.png?raw=true)


## token ##

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/token1.png?raw=true)
![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/token2.png?raw=true)

## current user ##

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/user_medocs.png?raw=true)

## all users ##

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/readusers1.png?raw=true)
![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/readusers2.png?raw=true)

## create user ##

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/createuser1.png?raw=true)
![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/createuser2.png?raw=true)

## get user with userid ##

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/readuseriddocs.png?raw=true)

## get heaviest lift from user ##

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/readuserheaviestdocs.png?raw=true)

## get all lifts from user ##

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/readuserliftsdocs.png?raw=true)

## update lifts from user ##

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/updateuserlift1.png?raw=true)
![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/updateuserlift2.png?raw=true)

## create a lift for user ##

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/createuserlift1.png?raw=true)
![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/createuserlift2.png?raw=true)

## remove a user's lift ##

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/removeuserliftdocs.png?raw=true)

##remove user with email

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/removeuserdocs.png?raw=true)



#Screenshots postman
##token

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/post_token.png?raw=true)

##current user

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/users_me.png?raw=true)

##all users

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/users.png?raw=true)

##create user

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/create_user.png?raw=true)

##get user with userid

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/users_3.png?raw=true)

##get heaviest lift from user

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/users_3_heaviestlift.png?raw=true)

##get all lifts from user

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/users_3_alllifts.png?raw=true)

##update lifts from user

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/users_3_updatelift.png?raw=true)

##create a lift for user

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/users_3_createlift.png?raw=true)

##remove a user's lift

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/Screenshot%202023-01-09%20180538.png?raw=true)

##remove user with email

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/users_delete.png?raw=true)


##tests
Ik heb voor dit project ook 5 tests geschreven om elk get endpoint te testen.
Deze worden gerund met pytest en staan in het bestand test_api2.py

![alt text](https://github.com/MatthiasTheys/api2/blob/main/images/tests.png?raw=true)