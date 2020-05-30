#!/bin/bash
CURRENT_UID=$(id -u):$(id -g) SAVE_FOLDER=$(pwd)/data docker-compose up --force-recreate