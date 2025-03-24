#!/bin/bash

if [[ $1 == 'list' ]] then
    $HOME/.pyenv/versions/3.12.8/bin/python -m fabric list-all

elif [[ $1 == 'install' ]] then
    $HOME/.pyenv/versions/3.12.8/bin/pip install $2

elif [[ $1 == 'update' ]] then
    echo "Updating, please wait..."
    $HOME/.pyenv/versions/3.12.8/bin/pip install git+https://github.com/Fabric-Development/fabric.git -q
    echo "DONE :)"

else
    $HOME/.pyenv/versions/3.12.8/bin/python $HOME/.config/fabric/main.py

fi

