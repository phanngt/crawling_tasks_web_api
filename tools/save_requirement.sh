#bin/bash

echo 'saving dependencies to requirements.txt'
source ../env/bin/activate
pip freeze > ../requirements.txt