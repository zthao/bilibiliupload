#post data 长度，用于Content-Length
def get_content_length(data):
    length = len(data.keys()) * 2 - 1
    total = ''.join(list(data.keys()) + list(data.values()))
    length += len(total)

int(time_now2())>2 and int(common.time_now2())<12)