#!/bin/bash

initdb -D ./database -U admin --pwfile=./config/pw.txt

pg_ctl -D ./database -l logfile start



