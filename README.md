# VIBBIDI V6 Web API

## Installation
In base project directory, create file `config.env` from template `config-template.env`.

In base project directory, create file `Procfile` from template `Procfile-template`:  
`--workers (2 * CPU Cores + 1)`

Execute commands:  
```
pip3 install --user virtualenv
virtualenv -p python3 env
 
. env/bin/activate
pip install -r requirements.txt
```

## Start Web API server
In base project directory, execute commands to start 2 services:
```
. env/bin/activate
FLASK_APP=manage flask clean_cache && FLASK_APP=manage flask maintain

. env/bin/activate
honcho start
```

## Automatic URI mapping
```
. env/bin/activate
FLASK_APP=manage flask uri_mapping
```

## Run at startup
Add code to `/etc/rc.local`.  
For example:  
```
su ec2-user -c '/home/ec2-user/scripts/tmux-web-api.sh'
```

## Debug Web API server (PyCharm)
![debug](documents/debug.png?raw=true)