# Boda Justice

The Boda Justice app is an application that promotes Social Justice by enabling users to report complaints such as Police Harassment etc.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
- Just clone this repository by typing: `git clone https://github.com/boda-justice/boda-justice-frontend.git`
- Switch to project directory: `cd boda-justice-frontend`
- Install project requirements using python pipenv. But wait, you have to have some stuff before you get to this point. So these are:

### Prerequisites

- Python3.5 and above
- Python pipenv
Just type:
```
python -V
```
in your terminal and if its not greater than or equal to 3.5, you're not in big trouble, there are tons of tutorials to get up up and running with these. Just grub one then come back when done.

### Installing

Now, you have python3 and a way of running a virtual environment. Lets set up the project environment.(remember we're still in the app directory)

## Usage

Due to the current Service Worker [specification](https://w3c.github.io/ServiceWorker/#secure-context), the web browser will only allow its registration if the application is served over **https, or on localhost** for development purposes.

This makes **nGrok** useful for testing the PWA functionality, as it allows you to expose localhost over the internet with **https** included.

### localhost

```shell
> pipenv run flask run
```

### nGrok

```shell
> pipenv run flask run
> ngrok http 80
```


This is enough to get you started.
You can now run the application using:
`pipenv run flask run`


## Running the tests

No automated tests yet.

## Deployment

This app is ready for Heroku. You can deploy your copy of this app by:
`heroku create <your_url_name>` (where <your_url_name> is what you want to call your app)
`git push heroku master` 
..and boom, you're done! You can chat me on gitter in case of any problems.(gitter link is on badge above)
If you have never worked with Heroku, you can learn how to [Deploy Python Applications on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)

## Built With

* [Python Flask](https://www.fullstackpython.com/flask.html) - The web framework used
* [MaterializeCSS](https://materializecss.com) - The sleek styling

## Contributing

TBD

## Versioning

For the versions available, see the [tags on this repository](https://github.com/boda-justice/boda-justice-frontend/tags). 

## Authors

* **James Lemayian** - *Developing* - [@Lemmah](https://github.com/lemmah)

* **Newton Adams** - *Developing* - [@Blackadams](https://github.com/Blackadams)


## License

This project is currently under the MIT License.

## Acknowledgments

TBD

