# Import the dependencies.

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, distinct
import datetime as dt

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

"""
The date for the last year starting from the most recent date in the dataset is
being used in multiple functions, so we calculate it as a global value.
"""

# the most recent percipitation
most_recent_date = session.query(Measurement.date).\
    order_by(Measurement.date.desc()).first()

# convert the string format to date formate
most_recent_dateteime = dt.datetime.strptime(most_recent_date[0],\
                                                "%Y-%m-%d").date()

# find the date of last year from the most recent year
last_yr_date = most_recent_dateteime - dt.timedelta(days=365)

# clsoe the session
session.close()

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():

    """
    All available api routes.
    """
    return (
        f"Available Routes:<br/>"
        f"Last year precipitation: <a href=\"/api/v1.0/precipitation\">\
            /api/v1.0/precipitation<a><br/>"
        f"All active stations: <a href=\"/api/v1.0/stations\">\
            /api/v1.0/stations<a><br/>"
        f"Temperature for one year: <a href=\"/api/v1.0/tobs\">\
            /api/v1.0/tobs<a><br/>"
        f"Calculate [minimum, average, maximum] temperatures for given:<br/>"
        f"-- Start date; <a href=\"/api/v1.0/yyyy-mm-dd\">\
            /api/v1.0/yyyy-mm-dd<a><br/>"\
        f"-- Start and End dates: <a href=\"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd\">\
            /api/v1.0/yyyy-mm-dd/yyyy-mm-dd<a>"
    )
    
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Start a new session
    session = Session(engine)

    """
    Precipitation across all stations for the last year
    """
    # query all percipitation in the last year
    last_yr_prcp = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= last_yr_date).all()
    
    # clsoe the session
    session.close()

    # save as a dictionary
    percipitaion = {}
    for date, percp in last_yr_prcp:
        percipitaion[date] = percp
    
    precipitation = []
    for date, prcp in last_yr_prcp:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        precipitation.append(prcp_dict)

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():

    # Start a new session
    session = Session(engine)

    """
    All the active stations in Hawaii
    """
    # Return a list of active weather stations in Hawaii

    active_stations = session.query(Measurement.station).\
        group_by(Measurement.station).all()

    # clsoe the session
    session.close()

    # Convert the tuples into a list of strings
    stations_list = list(np.ravel(active_stations)) 

    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():

    # Start a new session
    session = Session(engine)

    """
    Temperature observations of the most-active station for the previous year
    """

    # the most active station
    most_active_station = session.query(Measurement.station).\
        filter(Measurement.date >= last_yr_date).\
            group_by(Measurement.station).\
                order_by(func.count(Measurement.station).desc()).\
                    first()
    
    # all temperatures of the most active station
    tobs = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active_station[0]).\
            all()
    
    # close the session
    session.close()

    tobs_list = []
    for date, temp in tobs:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Temperature"] = temp
        tobs_list.append(tobs_dict)   

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def from_date(start):
        
    # Start a new session
    session = Session(engine)

    """    
    Calculate minimum, average and maximum temperatures for given start date.
    """

    summary_from_date = session.query(func.min(Measurement.tobs), \
                                      func.avg(Measurement.tobs), \
                                        func.max(Measurement.tobs)).\
                                            filter(Measurement.date >= start).\
                                                all()
    
    # close the session
    session.close()
    
    return jsonify(list(np.ravel(summary_from_date)))
    
@app.route("/api/v1.0/<start>/<end>")
def from_to_date(start, end):

    # Start a new session
    session = Session(engine)

    """    
    Calculate minimum, average and maximum temperatures for given start and end date.
    """

    summary_from_to_date = session.query(func.min(Measurement.tobs),\
                                         func.avg(Measurement.tobs), \
                                         func.max(Measurement.tobs)).\
                                            filter((Measurement.date >= start) & 
                                                   (Measurement.date <= end)).\
                                                    all()

    # close the session
    session.close()
    
    return jsonify(list(np.ravel(summary_from_to_date)))


if __name__ == '__main__':
    app.run(debug=True)