subdata1=\
{
            "contextElements": [
                {
                    "entityId": {
                        "id": "RoomTrial10",
                        "type": "Room"
                        },
                    "attributes": [
                            {
                            "name": "temperature",
                            "type": "float",
                            "value": 69
                            },
                            {
                            "name": "pressure",
                            "type": "float",
                            "value": 75
                            }
                        ],
                    "domainMetadata": [
                            {
                            "name": "location",
                            "type": "point",
                            "value": {
                            "latitude": -33.1,
                            "longitude": -1.1
                            }}
                        ]
                }
            ],
            "updateAction": "UPDATE"
}


subdata2=\
{
  "description": "A subscription to get info about RoomTrial10",
  "subject": {
    "entities": [
      {
        "id": "RoomTrial10",
        "type": "Room"
      }
    ],
    "condition": {
      "attrs": [
        "pressure"
      ]
    }
  },
  "notification": {
    "http": {
      "url": "http://180.179.214.211:8888/accumulate"
    },
    "attrs": [
      "temperature"
    ]
  },
  "expires": "2040-01-01T14:00:00.00Z",
  "throttling": 5
}


subdata3=\
{
            "contextElements": [
                {
                    "entityId": {
                        "id": "RoomTrial10",
                        "type": "Room"
                        },
                    "attributes": [
                            {
                            "name": "temperature",
                            "type": "float",
                            "value": 50
                            },
                            {
                            "name": "pressure",
                            "type": "float",
                            "value": 80
                            }
                        ],
                    "domainMetadata": [
                            {
                            "name": "location",
                            "type": "point",
                            "value": {
                            "latitude": -33.1,
                            "longitude": -1.1
                            }}
                        ]
                }
            ],
            "updateAction": "UPDATE"
}

subdata4=\
{
            "contextElements": [
                {
                    "entityId": {
                        "id": "RoomTrial20",
                        "type": "Room"
                        },
                    "attributes": [
                            {
                            "name": "temperature",
                            "type": "float",
                            "value": 69
                            },
                            {
                            "name": "pressure",
                            "type": "float",
                            "value": 75
                            }
                        ],
                    "domainMetadata": [
                            {
                            "name": "location",
                            "type": "point",
                            "value": {
                            "latitude": -33.1,
                            "longitude": -1.1
                            }}
                        ]
                }
            ],
            "updateAction": "UPDATE"
}


subdata5=\
{
  "description": "A subscription to get info about RoomTrial20",
  "subject": {
    "entities": [
      {
        "id": "RoomTrial20",
        "type": "Room"
      }
    ],
    "condition": {
      "attrs": [
        "pressure"
      ]
    }
  },
  "notification": {
    "http": {
      "url": "http://180.179.214.211:8888/accumulate"
    },
    "attrs": [
      "temperature"
    ]
  },
  "expires": "2040-01-01T14:00:00.00Z",
  "throttling": 5
}


subdata6=\
{
            "contextElements": [
                {
                    "entityId": {
                        "id": "RoomTrial20",
                        "type": "Room"
                        },
                    "attributes": [
                            {
                            "name": "temperature",
                            "type": "float",
                            "value": 40
                            },
                            {
                            "name": "pressure",
                            "type": "float",
                            "value": 85
                            }
                        ],
                    "domainMetadata": [
                            {
                            "name": "location",
                            "type": "point",
                            "value": {
                            "latitude": -33.1,
                            "longitude": -1.1
                            }}
                        ]
                }
            ],
            "updateAction": "UPDATE"
}

subdata7=\
{
            "contextElements": [
                {
                    "entityId": {
                        "id": "RoomTrial30",
                        "type": "Room"
                        },
                    "attributes": [
                            {
                            "name": "temperature",
                            "type": "float",
                            "value": 69
                            },
                            {
                            "name": "pressure",
                            "type": "float",
                            "value": 75
                            }
                        ],
                    "domainMetadata": [
                            {
                            "name": "location",
                            "type": "point",
                            "value": {
                            "latitude": -33.1,
                            "longitude": -1.1
                            }}
                        ]
                }
            ],
            "updateAction": "UPDATE"
}


subdata8=\
{
  "description": "A subscription to get info about RoomTrial30",
  "subject": {
    "entities": [
      {
        "id": "RoomTrial30",
        "type": "Room"
      }
    ],
    "condition": {
      "attrs": [
        "pressure"
      ]
    }
  },
  "notification": {
    "http": {
      "url": "http://180.179.214.211:8888/accumulate"
    },
    "attrs": [
      "temperature"
    ]
  },
  "expires": "2040-01-01T14:00:00.00Z",
  "throttling": 5
}



subdata9=\
{
            "contextElements": [
                {
                    "entityId": {
                        "id": "RoomTrial30",
                        "type": "Room"
                        },
                    "attributes": [
                            {
                            "name": "temperature",
                            "type": "float",
                            "value": 44
                            },
                            {
                            "name": "pressure",
                            "type": "float",
                            "value": 60
                            }
                        ],
                    "domainMetadata": [
                            {
                            "name": "location",
                            "type": "point",
                            "value": {
                            "latitude": -33.1,
                            "longitude": -1.1
                            }}
                        ]
                }
            ],
            "updateAction": "UPDATE"
}

