export CVSIGNORE="settings.py logs media log temp *.pyc"
rsync -avrz -e 'ssh -p 22' --port=22 --cvs-exclude --no-p --no-g --chmod=ugo=rwX ./* hspace@freesquatters.com:/usr/home/hspace/h-hspace.com/www/
