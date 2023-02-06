<h1 align="center">Djange store template 👋</h1>
<p>
  <a href="http://localhost:8080/redoc/" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
</p>

Django Store Template is a demonstration of a backend application built using Django framework. The project showcases the use of two apps - Account and Store, following Django project architecture. Additionally, the project demonstrates the integration of various tools with Django, including pytest for testing, celery and RabbitMQ for scheduling tasks, and Docker and Docker-Compose for containerizing the entire application.

## The usage of this template is pretty easy:

### Install & build docker images using docker compose:

```sh
make build
```

## to run the containers:

```sh
make local
```

To use different API that the backend provides, make sure to use add the prefix 'JWT `<your token>` ' to the request header, if you are asked for authentication.

## To run pytest use:

```sh
make test
```

to generate the test coverage report.

```sh
make coverage
```

### Django Admin

to create an admin user use the following command:

```sh
make superuser
```

and then login in the admin panel with your credentials.

> Note: if you have problems running Makefile commands line, you can just check Makfile file, then copt and past the commands into your terminal.

## Author

👤 **na0495**

* Website: https://mrabet-saad.me/
* Github: [@na0495](https://github.com/na0495)
* LinkedIn: [@mrabet saad](https://www.linkedin.com/in/saad-mrabet/)

## Show your support

Give a ⭐️ if this project helped you!

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
