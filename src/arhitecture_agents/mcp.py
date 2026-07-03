{
    "name": "SearchFlights",
    "description": "Retrieve available flights based on input parameters",
    "input_schema": {
        "type": "object",
        "properties": {
            "origin": {"type": "string"},
            "destination": {"type": "string"},
            "departure_date": {"type": "string", "format": "date"}
        },
        "required": ["origin", "destination", "departure_date"]
    },
    "output_schema": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "airline": {"type": "string"},
                "price": {"type": "number"},
                "duration": {"type": "string"}
            }
        }
    }
}