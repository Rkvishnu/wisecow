#!/usr/bin/env bash

SRVPORT=4499
RSPFILE=response

rm -f $RSPFILE
mkfifo $RSPFILE

handleRequest() {
    # 1) Process the request
    cat <<EOF > $RSPFILE
HTTP/1.1 200

Hello, World!
EOF
}

main() {
    echo "Wisdom served on port=$SRVPORT..."

    while [ 1 ]; do
        nc -lN $SRVPORT | handleRequest
    done
}

main
