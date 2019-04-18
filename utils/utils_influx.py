from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost', port=8086)

# print (client.get_list_database())

client.create_database('datn')

json_body = [
    {
        "measurement": "metric_id_1",
        "tags": {
            "DataType": "int"
        },
        "time": "2018-03-28T8:01:00Z",
        "fields": {
            "value": 32
        }
    },
    {
        "measurement": "metric_id_2",
        "tags": {
            "DataType": "int"
        },
        "time": "2019-04-28T8:01:00Z",
        "fields": {
            "value": 27
        }
    }
]

client.switch_database('datn')

client.write_points(json_body)

results = client.query('SELECT * FROM "datn"."autogen"."metric_id_2" ')

points = results.get_points()

for point in points:
    print (point)
