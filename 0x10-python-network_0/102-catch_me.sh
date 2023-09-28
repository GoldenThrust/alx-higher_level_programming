#!/bin/bash
# causes the server to respond with a message containing You got me!
curl -sL -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
