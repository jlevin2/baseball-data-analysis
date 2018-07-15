#!/bin/bash

initdb -D ./database

pg_ctl -D ./database -l logfile start



