#!/bin/bash

function upd_curr() {
  cd /srv/live
  source venv/bin/activate
  python2 manage.py parse_currency
}
upd_curr