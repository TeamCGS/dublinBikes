#!/usr/bin/env python

from sqlalchemy import create_engine
engine = create_engine('mysql://CGSdatabase:password@dublinbikes.ctaptplk7c5t.eu-west-1.rds.amazonaws.com/dublinbikes')

result = engine.execute("select number from Stations")
for row in result:
    print("username:", row['number'])
