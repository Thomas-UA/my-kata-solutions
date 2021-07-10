def openOrSenior(data):
    output_list = []
    for i in data:
        if(i[0] > 54 and i[1] > 7):
            output_list.append("Senior")
        else:
            output_list.append("Open")
    return output_list