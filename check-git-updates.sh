#!/bin/bash

LOGTIME=$(date +'%F-%H:%M')

flask_update() {
    CHANGED_FILES=$(git diff $LOCAL $REMOTE)

    if echo "$CHANGED_FILES" | grep -q "app/"; then
	echo "$LOGTIME: App updated, rebuilding image" >> $LOGS
        docker compose up -d --build
    fi

}

GIT_DIR='/home/eoinh/days-of-code-portfolio-website'
BRANCH='production-main'
LOGS='/home/eoinh/sitedeploy.log'

echo "$LOGTIME: Checking for updates on" >> $LOGS

cd $GIT_DIR || exit

git fetch origin $BRANCH

# Check if local is behind remote
LOCAL=$(git rev-parse $BRANCH)
REMOTE=$(git rev-parse origin/$BRANCH)

if [ $LOCAL != $REMOTE ]; then
    echo "$LOGTIME: Updates found. Pulling latest changes..." >> $LOGS
    git pull origin $BRANCH >> $LOGS 2>&1
	
    flask_update

    echo "$LOGTIME:Deployment complete." >> $LOGS
else
    echo "$LOGTIME:No updates found." >> $LOGS
fi
