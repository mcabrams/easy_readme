# Easy Readme
> Always looking up markdown syntax when you start a new project?  Get a good looking barebones README.md in seconds with one command.
## Installing package
```sh
python easy_readme/setup.py install
```
## Start a new project and use
```sh
mkdir new-project
cd new-project
easy-readme
git init
git add .
git commit -m "Add readme; initial commit"
```
## Development Setup
```sh
docker-compose run app bash
```
## Running Tests
```sh
docker-compose run app bash
python -m unittest discover
```
