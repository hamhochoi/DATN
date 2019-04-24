{
    "select" : "select_value",
    "from" : "from_value",
    "where" : "platform_id=openhab",    # a condition
    "Rule" : [
        "if" : "temperature>10",      # a condition
        "then" : [      # Actions
            {
                "key" : "led_id_1",
                "value" : "turn on"
            },
            {
                "key" : "led_id_2",
                "value" : "turn off"
            }
        ], 
        "else" : [ # Actions
            {
                "key" : "led_id_3",
                "value" : "turn off"
            }
        ]
    ]
}

# key_words: