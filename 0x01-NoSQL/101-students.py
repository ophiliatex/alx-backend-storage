#!/usr/bin/env python3
"""" returns all students sorted by average score"""


def top_students(mongo_collection):
    """Returns all students sorted by average"""

    pipeline = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return mongo_collection.aggregate(pipeline)
