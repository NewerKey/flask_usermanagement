## Unit Tests

- Test creating a new User (check email, check not plaintext password, check registration date, check is_authenticated is false)
- Test verifying the password for a User
- Test changing the password for a User and then verifying the password for that User
- Check that the get_id() method returns a string, not an integer (needed for Flask-Login)

## Functional/Integration Tests

- Registration:
  - Test registering a new, valid user
  - Test registering with different passwords
  - Test registering with an improperly formatted email address
  - Test registering with an existing user

## End-to-end Tests

- Test app with chrome and firefox

## Setup CI/CD Suppport with Github Actions
