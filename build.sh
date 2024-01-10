#!/bin/sh

echo 'Downloading the google authenticator library'

# Source: https://stackoverflow.com/questions/6122932/execute-git-command-inside-bash-script
GIT='git --git-dir='$PWD'/.git'

$GIT clone 'https://github.com/google/google-authenticator-libpam.git'

