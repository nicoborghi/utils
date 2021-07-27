### apt backups

A quick way of backing up a list of programs is to run this:

```
dpkg --get-selections > ~/Package.list
sudo cp -R /etc/apt/sources.list* ~/
sudo apt-key exportall > ~/Repo.keys
```

It will back them up in a format that dpkg can read* for after your reinstall, like this:

```
sudo apt-key add ~/Repo.keys
sudo cp -R ~/sources.list* /etc/apt/
sudo apt-get update
sudo apt-get install dselect
sudo dselect update
sudo dpkg --set-selections < ~/Package.list
sudo apt-get dselect-upgrade -y
```

### conda backups

```
conda env create -f environment.yml
```


### additional packages
- Baccus
- Bagpipes
- CosmoBolognaLib
- FSPS
- H0 tension
- julia 
- montepython_public
- Plank2018
- prospector
- python-fsps
- SciScript-Python
- SDSS_get
- sedpy 
