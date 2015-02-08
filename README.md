Custom Heroku buildpack with Numpy + Scipy:
https://github.com/thenovices/heroku-buildpack-scipy

Launch custom buildpack on old Cedar stack:
heroku create --buildpack https://github.com/thenovices/heroku-buildpack-scipy --stack cedar
