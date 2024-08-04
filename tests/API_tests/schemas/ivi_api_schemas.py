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

meta_genres_schema_v5_all_params = {
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
                    }
                },
                "required": ["id", "title", "hru", "priority", "genre_list", "icons"],
                "additionalProperties": False
            }
        }
    },
    "required": ["result"],
    "additionalProperties": False
}

catalogue_schema_catalogue_genre_and_rating = {
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
                    "country": {"type": "string"},
                    "year": {"type": "integer"},
                    "rating": {"type": "number"}

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

catalogue_schema_format_and_3d = {
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
                    "country": {"type": "string"},
                    "year": {"type": "integer"},
                    "rating": {"type": "number"},
                    "hd_available": {"type": "boolean"},
                    "3d_available": {"type": "boolean"}

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