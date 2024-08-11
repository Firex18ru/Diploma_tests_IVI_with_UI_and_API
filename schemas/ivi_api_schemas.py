age_categories_schema = {
    "type": "object",
    "properties": {
        "result": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "title": {"type": "string"}
                },
                "required": ["id", "title"],
                "additionalProperties": False
            }
        }
    },
    "required": ["result"],
    "additionalProperties": False
}

all_age_categories_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "title": {"type": "string"}
        },
        "required": ["id", "title"],
        "additionalProperties": False
    }
}

meta_genres_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "hru": {"type": "string"},
            "priority": {"type": "integer"},
            "genre_list": {"type": "array"},
            "icons": {"type": "object"},
            "background": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "content_format": {"type": "string"},
                        "dominant_color": {"type": "string"},
                        "height": {"type": "integer"},
                        "url": {"type": "string"},
                        "width": {"type": "integer"}
                    },
                    "required": ["content_format", "dominant_color", "height", "url", "width"],
                    "additionalProperties": False
                }
            }
        },
        "required": ["id", "title", "hru", "priority", "genre_list", "icons"],
        "additionalProperties": False
    }
}

meta_genres_schema_with_params = {
    "type": "object",
    "properties": {
        "result": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "hru": {"type": "string"},
                    "priority": {"type": "integer"},
                    "genre_list": {"type": "array"},
                    "icons": {"type": "object"},
                    "background": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "content_format": {"type": "string"},
                                "dominant_color": {"type": "string"},
                                "height": {"type": "integer"},
                                "url": {"type": "string"},
                                "width": {"type": "integer"}
                            },
                            "required": ["content_format", "dominant_color", "height", "url", "width"],
                            "additionalProperties": False
                        }
                    },
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "hru": {"type": "string"},
                    "priority": {"type": "integer"}
                },
                "required": ["id", "title", "hru", "priority", "genre_list", "icons"],
                "additionalProperties": False
            }
        }
    },
    "required": ["result"],
    "additionalProperties": False
}

catalogue_schema_catalogue_with_params = {
    "type": "object",
    "properties": {
        "result": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "genres": {"type": "array"},
                    "country": {"type": ["string", "number"]},
                    "year": {"type": "integer"},
                    "rating": {
                        "oneOf": [
                            {"type": "number"},
                            {"type": "null"},
                            {
                                "type": "object",
                                "properties": {
                                    "ready": {
                                        "type": "object",
                                        "properties": {
                                            "votes": {"type": "integer"},
                                            "main": {"type": "number"},
                                            "director": {"type": "number"},
                                            "pretty": {"type": "number"},
                                            "actors": {"type": "number"},
                                            "story": {"type": "number"},
                                        },
                                        "additionalProperties": False,
                                    }
                                },
                                "additionalProperties": False,
                            }
                        ]
                    }
                },
                "required": ["id", "title"],
                "additionalProperties": True
            }
        },
        "count": {"type": "integer"},
        "meta": {"type": "object"},
    },
    "required": ["result", "count", "meta"],
    "additionalProperties": False
}

catalogue_schema_format_movie = {
    "type": "object",
    "properties": {
        "result": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "genres": {"type": "array"},
                    "country": {"type": ["string", "number"]},
                    "year": {"type": "integer"},
                    "rating": {
                        "oneOf": [
                            {"type": "number"},
                            {"type": "null"},
                            {
                                "type": "object",
                                "properties": {
                                    "ready": {
                                        "type": "object",
                                        "properties": {
                                            "votes": {"type": "integer"},
                                            "main": {"type": "number"},
                                            "director": {"type": "number"},
                                            "pretty": {"type": "number"},
                                            "actors": {"type": "number"},
                                            "story": {"type": "number"},
                                        },
                                        "additionalProperties": False,
                                    }
                                },
                                "additionalProperties": False,
                            }
                        ]
                    }
                },
                "required": ["id", "title"],
                "additionalProperties": True
            }
        },
        "count": {"type": "integer"},
        "meta": {"type": "object"},
    },
    "required": ["result", "count", "meta"],
    "additionalProperties": False
}
