#!/bin/bash

err() {
    echo "ERROR: $*" >>/dev/stderr
}

if [ -z "$1" ]; then
    err "No install directory given."
    exit 1
fi

BASE_DIR=$1
INSTALL_DIR=$BASE_DIR/shell-prompt/

if [ ! -d "$BASE_DIR" ]; then
    err "Given install directory does not exist: $BASE_DIR"
    exit 1
fi

if [ ! -d "$INSTALL_DIR" ]; then
    echo "Creating install directory: $INSTALL_DIR"
    mkdir $INSTALL_DIR
fi

echo "Copying scripts..."
cp color.py $INSTALL_DIR
cp prompt.py $INSTALL_DIR

echo "Copying settings file sample..."
cp settings.json $INSTALL_DIR

echo "Creating launch script..."
echo "export PS1=\`python3 ${INSTALL_DIR}prompt.py\`" > ${INSTALL_DIR}prompt.sh

echo "Done."