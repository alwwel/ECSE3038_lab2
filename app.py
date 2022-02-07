from flask import Flask, request, jsonify
from datetime import datetime

app=Flask(__name__)

FAKE_Storage = []
FAKE_Storage2 =[]
count=0

#CREATE
@app.route("/profile", methods=["POST"])
def create1():
    user=request.json["Username"]
    fc=request.json["Favourite_color"]
    r=request.json["Role"]
    now = datetime.now()
    clocking = now.strftime("%d/%m/%Y %H:%M:%S")

    Profile = {
        "last_updated"    : clocking,
        "Username"        : user,
        "Role"            : r,
        "Favourite_color" : fc
    }
    FAKE_Storage.append(Profile)
    return jsonify(Profile)

@app.route("/data", methods=["POST"])
def create2():
    desc=request.json["Tank_location_description"]
    lat=request.json["latitude"]
    long=request.json["longitude"]
    p=request.json["percentage_full"]

    global count
    count +=1

    Tank = {
        "id"                        : count,
        "Tank_location_description" : desc,
        "latitude"                  : lat,
        "longitude"                 : long,
        "percentage_full"           : p
    }
    FAKE_Storage2.append(Tank)
    return jsonify(Tank)


#READ
@app.route("/profile", methods=["GET"])
def readd():
    return jsonify(FAKE_Storage)

@app.route("/data", methods=["GET"])
def read2():
    return jsonify(FAKE_Storage2)

#UPDATE
@app.route("/profile", methods=["PATCH"])
def update():
  for user in FAKE_Storage:
      user["Username"]=request.json["Username"]
  for r in FAKE_Storage:
      r["Role"]=request.json["Role"]
  for fc in FAKE_Storage:
      fc["Favourite_color"]=request.json["Favourite_color"]
  return jsonify(FAKE_Storage)


@app.route("/data/<int:id>", methods=["PATCH"])
def update2(id):
    for desc in FAKE_Storage2:
      if desc["id"] == id:
            desc["Tank_location_description"] = request.json["Tank_location_description"]
            for lat in FAKE_Storage2:
                if lat["id"] == id:
                  lat["latitude"] = request.json["latitude"]
                  for lon in FAKE_Storage2:
                    if lon["id"] == id:
                       lon["longitude"] = request.json["longitude"]
                       for p in FAKE_Storage2:
                          if p["id"] == id:
                           p["percentage_full"] = request.json['percentage_full']
    return jsonify(FAKE_Storage2)

#DELETE
@app.route("/data/<int:id>", methods=["DELETE"])
def geridoff(id):
    for desc in FAKE_Storage2:
        if desc["id"] == id:
            FAKE_Storage2.remove(desc)
    return f"Success"


if __name__ == '__main__':
    app.run(
       debug=True,
       port=3000,
       host="0.0.0.0"
    )  