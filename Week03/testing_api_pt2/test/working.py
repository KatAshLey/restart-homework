import jsondiff

obj1 = {
    "countries": [
        {
            "name": "Great Britian",
            "cities": [{"name": "Manchester"}, {"name": "London"}],
        }
    ]
}

obj2 = {
    "countries": [
        {
            "name": "Great Britian",
            "cities": [{"name": "Manchester"}, {"name": "London"}],
        }
    ]
}

res = jsondiff.diff(obj1, obj2)

if res:
    print("Diff found")
else:
    print("Same")
