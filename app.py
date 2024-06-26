# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func




#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)


# Save references to each table
Measure = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB

session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs
    )

        @app.route("/api/v1.0/precipitation")
def precipitation():
session = Session(engine)
results = session.query(Measurement.prcp).all()

    session.close()


     return jsonify(precip_data)

   
   
   
    @app.route("/api/v1.0/stations")
def station_list():
session = Session(engine)
results = session.query(Measurement.station).distinct().all()

    session.close()


return jsonify(station_list)