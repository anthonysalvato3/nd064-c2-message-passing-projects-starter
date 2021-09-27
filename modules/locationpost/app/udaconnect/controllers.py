from datetime import datetime

from app.udaconnect.models import Location
from app.udaconnect.schemas import (
    LocationSchema,
)
from app.udaconnect.services import LocationService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


@api.route("/locations/<location_id>")
@api.param("creation_time", "Time that this API is called", _in="query")
@api.param("latitude", "Location latitude", _in="query")
@api.param("longitude", "Location longitude", _in="query")
@api.param("person_id", "Unique ID for a given Person", _in="query")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        payload = request.get_json()
        location: Location = LocationService.create(payload)
        return location
