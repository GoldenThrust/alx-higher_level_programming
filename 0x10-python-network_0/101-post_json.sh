#!/bin/bash
# displays the body of the response.
curl -sH "Content-Type: application/json" -d $(cat $2) $1
