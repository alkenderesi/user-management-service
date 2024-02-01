# Further Improvements

* Password encryption using [Argon2](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#argon2id)
* Authentication with a [JWT token](https://jwt.io/introduction) system
* Authorization system for the [CRUD endpoints](../src/crud.py)
* Additional information to the [auto-generated API documentation](https://fastapi.tiangolo.com/tutorial/metadata/)
* Unit tests (all major functionality currently uses the [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection) pattern, making [mock testing](https://en.wikipedia.org/wiki/Mock_object) easy)
* CI scripts (running the unit tests on each push, using [GitHub Actions workflows](https://docs.github.com/en/actions/using-workflows/about-workflows))
