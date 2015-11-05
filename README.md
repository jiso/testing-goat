# testing-goat
Python Testing Goat

[![Build Status](https://travis-ci.org/jiso/testing-goat.svg?branch=master)](https://travis-ci.org/jiso/testing-goat)
[![Coverage Status](https://coveralls.io/repos/jiso/testing-goat/badge.svg?branch=master)](https://coveralls.io/github/jiso/testing-goat?branch=master)


# Travis-CI to Heroku Notes:

* Create [Travis-CI](https://travis-ci.org/) account 
* Create [Coveralls.io](https://coveralls.io) account
* See .travis.yml for an example file to run tests and deploy
* (Travis-CI Headless Browser)[http://docs.travis-ci.com/user/gui-and-headless-browsers/] - xvfb (functional tests) and phantomjs
* [CI Obey the goat](http://chimera.labs.oreilly.com/books/1234000000754/ch20.html#_running_our_qunit_javascript_tests_in_jenkins_with_phantomjs) - for example on how to run javascript tests
* [Travis-CI -> Heroku](http://docs.travis-ci.com/user/deployment/heroku/)
